command: 
to encrypt a file:
python3 sdes.py -e <10-bit key> <plaintextfile> <ciphertextfile>
eq: python3 sdes.py -e 1010001110 plain.docx cipher.out
anyplainfile(couldbe pdf,docx,txt,etc.)

to decrypt ciphered file:
python3 sdes.py -d <10-bit key> <ciphertextfile> <plaintextfile>
eq: python3 sdes.py -d 1010001110 cipher.out plain.docx

  
the code still have some problem validating the 10-bit key binary. It should be an easy fix, but too busy working on other things.🙏
