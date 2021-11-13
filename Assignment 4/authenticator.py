##########################################################################
## * Program: authenticator.py
## * Author: Lake Peterson
## * Date: November 14, 2021
## * Description: A simple otp authenticator that works with Google Auth
## * Input: Command line arguments
## * Output: A generated QR code and OTP code that changes every 30 seconds
##########################################################################

##########################################################################
## * Included Libraries
##########################################################################

import sys
import qrcode
import pyotp
import random
import string
import time

##########################################################################
## * Function: commands
## * Description: Error handling and interprets command line arguments
## * Parameters: None
## * Pre-Conditions: Correct arguments must be present along with correct amount
## * Post-Conditions: Program interprets the correct function to execute
##########################################################################

def commands():

    if len(sys.argv) <= 1 or len(sys.argv) >= 3 and sys.argv[1] != "--generate-qr" and sys.argv[1] != "--get-otp":
        print("The command you provided was incorrect try --generate-qr or --get-otp")
        exit()
    elif sys.argv[1] == "--generate-qr":
        generateQR()
        exit()
    elif sys.argv[1] == "--get-otp":
        getOTP()
        exit()

##########################################################################
## * Function: generateQR
## * Description: Generates a QR code from a Google Auth URI
## * Parameters: None
## * Pre-Conditions: None
## * Post-Conditions: A QR Code will be created along with corresponding key
##########################################################################

def generateQR():

    user = str('example@google.com')
    issuer = str('Secure App')
    secret = ''.join(random.choice(string.ascii_uppercase) for i in range(32))
    
    file = open("./key", "w")
    file.write(secret)
    file.close()

    qrcode.make("otpauth://totp/" + issuer + ":" + user + "?secret=" + secret + "&issuer=" + issuer).save("./qrCode.png")

    print("QR Code has been created successfully!")

##########################################################################
## * Function: getOTP
## * Description: Prints out the current OTP Code every 30 seconds
## * Parameters: None
## * Pre-Conditions: The corresponidng key made in generateQR must be present
## * Post-Conditions: Current OTP Code is displayed
##########################################################################

def getOTP():

    file = open('./key', 'r')

    for line in file:
        key = line.strip()

    file.close()

    while(True):
        totp = pyotp.TOTP(key)
        print("OTP Code:", totp.now())
        time.sleep(30)

##########################################################################
## * Function: main
##########################################################################

def main(): 

    commands()

main()