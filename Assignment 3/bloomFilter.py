##########################################################################
## * Program: bloomFilter.py
## * Author: Lake Peterson
## * Date: October 31, 2021
## * Description: Bloom Filter script for weak password detection given a set of bad passwords
## * Input: Requires two input files (dictionary.txt and inputPasswords.txt)
## * Output: Outputs a file that gives password detection results
##########################################################################

##########################################################################
## * Included Libraries
##########################################################################

from bitarray import bitarray
import mmh3

##########################################################################
## * Constants
##########################################################################

PASSWORDLISTSIZE = 4294967296
HASHFUNCTIONS = 3

##########################################################################
## * class: BloomFilter
## * Description: Creates a Bloom Filter object for a given password
## * Parameters: object
##########################################################################

class BloomFilter(object):

	##########################################################################
	## * Function: __init__
	## * Description: Initializes the objects state and attributes
	## * Parameters: bloomObject)
	## * Pre-Conditions: Correct files must be provided
	## * Post-Conditions: The bloom filter object has been made correctly
	##########################################################################

	def __init__(bloomObject):

		bloomObject.bitarray = bitarray(PASSWORDLISTSIZE)
		bloomObject.bitarray.setall(0)

	##########################################################################
	## * Function: bloomInsert
	## * Description: A new password is added to the bloom filter
	## * Parameters: bloomObject, password
	## * Pre-Conditions: The bloom object and password must be provided
	## * Post-Conditions: The bit is set true in the bit array
	##########################################################################

	def bloomInsert(bloomObject, password):

		data = []
		
		for x in range(HASHFUNCTIONS):
			data = mmh3.hash(password, x) % PASSWORDLISTSIZE

			bloomObject.bitarray[data] = True

	##########################################################################
	## * Function: bloomLookup
	## * Description: Look to see is the password exists in the bloom filter
	## * Parameters: bloomObject, password
	## * Pre-Conditions: The bloom object and password must be provided
	## * Post-Conditions: Returns whether or no the password is present or not
	##########################################################################

	def bloomLookup(bloomObject, password):

		for x in range(HASHFUNCTIONS):
			data = mmh3.hash(password, x) % PASSWORDLISTSIZE

			if bloomObject.bitarray[data] == True:
				return "'{}' = no\n".format(password)
			return "'{}' = maybe\n".format(password)

##########################################################################
## * Function: main
##########################################################################

def main(): 

	passwordList = open("passwordInput.txt").read().splitlines()
	passwordList.pop(0)

	dictionaryList = open("dictionary.txt").read().splitlines()

	passwordObject = BloomFilter()

	for password in dictionaryList:
		passwordObject.bloomInsert(password)

	output = open("passwordOutput.txt", 'w+')

	for password in passwordList:
		output.write(passwordObject.bloomLookup(password))

main()