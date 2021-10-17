##########################################################################
## * Program: opensslEnc.py
## * Author: Lake Peterson
## * Date: October 16, 2021
## * Description: Matches a given ciphertext to an encrypted ciphertext from which a matching key is reported if found
## * Input: A .txt file must be provided
## * Output: Determines whther or not a key is found
##########################################################################

##########################################################################
## * Included Libraries
##########################################################################

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

##########################################################################
## * Function: getWords
## * Description: Reads in strings from the words.txt file
## * Parameters: None
## * Pre-Conditions: The file must not be empty
## * Post-Conditions: A list of strings is returned
##########################################################################

def getWords():

    wordList = []
    file = open('words.txt', 'r')

    for line in file:
        newLine = line.strip()
        wordList.append(newLine)

    file.close()

    return wordList

##########################################################################
## * Function: wordPadding
## * Description: Ensures all strings (words) are of the same length
## * Parameters: word, buffer
## * Pre-Conditions: The string (word) must be shorter then 16
## * Post-Conditions: The string (word) is of lenght 16
##########################################################################

def wordPadding(word, buffer):

    for x in range(0, buffer):
        word += ' '

    return word

##########################################################################
## * Function: encValues
## * Description: Encodes the iv and key values
## * Parameters: key
## * Pre-Conditions: Key value
## * Post-Conditions: Number of bytes in the key and iv value are returned
##########################################################################

def encValues(key):

    return bytearray(key, encoding = "utf-8"), bytearray.fromhex("00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")

##########################################################################
## * Function: encMessage
## * Description: Plainext is encrypted in order to determine the ciphertext
## * Parameters: key, iv, word
## * Pre-Conditions: Plaintext is encrypted 
## * Post-Conditions: Ciphertext is returned
##########################################################################

def encMessage(key, iv, word):

    return AES.new(key, AES.MODE_CBC, iv).encrypt(pad(str.encode(word), AES.block_size)).hex()

##########################################################################
## * Function: matchWord
## * Description: Retrieves a words ciphertext and compares to the given ciphertext
## * Parameters: wordList
## * Pre-Conditions: Given ciphertext must be given so that we can compare
## * Post-Conditions: Returns the word if ciphertext matches
##########################################################################

def matchWord(wordList):

    for word in wordList:
        if(len(word) < 16):

            keySize, iv = encValues(wordPadding(word, 16 - len(word)))

            if('8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9' == encMessage(keySize, iv, 'This is a top secret.')):
                return word
        else:
            continue

##########################################################################
## * Function: main
##########################################################################

def main():

    if len(matchWord(getWords())) == 0:
        print("No key exists.")
    else:
        print("A key was found, here is the key -->", matchWord(getWords()))

main()