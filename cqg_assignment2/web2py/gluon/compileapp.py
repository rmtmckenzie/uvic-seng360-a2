#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is part of the web2py Web Framework
Copyrighted by Massimo Di Pierro <mdipierro@cs.depaul.edu>
License: LGPLv3 (http://www.gnu.org/licenses/lgpl.html)

Functions required to execute app components
============================================

FOR INTERNAL USE ONLY
"""

import os
import copy
import random
from storage import Storage, List
from template import parse_template
from restricted import restricted, compile2
from fileutils import listdir
from myregex import regex_expose
from languages import translator
from sql import BaseAdapter, SQLDB, SQLField, DAL, Field
from sqlhtml import SQLFORM, SQLTABLE
from cache import Cache
import settings
from cfs import getcfs
import html
import validators
from http import HTTP, redirect
import marshal
import imp
import logging
logger = logging.getLogger("web2py")
import rewrite

try:
    import py_compile
except:
    logger.warning('unable to import py_compile')

is_gae = settings.global_settings.web2py_runtime_gae

TEST_CODE = \
    r"""
def _TEST():
    import doctest, sys, cStringIO, types, cgi, gluon.fileutils
    if not gluon.fileutils.check_credentials(request):
        raise HTTP(401, web2py_error='invalid credentials')
    stdout = sys.stdout
    html = '<h2>Testing controller "%s.py" ... done.</h2><br/>\n' \
        % request.controller
    for key in sorted([key for key in globals() if not key in __symbols__+['_TEST']]):
        eval_key = eval(key)
        if type(eval_key) == types.FunctionType:
            number_doctests = sum([len(ds.examples) for ds in doctest.DocTestFinder().find(eval_key)])
            if number_doctests>0:
                sys.stdout = cStringIO.StringIO()
                name = '%s/controllers/%s.py in %s.__doc__' \
                    % (request.folder, request.controller, key)
                doctest.run_docstring_examples(eval_key,
                    globals(), False, name=name)
                report = sys.stdout.getvalue().strip()
                if report:
                    pf = 'failed'
                else:
                    pf = 'passed'
                html += '<h3 class="%s">Function %s [%s]</h3>\n' \
                    % (pf, key, pf)
                if report:
                    html += CODE(report, language='web2py', \
                        link='/examples/global/vars/').xml()
                html += '<br/>\n'
            else:
                html += \
                    '<h3 class="nodoctests">Function %s [no doctests]</h3><br/>\n' \
                    % (key)
    response._vars = html
    sys.stdout = stdout
_TEST()
"""

class LoadFactory(object):
    """
    Attention: this helper is new and experimental
    """
    def __init__(self,environment):
        self.environment = environment
    def __call__(self, c=None, f='index', args=[], vars={},
                 extension=None, target=None,ajax=False,ajax_trap=False,
                 url=None):
        import globals
        target = target or 'c'+str(random.random())[2:]
        request = self.environment['request']
        if '.' in f:
            f, extension = f.split('.',1)
        if url or ajax:
            url = url or html.URL(request.application, c, f, r=request,
                                  args=args, vars=vars, extension=extension)
            script = html.SCRIPT('web2py_component("%s","%s")' % (url, target),
                                 _type="text/javascript")
            return html.TAG[''](script, html.DIV('loading...', _id=target))
        else:
            c = c or request.controller
            other_environment = copy.copy(self.environment)
            other_request = globals.Request()
            other_request.application = request.application
            other_request.controller = c
            other_request.function = f
            other_request.extension = extension or request.extension
            other_request.args = List(args)
            other_request.folder = request.folder
            other_request.env = request.env
            if not ajax_trap:
                other_request.vars = request.vars
                other_request.get_vars = request.get_vars
                other_request.post_vars = request.post_vars
            else:
                other_request.vars = vars
            other_environment['request'] = other_request
            other_response = globals.Response()
            other_environment['response'] = other_response
            other_response._view_environment = other_environment
            other_request.env.http_web2py_component_location = \
                request.env.path_info
            other_request.env.http_web2py_component_element = target
            other_response.view = '%s/%s.%s' % (c,f, other_request.extension)
            page = run_controller_in(c, f, other_environment)
            if isinstance(page, dict):
                other_response._vars = page
                for key in page:
                    other_response._view_environment[key] = page[key]
                run_view_in(other_response._view_environment)
                page = other_response.body.getvalue()
            js = None
            if ajax_trap:
                link = html.URL(request.application, c, f, r=request,
                                args=args, vars=vars, extension=extension),
                js = "web2py_trap_form('%s','%s');" % (link, target)
            # not sure about this
            # for (name,value) in other_response.headers:
            #     if name == 'web2py-component-command':
            #         js += value
            script = js and html.SCRIPT(js,_type="text/javascript") or ''
            return html.TAG[''](html.DIV(html.XML(page),_id=target),script)


def local_import_aux(name, force=False, app='welcome'):
    """
    In apps, instead of importing a local module
    (in applications/app/modules) with::

       import a.b.c as d

    you should do::

       d = local_import('a.b.c')

    or (to force a reload):

       d = local_import('a.b.c', reload=True)

    This prevents conflict between applications and un-necessary execs.
    It can be used to import any module, including regular Python modules.
    """
    items = name.replace('/','.')
    name = "applications.%s.modules.%s" % (app, items)
    module = __import__(name)
    for item in name.split(".")[1:]:
        module = getattr(module, item)
    if force:
        reload(module)
    return module


"""
OLD IMPLEMENTATION:
    items = name.replace('/','.').split('.')
    filename, modulepath = items[-1], os.path.join(apath,'modules',*items[:-1])
    imp.acquire_lock()
    try:
        file=None
        (file,path,desc) = imp.find_module(filename,[modulepath]+sys.path)
        if not path in sys.modules or reload:
            if is_gae:
                module={}
                execfile(path,{},module)
                module=Storage(module)
            else:
                module = imp.load_module(path,file,path,desc)
            sys.modules[path] = module
        else:
            module = sys.modules[path]
    except Exception, e:
        module = None
    if file:
        file.close()
    imp.release_lock()
    if not module:
        raise ImportError, "cannot find module %s in %s" % (filename, modulepath)
    return module
"""

def build_environment(request, response, session):
    """
    Build the environment dictionary into which web2py files are executed.
    """

    environment = {}
    for key in html.__all__:
        environment[key] = getattr(html, key)

    # Overwrite the URL function with a proxy
    # url function which contains this request.
    environment['URL'] = html._gURL(request)

    for key in validators.__all__:
        environment[key] = getattr(validators, key)
    if not request.env:
        request.env = Storage()
    environment['T'] = translator(request)
    environment['HTTP'] = HTTP
    environment['redirect'] = redirect
    environment['request'] = request
    environment['response'] = response
    environment['session'] = session
    environment['cache'] = Cache(request)
    environment['DAL'] = DAL
    environment['Field'] = Field
    environment['SQLDB'] = SQLDB        # for backward compatibility
    environment['SQLField'] = SQLField  # for backward compatibility
    environment['SQLFORM'] = SQLFORM
    environment['SQLTABLE'] = SQLTABLE
    environment['LOAD'] = LoadFactory(environment)
    environment['local_import'] = \
        lambda name, reload=False, app=request.application:\
        local_import_aux(name,reload,app)
    BaseAdapter.set_folder(os.path.join(request.folder, 'databases'))
    response._view_environment = copy.copy(environment)
    return environment


def save_pyc(filename):
    """
    Bytecode compiles the file `filename`
    """
    py_compile.compile(filename)


def read_pyc(filename):
    """
    Read the code inside a bytecode compiled file if the MAGIC number is
    compatible

    :returns: a code object
    """
    fp = open(filename, 'rb')
    data = fp.read()
    fp.close()
    if not is_gae and data[:4] != imp.get_magic():
        raise SystemError, 'compiled code is incompatible'
    return marshal.loads(data[8:])


def compile_views(folder):
    """
    Compiles all the views in the application specified by `folder`
    """

    path = os.path.join(folder, 'views')
    for file in listdir(path, '^[\w/]+\.\w+$'):
        data = parse_template(file, path)
        filename = ('views/%s.py' % file).replace('/', '_').replace('\\', '_')
        filename = os.path.join(folder, 'compiled', filename)
        fp = open(filename, 'w')
        fp.write(data)
        fp.close()
        save_pyc(filename)
        os.unlink(filename)


def compile_models(folder):
    """
    Compiles all the models in the application specified by `folder`
    """

    path = os.path.join(folder, 'models')
    for file in listdir(path, '.+\.py$'):
        fp = open(os.path.join(path, file), 'r')
        data = fp.read()
        fp.close()
        filename = os.path.join(folder, 'compiled', ('models/'
                                 + file).replace('/', '_'))
        fp = open(filename, 'w')
        fp.write(data)
        fp.close()
        save_pyc(filename)
        os.unlink(filename)


def compile_controllers(folder):
    """
    Compiles all the controllers in the application specified by `folder`
    """

    path = os.path.join(folder, 'controllers')
    for file in listdir(path, '.+\.py$'):
        ### why is this here? save_pyc(os.path.join(path, file))
        fp = open(os.path.join(path,file), 'r')
        data = fp.read()
        fp.close()
        exposed = regex_expose.findall(data)
        for function in exposed:
            command = data + "\nresponse._vars=response._caller(%s)\n" % \
                function
            filename = os.path.join(folder, 'compiled', ('controllers/'
                                     + file[:-3]).replace('/', '_')
                                     + '_' + function + '.py')
            fp = open(filename, 'w')
            fp.write(command)
            fp.close()
            save_pyc(filename)
            os.unlink(filename)


def run_models_in(environment):
    """
    Runs all models (in the app specified by the current folder)
    It tries pre-compiled models first before compiling them.
    """

    folder = environment['request'].folder
    path = os.path.join(folder, 'compiled')
    if os.path.exists(path):
        for model in listdir(path, '^models_.+\.pyc$', 0):
            restricted(read_pyc(model), environment, layer=model)
    else:
        models = listdir(os.path.join(folder, 'models'), '^\w+\.py$',
                         0)
        for model in models:
            layer = model
            if is_gae:
                code = getcfs(model, model,
                              lambda: compile2(open(model, 'r').read(),layer))
            else:
                code = getcfs(model, model, None)
            restricted(code, environment, layer)


def run_controller_in(controller, function, environment):
    """
    Runs the controller.function() (for the app specified by
    the current folder).
    It tries pre-compiled controller_function.pyc first before compiling it.
    """

    # if compiled should run compiled!

    folder = environment['request'].folder
    path = os.path.join(folder, 'compiled')
    badc = 'invalid controller (%s/%s)' % (controller, function)
    badf = 'invalid function (%s/%s)' % (controller, function)
    if os.path.exists(path):
        filename = os.path.join(path, 'controllers_%s_%s.pyc'
                                 % (controller, function))
        if not os.path.exists(filename):
            raise HTTP(404,
                       rewrite.thread.routes.error_message % badf,
                       web2py_error=badf)
        restricted(read_pyc(filename), environment, layer=filename)
    elif function == '_TEST':
        filename = os.path.join(folder, 'controllers/%s.py'
                                 % controller)
        if not os.path.exists(filename):
            raise HTTP(404,
                       rewrite.thread.routes.error_message % badc,
                       web2py_error=badc)
        environment['__symbols__'] = environment.keys()
        fp = open(filename, 'r')
        code = fp.read()
        fp.close()
        code += TEST_CODE
        restricted(code, environment, layer=filename)
    else:
        filename = os.path.join(folder, 'controllers/%s.py'
                                 % controller)
        if not os.path.exists(filename):
            raise HTTP(404,
                       rewrite.thread.routes.error_message % badc,
                       web2py_error=badc)
        fp = open(filename, 'r')
        code = fp.read()
        fp.close()
        exposed = regex_expose.findall(code)
        if not function in exposed:
            raise HTTP(404,
                       rewrite.thread.routes.error_message % badf,
                       web2py_error=badf)
        code = "%s\nresponse._vars=response._caller(%s)\n" % (code, function)
        if is_gae:
            layer = filename + ':' + function
            code = getcfs(layer, filename,  lambda: compile2(code,layer))
        restricted(code, environment, filename)
    response = environment['response']
    vars=response._vars
    if response.postprocessing:
        for p in response.postprocessing:
            vars = p(vars)
    if isinstance(vars,unicode):
        vars = vars.encode('utf8')
    if hasattr(vars,'xml'):
        vars = vars.xml()
    return vars

def run_view_in(environment):
    """
    Executes the view for the requested action.
    The view is the one specified in `response.view` or determined by the url
    or `view/generic.extension`
    It tries the pre-compiled views_controller_function.pyc before compiling it.
    """

    request = environment['request']
    response = environment['response']
    folder = request.folder
    path = os.path.join(folder, 'compiled')
    badv = 'invalid view (%s)' % response.view
    if not isinstance(response.view, str):
        ccode = parse_template(response.view, os.path.join(folder, 'views'),
                               context=environment)
        restricted(ccode, environment, 'file stream')
    elif os.path.exists(path):
        x = response.view.replace('/', '_')
        if request.extension == 'html':
            # for backward compatibility
            files = [os.path.join(path, 'views_%s.pyc' % x),
                     os.path.join(path, 'views_%s.pyc' % x[:-5]),
                     os.path.join(path, 'views_generic.html.pyc'),
                     os.path.join(path, 'views_generic.pyc')]
        else:
            files = [os.path.join(path, 'views_%s.pyc' % x),
                     os.path.join(path, 'views_generic.%s.pyc'
                                  % request.extension)]
        for filename in files:
            if os.path.exists(filename):
                code = read_pyc(filename)
                restricted(code, environment, layer=filename)
                return
        raise HTTP(404,
                   rewrite.thread.routes.error_message % badv,
                   web2py_error=badv)
    else:
        filename = os.path.join(folder, 'views', response.view)
        if not os.path.exists(filename):
            response.view = 'generic.' + request.extension
        filename = os.path.join(folder, 'views', response.view)
        if not os.path.exists(filename):
            raise HTTP(404,
                       rewrite.thread.routes.error_message % badv,
                       web2py_error=badv)
        layer = filename
        if is_gae:
            ccode = getcfs(layer, filename,
                           lambda: compile2(parse_template(response.view,
                                            os.path.join(folder, 'views'),
                                            context=environment),layer))
        else:
            ccode = parse_template(response.view,
                                   os.path.join(folder, 'views'),
                                   context=environment)
        restricted(ccode, environment, layer)

def remove_compiled_application(folder):
    """
    Deletes the folder `compiled` containing the compiled application.
    """
    try:
        path = os.path.join(folder, 'compiled')
        for file in listdir(path):
            os.unlink(os.path.join(path, file))
        os.rmdir(path)
        path = os.path.join(folder, 'controllers')
        for file in os.listdir(path):
            if file.endswith('.pyc'):
                os.unlink(os.path.join(path, file))
    except OSError:
        pass


def compile_application(folder):
    """
    Compiles all models, views, controller for the application in `folder`.
    """
    remove_compiled_application(folder)
    os.mkdir(os.path.join(folder, 'compiled'))
    compile_models(folder)
    compile_controllers(folder)
    compile_views(folder)


def test():
    """
    Example::

        >>> import traceback, types
        >>> environment={'x':1}
        >>> open('a.py', 'w').write('print 1/x')
        >>> save_pyc('a.py')
        >>> os.unlink('a.py')
        >>> if type(read_pyc('a.pyc'))==types.CodeType: print 'code'
        code
        >>> exec read_pyc('a.pyc') in environment
        1
    """

    return


if __name__ == '__main__':
    import doctest
    doctest.testmod()
