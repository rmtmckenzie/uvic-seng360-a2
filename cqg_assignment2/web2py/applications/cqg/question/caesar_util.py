#A2 DONE
# intentionally empty; no util functions needed

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_encrypt(P,K):

	result = []
	for i in P:
		val = ALPHABET.index(i)
		result.append( ALPHABET[ (val + K) % 26 ] )
	return result

