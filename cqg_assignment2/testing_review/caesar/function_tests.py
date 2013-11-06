'''
SENG 360 : A2 2013-11-06
	Paul Hunter
	Morgan McKenzie

Functional Testing of the Caesar_util.caesar_encrypt method
using a different implementation as a cross check measure. 

'''

import caesar_util
import random


tests = [
[0,1,2,3,10], 
[0,1,24,25], 
['ABYZ', 'CDEFGHIJKLMNOPQRSTUVWX'], 
]

'''
Purpose:
	Run the tests against the caesar_util.caesar_encrpyt method
Preconditions:
	Tests (defined globally) is a list of length three which contains
		A list of lengths
		A list of keys
		A list of alphabets

'''
def run_tests():
	for l in tests[0]:
		for k in tests[1]:
			for alphabet in tests[2]:
				p = generate_plain_text(l, alphabet)
				c_internal = generate_caesar_result(k, p)
				c_caesar_util = ''.join(caesar_util.caesar_encrypt(p, k))
				if(c_internal != c_caesar_util):
					print("Test Failed!: \n" \
						"Plaintext: '" + p + "'\n" \
						"Key: " + str(k) + "\n" \
						"Expected Result: '" + c_internal + "'\n" \
						"Provided Result: '" + c_caesar_util + "'\n")	
		
'''
Purpose:
	To generate a string of specified length using a specified alphabet
Preconditions:
	size: an integer specifying the size of plain text to generate
		size >= 0
	alphabet: a string of 'A....Z' from which to choose characters from
		len(alphabet) > 0
Returns:
	A string of length 'size' formed using the characters in 'alphabet'
'''
def generate_plain_text(size, alphabet):
	plain_text = ''	
	max_a_index = len(alphabet) - 1
	for i in range(size):
		plain_text += alphabet[random.randint(0, max_a_index)]
	return plain_text
'''
Purpose:
	A caesar_encrypt method used to cross check the caesar_encrypt method in caesar_util
Preconditions:
	plaintext: a String of A....Z
	key: an integer
Returns:
	A encrypted version of plaintext using the key
	which forms a strings of A....Z
'''
def generate_caesar_result(key, plaintext):
	C = ''
	for c in plaintext:
		c_index = ((ord(c) - ord('A')) + key) % 26
		C += chr(c_index + ord('A'))
	return C

if __name__=="__main__":
	run_tests()

