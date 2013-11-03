# NOTE: does not work for code_activator_question_verifier.py
#	that file needs path to web2py/applications/cqg/

absolute_path_to_cqg=~/cqg

export PATH=$PATH:$absolute_path_to_cqg/bin/

export PYTHONPATH=$absolute_path_to_cqg/web2py/applications/cqg/question/:\
$absolute_path_to_cqg/web2py/applications/cqg/
