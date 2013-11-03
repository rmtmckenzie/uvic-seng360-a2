import math
import copy

# counting functions ******************************************************

def n_c_k(n,k):
	'''
	Purpose
		return C(n,k)
	Precondition
		n,k strictly positive integers
		n >= k
	'''
	return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

# Group_list ******************************************************

class Group_list:
	'''
	A group list is of the form:
	[
		[g_0, h_0_0, h_0_1, ...,h_0_N-1 ]
		[g_1, h_1_0, h_1_1, ...,h_1_N-1 ]
		...
	]
	where
		group name g_i is a string unique among the groups
		each hotspot vector h_i_j is a list of length N > 0
	TODO: factor out to here the pur/pre from the generate functions
	'''
	def __init__(self,group_list,vector_length):
		'''
		purpose
		preconditions
			group_list is a legal group list with vectors
			of length vector_length
		'''
		self.vector_length = vector_length
		self.group_list = list(group_list)
		
	def cross_product(self,suffix,indexes):
		'''
		purpose
			if name is None
				generate new vectors in the existing groups by
				applying cross_product_sublist to the
				current vectors
			else
				generate one new group for each vector by
				(1) applying cross_product_sublist to the
				current vectors
				(2) appending suffix % i to the current
				group name, with i set to 0, 1, 2, ...
		preconditions
			if name is None
				suffix: a string containing exactly one %i
			indexes
				each element in range(vector_length)
				no duplicates, sorted ascending
		'''
		G = [ ]
		for g in self.group_list:
			if suffix == None:
				g0 = [g[0]]
				G.append(g0)
				for h_vector in g[1:]:
					for h in cross_product_sublist \
					 (h_vector,indexes):
						g0.append(h)
			else:
				base_name = g[0]
				for h_vector in g[1:]:
					for i,g0 in enumerate \
					 (cross_product_sublist
					 (h_vector,indexes)):
						g0 = [base_name+suffix%i,g0]
						G.append(g0)
		self.group_list = G
		
	def generalize(self,suffix,indexes,count):
		'''
		purpose
			if name is None
				generate new vectors in the existing groups by
				applying generalize_sublist, with count
				hotspots, to the current vectors
			else
				generate one new group for each vector by
				(1) applying generalize_sublist, with count
				hotspots, to the current vectors
				(2) appending suffix % i to the current
				group name, with i set to 0, 1, 2, ...
		preconditions
			if name is None
				suffix: a string containing exactly one %i
			indexes
				each element in range(vector_length)
				no duplicates, sorted ascending
			count: in [1,len(indexes)]
		'''
		G = [ ]
		for g in self.group_list:
			if suffix == None:
				g0 = [g[0]]
				G.append(g0)
				for h_vector in g[1:]:
					for h in generalize_sublist \
					 (h_vector,count,indexes):
						g0.append(h)
			else:
				base_name = g[0]
				for h_vector in g[1:]:
					for i,g0 in enumerate \
					 (generalize_sublist
					 (h_vector,count,indexes)):
						g0 = [base_name+suffix%i,g0]
						G.append(g0)
		self.group_list = G

	def substitute(self,suffix,indexes,value_list):
		'''
		purpose
			if name is None
				generate new vectors in the existing groups by
				applying substitute_sublist to the
				current vectors
			else
				generate one new group for each vector by
				(1) applying substitute_sublist to the
				current vectors
				(2) appending suffix % i to the current
				group name, with i set to 0, 1, 2, ...
		preconditions
			if name is None
				suffix: a string containing exactly one %i
			indexes
				each element in range(vector_length)
				no duplicates, sorted ascending
		'''
		G = [ ]
		for g in self.group_list:
			if suffix == None:
				g0 = [g[0]]
				G.append(g0)
				for h_vector in g[1:]:
					for h in substitute_sublist \
					 (h_vector,indexes,value_list):
						g0.append(h)
			else:
				base_name = g[0]
				for h_vector in g[1:]:
					for i,g0 in enumerate \
					 (substitute_sublist
					 (h_vector,indexes,value_list)):
						g0 = [base_name+suffix%i,g0]
						G.append(g0)
		self.group_list = G

# sublist functions ******************************************************

def cross_product_sublist(L,indexes):
	'''
	purpose
		return a list containing all L0 where
			if i in indexes: L0[i] in L[i]
			else: L0[i] == L[i]
	preconditions
		for i in range(len(L)):
			if i in indexes: L[i] is a list of string or number
			else: L[i] is a string
		indexes
			in range(len(L)), no duplicates, sorted ascending
	'''
	# extract sublist for cross product
	sublist = [ L[i] for i in indexes ]

	# generate sublist cross product
	C = cross_product(sublist)

	# embed each cross product element in a copy of L
	LL = [ ]
	for c in C:
		# create a new group, selecting from L and c
		c_iter = iter(c)
		LL.append([ c_iter.next() if i in indexes else L[i]
		 for i in range(len(L))])

	return LL

def generalize_sublist(L,n,indexes):
	'''
	purpose
		return a list containing all the generalizations of L
		with n holes of the sublist of L specified by sublist_indexes
		return the generalizations "embedded" in the original L values
	preconditions
		L: list of numbers or strings
		n in [0..len(sublist_indexes)-1]
		indexes:
			in [0..len(full_list)-1]
			no duplicates
			sorted ascending
	'''
	# extract sublist for generalization
	sublist = [ L[i] for i in indexes ]

	# generalize sublist
	G = generalize(sublist,n)

	# embed each generalization in a copy of L
	LL = [ ]
	for g in G:
		# create a new group, selecting from L and g
		g_iter = iter(g)
		LL.append([ g_iter.next() if i in indexes else L[i]
		 for i in range(len(L)) ])

	return LL

def substitute_sublist(L,indexes,values):
	'''
	purpose
		Return a list of new lists using by substituting in L
		the value_list elements at the positions in indexes
	preconditions
		L: list of numbers or strings
		indexes:
			in [0..len(full_list)-1]
			no duplicates
			sorted ascending
		values
			list of lists of numbers or strings
			each sublist is of length len(indexes)
	'''
	LL = [ ]
	for v in values:
		v_iter = iter(v)
		LL.append([ v_iter.next() if i in indexes else L[i]
		 for i in range(len(L)) ])

	return LL

def two_cover_sublist(L,indexes):
	'''
	purpose
		return a list containing all L0 where
			if i in indexes: L0[i] in L[i]
			else: L0[i] == L[i]
	preconditions
		for i in range(len(L)):
			if i in indexes: L[i] is a list of string or number
			else: L[i] is a string
		indexes
			in range(len(L)), no duplicates, sorted ascending
	'''
	# extract sublist for cross product
	sublist = [ L[i] for i in indexes ]

	# generate sublist two cover
	C = two_cover(sublist)

	# embed each cross product element in a copy of L
	return substitute_sublist(L,indexes,C)

# primitives ******************************************************

def cross_product(domains):
	'''
	purpose
		return a list containing the cross product of domains
	precondition
		domains is a list of lists containing string, float, or integer
	examples
	'''
	L = []
	for row in genCPRow(domains):
		L.append(row)
	return L

def generalize(L,n):
	'''
	Purpose
		return a list containing every generalization of L with exactly
			n occurrences of None
		where
		G is a generalization of L if G can be obtained
			from L by replacing one or more elements of L with None
	Precondition
		L is a list of string, float, or integer
		n is a non-negative integer
	'''
	G_list = []
	if n == 0:
		G_list.append(L)
	elif n == len(L):
		G_list.append([None]*len(L))
	else:
		for i in range(len(L)-n):
			prefix = L[:i]

			# add to G_list:
			#	all generalizations with None in position i
			for suffix in generalize(L[i+1:],n-1):
				G = prefix + [None] + suffix
				if G not in G_list:
					G_list.append(G)

			# add to G_list:
			#	all generalizations with L[i] in position i
			for suffix in generalize(L[i+1:],n): # with no None
				G = prefix + [L[i]] + suffix
				if G not in G_list:
					G_list.append(G)
	return G_list


def choose_k(L, k):
	'''
	Purpose
		Return a list of the sublists of L of length k.
	Precondition
		L: list of string or number
		k: integer, in [0..len(L)]
	'''
	return list(choose_k_yield(L,k))
def choose_k_yield(L,k):
	for i in range(len(L)):
		if k == 1:
			yield [L[i],]
		else:
			for next in choose_k(L[i+1:len(L)], k-1):
				yield [L[i],] + next

def two_cover(domains):
	'''
	Purpose
		return a two-cover of domains
	Precondition
		domains is a list of lists containing string, float, or integer
	'''
	# calculate domain sizes
	domain_sizes = []
	for i in range(len(domains)):
		domain_sizes.append( len(domains[i]) )

	# generate a two-cover and return it
	L = []
	for row in gen2Cover(domain_sizes):
		tuple = [None]*len(row)
		for i in range(len(row)):
			tuple[i] = domains[i][row[i]]
		L.append(tuple)
	return L

def genCPRow(domains):
	'''
	Purpose
		yields each row in cross product of the n domains
	Precondition
		domains is a list containing n domains over which to form
		 cross product
		must specify at least one domain
	'''
	# if there is more than one domain specified
	if len(domains) > 1:
		# get a row of the cross product of the first n-1 domains
		for sublist in genCPRow(domains[:-1]):
			# for every element in this domain, append it to row
			for item in iter(domains[ len(domains)-1 ]):
				yield  sublist + [item]

	# if only one domain given, yield its elements
	else:
		for item in iter(domains[ len(domains)-1 ]):
			yield [item]

def gen2Cover(domainSizes):
	'''
	Purpose
		generates a 2-cover of index vectors of a set of domains
		yields rows in the 2-cover of the index vectors of the domains
	Precondition
		domainSizes is list of sizes of each domain
		domain sizes must be nonzero.
	'''
	indexVectors = []
	for i in range(len(domainSizes)):
		indexVectors.append( range(domainSizes[i]) )

	# yield each row in the 2-cover of index vectors.
	hc = HillClimb(indexVectors)
	for row in iter(hc):
		yield row

STRENGTH = 2
class HillClimb:
	'''
	a heuristic search for finding the optimal solution for a pairwise
	 (strength 2) cover
	'''
	def __init__(self, dv):
		self.domainVector = dv
		self.pairSet = []

	# yields test tuples from the given domains
	def gen(self):
		if len(self.domainVector) == 1:
			for i in self.domainVector[0]:
				yield [i]
		else:
			# calculate all pairs
			self.pairSet = self.makePairs()
			# yield first tuple and remove from pairs
			tpl = [domain[0] for domain in self.domainVector]
			yield tpl
			self.removePairs(tpl)

			# perform hill climbing while there are pairs to add
			while len(self.pairSet) > 0:
				# create initial tuple
				p = self.pairSet[0]
				tpl = []
				indices = [d[1] for d in p]
				values = [d[0] for d in p]
				for i in xrange(len(self.domainVector)):
					if i in indices:
						tpl.append(
						 values[indices.index(i)])
					else:
						tpl.append(
						 self.domainVector[i][0])

				# see if there is a better tuple by analyzing
				# neighbours of tpl
				numPairs = 0
				maxTuple = tpl
				maxPairs = self.numPairs(tpl)
				while numPairs < maxPairs:
					numPairs = maxPairs
					tpl = maxTuple
					# try to find new tuple and better
					# newPairs2
					for i in xrange(len(tpl)):
						domain = self.domainVector[i]
						for j in xrange(len(domain)):
							newTuple = \
							 copy.copy(tpl)
							newTuple[i] = domain[j]
							# OPTIMIZATION NOTE:
							# Could cache newPairs
							# value as it may be
							# recalculated many
							# times
							newPairs = \
							 self.numPairs(newTuple)
							if newPairs > maxPairs:
								maxPairs = \
								 newPairs
								maxTuple = \
								 newTuple

				# yield new tuple
				yield tpl
				self.removePairs(tpl)

	# add pairs generated by a new domain to the pairSet
	def makePairs(self):
		pairs = []
		# create the first element in the pair
		for i in xrange(len(self.domainVector)-STRENGTH+1):
			d1 = self.domainVector[i]
			for i1 in xrange(len(d1)):
				e1 = (d1[i1], i)
				# add elements from subsequent domains
				for j in xrange(i+1, len(self.domainVector)):
					d2 = self.domainVector[j]
					for j1 in xrange(len(d2)):
						e2 = (d2[j1], j)
						p = (e1, e2)
						pairs.append(p)
		return pairs

	# remove pairs that are in tuple from the pairSet
	def removePairs(self, tpl):
		for i in xrange(len(tpl)-1):
			e1 = (tpl[i], i)
			for j in xrange(i+1, len(tpl)):
				e2 = (tpl[j], j)
				p = (e1, e2)
				try:
					self.pairSet.remove(p)
				except ValueError:
					pass

	# count pairs that are in tuple from the pairSet
	def numPairs(self, tpl):
		count = 0
		for i in xrange(len(tpl)-1):
			e1 = (tpl[i], i)
			for j in xrange(i+1, len(tpl)):
				e2 = (tpl[j], j)
				p = (e1, e2)
				if p in self.pairSet:
					count += 1
		return count

	# make this object iterable
	def __iter__(self):
		return self.gen()
