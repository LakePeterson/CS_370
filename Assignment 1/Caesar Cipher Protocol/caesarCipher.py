# ######################################################################################################################
# Caesar Cipher (c) by Bram Lewis
# (c) 2020
#
# Caesar Cipher is licensed under a
# Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
#
# You should have received a copy of the license along with this
# work.  If not, see <http://creativecommons.org/licenses/by-nc-sa/3.0/>.
# ######################################################################################################################
import sys

# ######################################################################################################################
# Global Variables
baseCipherSequence = "abcdefghijklmnopqrstuvwxyz"


# ######################################################################################################################
def main():
    parameterCount = len(sys.argv)

    if parameterCount == 3 and sys.argv[1] == "-p" and sys.argv[2].isnumber():
        key = int(sys.argv[2])
        printKeyMap(key)
    elif parameterCount == 4 and sys.argv[2].isdigit():
        key = int(sys.argv[2])
        if sys.argv[1] == "-e":
            encrypt(key, sys.argv[3])
        elif sys.argv[1] == "-d":
            decrypt(key, sys.argv[3])
        else:
            printCliSyntax()
    elif len(sys.argv) == 2 and sys.argv[1] == "-u":
        unitTests()
    else:
        printCliSyntax()


# ######################################################################################################################
def printCliSyntax():
    print("Syntax:")
    print("python " + sys.argv[0] + " [-e|-d] rotationNumber \"[plaintext|ciphertext] string\"")
    print("python " + sys.argv[0] + " [-p] rotationNumber")
    print("\t-e\tEncryption mode")
    print("\t-d\tDecryption mode")
    print("\t-p\tPrint Key Map")


# ######################################################################################################################
def encrypt(key, plaintext):
    print("Encryption Mode")
    print(f"Key: {key}")
    print(f"Plaintext: {plaintext}")

    ciphertext = rotateString(key, plaintext)
    print(f"Ciphertext: {ciphertext}")


# ######################################################################################################################
def decrypt(key, ciphertext):
    print("Decryption Mode")
    print(f"Key: {key}")
    print(f"Ciphertext: {ciphertext}")

    plaintext = rotateString(-key, ciphertext)
    print(f"Plaintext: {plaintext}")


# ######################################################################################################################
def printKeyMap(key):
    print("Print Key Map")
    print(f"Base:     {baseCipherSequence}")
    print(f"With Key: {rotateString(key, baseCipherSequence)}")


# ######################################################################################################################
def rotateString(key, string):
    newString = ""
    for i, c in enumerate(string):
        newString += rotateCh(key, c)
    return newString


# ######################################################################################################################
def rotateCh(key, ch):
    # This rotation will only modify alpha characters
    # non-alpha characters are ignored
    if ch.isalpha():
        characterIndex = baseCipherSequence.find(ch.lower())
        updatedCharacterIndex = (characterIndex + key) % len(baseCipherSequence)
        returnCh = baseCipherSequence[updatedCharacterIndex]

        # return ch to matching case
        if ch.isupper():
            return returnCh.upper()
        else:
            return returnCh
    else:
        return ch


# ######################################################################################################################
def unitTests():
    print("Unit Tests:")
    test_1()
    test_2()
    test_3()
    test_4()


def displayCompareResults(string1, string2):
    if string1 == string2:
        print("Success!")
    else:
        print("Test Failed!")


def test_1():
    print("-------------------------------------------------------------------------------")
    print("Test start: test_01()")

    # Test Setup
    key = 3
    plaintext1 = "the quick brown fox jumps over the lazy dog. THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."
    expectedCiphertext = "wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj. WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ."

    # Run Test
    ciphertext = rotateString(key, plaintext1)

    # Display Test
    print("rotateString():")
    print(f"plaintext1:          \"{plaintext1}\"")
    print(f"ciphertext:          \"{ciphertext}\"")
    print(f"expectedCiphertext:  \"{expectedCiphertext}\"")
    displayCompareResults(ciphertext, expectedCiphertext)


def test_2():
    print("-------------------------------------------------------------------------------")
    print("Test start: test_02()")

    # Test Setup
    key = 3
    ciphertext = "wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj. WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ."
    expectedPlaintext2 = "the quick brown fox jumps over the lazy dog. THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."

    # Run Test
    plaintext2 = rotateString(-key, ciphertext)

    # Display Test
    print("rotateString():")
    print(f"ciphertext:         \"{ciphertext}\"")
    print(f"plaintext2:         \"{plaintext2}\"")
    print(f"expectedPlaintext2: \"{expectedPlaintext2}\"")
    displayCompareResults(plaintext2, expectedPlaintext2)


def test_3():
    print("-------------------------------------------------------------------------------")
    print("Test start: test_03()")

    # Test Setup
    key = 35
    plaintext1 = "the quick brown fox jumps over the lazy dog. THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."
    expectedCiphertext = "cqn zdrlt kaxfw oxg sdvyb xena cqn ujih mxp. CQN ZDRLT KAXFW OXG SDVYB XENA CQN UJIH MXP."

    # Run Test
    ciphertext = rotateString(key, plaintext1)

    # Display Test
    print("rotateString():")
    print(f"plaintext1:          \"{plaintext1}\"")
    print(f"ciphertext:          \"{ciphertext}\"")
    print(f"expectedCiphertext:  \"{expectedCiphertext}\"")
    displayCompareResults(ciphertext, expectedCiphertext)


def test_4():
    print("-------------------------------------------------------------------------------")
    print("Test start: test_04()")

    # Test Setup
    key = 35
    ciphertext = "cqn zdrlt kaxfw oxg sdvyb xena cqn ujih mxp. CQN ZDRLT KAXFW OXG SDVYB XENA CQN UJIH MXP."
    expectedPlaintext2 = "the quick brown fox jumps over the lazy dog. THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."

    # Run Test
    plaintext2 = rotateString(-key, ciphertext)

    # Display Test
    print("rotateString():")
    print(f"ciphertext:         \"{ciphertext}\"")
    print(f"plaintext2:         \"{plaintext2}\"")
    print(f"expectedPlaintext2: \"{expectedPlaintext2}\"")
    displayCompareResults(plaintext2, expectedPlaintext2)


# ######################################################################################################################
if __name__ == "__main__":
    main()
