## OTP

A program that generates a one-time password that can work with existing implementations such as the Google Authenticator App

**How to run program**

- Ensure that "qrcode" is installed. 
- "qrcode" can be installed via the following command -> pip install qrcode

- Ensure that "pyotp" is installed. 
- "pyotp" can be installed via the following command -> pip install pyotp

- Ensure that "pillow" is installed. 
- "pillow" can be installed via the following command -> pip3 install pillow

- If all the above dependencies are handled then the program is ready to be run via the command line.

- The program needs to be ran in the following order:

1. python3 authenticator.py --generate-qr
2. python3 authenticator.py --get-otp

- Once the above has been completed a QR will have been generated, a key will have been made and an OTP Code will be presented every 30 seconds.