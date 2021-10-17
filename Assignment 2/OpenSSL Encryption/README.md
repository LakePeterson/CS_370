## Encrypting with OpenSSL

Matches a given ciphertext to an encrypted ciphertext from which a matching key is reported if found.

**How to run program**

- Ensure that the words.txt file is contained within the same directory as opensslEnc.py

- Ensure that "pycryptodome" is installed. 
- "pycryptodome" can be installed via the following command -> pip3 install pycryptodome

- You may run into issues if "crypto" and "pycrypto" are already installed on your system.
- "crypto" can be uninstalled via the following command -> pip3 uninstall crypto
- "pycrypto" can be uninstalled via the following command -> pip3 uninstall pycrypto

- If all the above dependencies are handled then the program is ready to be run via the command line: python3 opensslEnc.py