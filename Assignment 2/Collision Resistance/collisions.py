##########################################################################
## * Program: collisions.py
## * Author: Lake Peterson
## * Date: October 16, 2021
## * Description: Calculates average attempts for strong and weak collisions
## * Input: None
## * Output: Outputs average attempts for strong and weak collisions
##########################################################################

##########################################################################
## * Included Libraries
##########################################################################

import hashlib
import random
import string

##########################################################################
## * Function: createString
## * Description: Creates a random string of length 10
## * Parameters: None
## * Pre-Conditions: An emtpy string must be initialized
## * Post-Conditions: A length 10 random string is returned
##########################################################################

def createString():

    newString = ''.join(random.choice(string.ascii_letters) for i in range(10))

    return newString

##########################################################################
## * Function: hashString
## * Description: Creates a hash for value for the passed in string
## * Parameters: givenString
## * Pre-Conditions: A string must be provided
## * Post-Conditions: Hash value created and returned for given string
##########################################################################

def hashString(givenString):

    hashValue = hashlib.sha256(givenString.encode())

    return hashValue.hexdigest()

##########################################################################
## * Function: weakCollision
## * Description: Calulates number of attempts to break the weak collision resistance property
## * Parameters: None
## * Pre-Conditions: Two random strings must be generated
## * Post-Conditions: Returns the number of attempts
##########################################################################

def weakCollision():

    testCount = 0
    netCollisions = 0

    stringOne = createString()

    for i in range(50):
       
        attemptNum = 0
        testCount += 1
       
        while 1:
            stringTwo = createString()

            if stringOne == stringTwo:
                continue
            else:
                hashValueOne = hashString(stringOne)
                hashValueTwo = hashString(stringTwo)
            
                attemptNum += 1

            if(hashValueOne[0:6] == hashValueTwo[0:6]):
                break

        netCollisions += attemptNum
    average = netCollisions / testCount

    print("Number of tests ran: %s" % (testCount))
    print("Average attempts to break: %s" % average)

##########################################################################
## * Function: freeCollision
## * Description: Calulates number of attempts to break the collision free resistance property
## * Parameters: None
## * Pre-Conditions: A random string must be generated
## * Post-Conditions: Returns the number of attempts
##########################################################################

def freeCollision():
    
    testCount = 0
    netCollisions = 0
    
    for i in range(50):
        attemptNum = 0
        testCount += 1

        while 1:
            stringOne = createString()
            stringTwo = createString()

            if stringOne == stringTwo:
                continue
            else:
                hashValueOne = hashString(stringOne)
                hashValueTwo = hashString(stringTwo)  

                attemptNum += 1

                if(hashValueOne[0:6] == hashValueTwo[0:6]):
                    break

        netCollisions += attemptNum
    average = netCollisions / testCount

    print("Number of tests ran: %s" % (testCount))
    print("Average attempts to break: %s" % average)

##########################################################################
## * Function: main
##########################################################################

def main():

    print("Weak Collision Resistance Property Test\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    weakCollision()

    print("Collision Free Resistance Property Test\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    freeCollision()

main()