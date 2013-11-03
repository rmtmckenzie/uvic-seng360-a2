import generate_util

# counting -------------------------------------------------------
cut = 'n_c_k'
actual = generate_util.n_c_k(3,2)
expected = 3
message = '''Error in %s:
\tactual: %s
\texpect: %s
if actual != expected:
	print message % (cut,str(actual),str(expected))
'''

# Group_list -------------------------------------------------------

# ********** cross_product
G = generate_util.Group_list([ ['g', [[0,1], 'x', [2,3]]] ],3)
G.cross_product(None,[0,2])
actual = G.group_list
expected = [       
	['g', [0, 'x', 2], [0, 'x', 3], [1, 'x', 2], [1, 'x', 3]],
]
message = '''Error in %s:
\tactual: %s
\texpected: %s
'''
if actual != expected:
	print message % (cut,str(actual),str(expected))

cut = 'cross_product'
G = generate_util.Group_list([ ['g', [[0,1], 'x', [2,3]]] ],3)
G.cross_product('_%i',[0,2])
actual = G.group_list
expected = [       
	['g_0', [0, 'x', 2]],
	['g_1', [0, 'x', 3]],
	['g_2', [1, 'x', 2]],
	['g_3', [1, 'x', 3]],
]
message = '''Error in %s:
\tactual: %s
\texpected: %s
'''
if actual != expected:
	print message % (cut,str(actual),str(expected))

# ********** generalize
cut = 'generalize'
G = generate_util.Group_list([ ['g',[1,2,3,4]] ],4)
G.generalize(None,[1,2,3],2)
actual = G.group_list
expected = [       
	[ 'g', [1,None,None,4], [1,None,3,None], [1,2,None,None] ],
]
message = '''Error in %s:
\tactual: %s
\texpected: %s
'''
if actual != expected:
	print message % (cut,str(actual),str(expected))

cut = 'generalize'
G = generate_util.Group_list([ ['g',[1,2,3,4]] ],4)
G.generalize('_%i',[1,2,3],2)
actual = G.group_list
expected = [       
	[ 'g_0', [1,None,None,4],],
	[ 'g_1', [1,None,3,None],],
	[ 'g_2', [1,2,None,None] ],
]
message = '''Error in %s:
\tactual: %s
\texpected: %s
'''
if actual != expected:
	print message % (cut,str(actual),str(expected))

# ********** substitute
cut = 'substitute'
G = generate_util.Group_list([ ['g',[1,'x',2]] ],3)
G.substitute(None,[0,2],[[4,5],[6,7]])
actual = G.group_list
expected = [       
	[ 'g', [4, 'x', 5], [6, 'x', 7] ],
]
message = '''Error in %s:
\tactual: %s
\texpected: %s
'''
if actual != expected:
	print message % (cut,str(actual),str(expected))

cut = 'substitute'
G = generate_util.Group_list([ ['g',[1,'x',2]] ],3)
G.substitute('_%i',[0,2],[[4,5],[6,7]])
actual = G.group_list
expected = [       
	['g_0', [4, 'x', 5]],
	['g_1', [6, 'x', 7]],
]
message = '''Error in %s:
\tactual: %s
\texpected: %s
'''
if actual != expected:
	print message % (cut,str(actual),str(expected))

# sub_list -------------------------------------------------------

cut = 'cross_product_sublist'
actual = generate_util.cross_product_sublist([[1,2],3,['a','b']], [0,2])
expected = [ [1,3,'a'], [1,3,'b'], [2,3,'a'], [2,3,'b'] ]
message = '''Error in %s:
\tactual: %s
\texpected: %s
'''
if actual != expected:
	print message % (cut,str(actual),str(expected))

cut = 'generalize_sublist'
actual = generate_util.generalize_sublist([1,'a',2],1,[0,2])
expected = [ [None,'a',2], [1,'a',None] ]
message = '''Error in %s:
\tactual: %s
\texpected: %s
'''
if actual != expected:
	print message % (cut,str(actual),str(expected))

cut = 'substitute_sublist'
actual = generate_util.substitute_sublist([1,2,3],[0,2],[[4,5],[6,7]])
expected = [ [4,2,5], [6,2,7] ]
message = '''Error in %s:
\tactual: %s
\texpected: %s
'''
if actual != expected:
	print message % (cut,str(actual),str(expected))

cut = 'two_cover_sublist'
actual = generate_util.two_cover_sublist([[1,2],[3,4],['a','b']], [0,1,2])
expected = [[1, 3, 'a'], [2, 4, 'a'], [1, 4, 'b'], [2, 3, 'b']]
message = '''Error in %s:
\tactual: %s
\texpected: %s
'''
if actual != expected:
	print message % (cut,str(actual),str(expected))

# primitives ----------------------------------------------------

# ********** cross_product

# cross product of 1 domain
actual = generate_util.cross_product([[1,2]])
expected = [[1],[2]]
if actual != expected:
	print 'Error:\n\tactual: %s\n\texpected: %s' % (str(actual),str(expected))

# cross product of 2 domains
actual = generate_util.cross_product([[1,2],[3,4]])
expected = [[1,3],[1,4],[2,3],[2,4]]
if actual != expected:
	print 'Error:\n\tactual: %s\n\texpected: %s' % (str(actual),str(expected))

# ********** generalize

# None count is 0
actual = generate_util.generalize([1,2,3],0)
expected = [[1,2,3]]
if actual != expected:
	print 'Error:\n\tactual: %s\n\texpected: %s' % (str(actual),str(expected))

# None count is equal to list length
actual = generate_util.generalize([1,2,3],3)
expected = [[None,None,None]]
if actual != expected:
	print 'Error:\n\tactual: %s\n\texpected: %s' % (str(actual),str(expected))

# None count is not equal to list length
actual = generate_util.generalize([1,2,3],1)
expected = [[None,2,3],[1,None,3],[1,2,None]]
if actual != expected:
	print 'Error:\n\tactual: %s\n\texpected: %s' % (str(actual),str(expected))

# ********** choose_k

cut = 'choose_k'
actual = generate_util.choose_k(range(3),2)
expected = [ [0,1], [0,2], [1,2] ]
message = '''Error in %s:
\tactual: %s
\texpected: %s
'''
if actual != expected:
	print message % (cut,str(actual),str(expected))

actual = generate_util.choose_k(range(3),1)
expected = [ [0], [1], [2] ]
message = '''Error in %s:
\tactual: %s
\texpected: %s
'''
if actual != expected:
	print message % (cut,str(actual),str(expected))

# ********** two_cover

# two-cover of 2 domains
actual = generate_util.two_cover([[1,2],[3,4]])
expected = [[1,3],[1,4],[2,3],[2,4]]
if actual != expected:
	print 'Error:\n\tactual: %s\n\texpected: %s' % (str(actual),str(expected))

# two-cover of 3 domains
actual = generate_util.two_cover([[1,2],[3,4],[5,6]])
expected = [[1,3,5],[2,4,5],[1,4,6],[2,3,6]]
if actual != expected:
	print 'Error:\n\tactual: %s\n\texpected: %s' % (str(actual),str(expected))
