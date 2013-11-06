#A2 DONE
# intentionally empty; no util functions needed

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_encrypt(P,K):
	'''Preconditions:
	P is a string of characters in the range A...Z
	K is a positive integer
	'''
	result = []
	for i in P:
		val = ALPHABET.index(i)
		result.append( ALPHABET[ (val + K) % 26 ] ) ###DR4
	return result

