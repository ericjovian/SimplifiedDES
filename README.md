anyplainfile(pdf,docx,txt,etc.)</br>
- to encrypt a file:<br />
python3 sdes.py -e <10-bit key> < plaintextfile > < ciphertextfile ><br />
eq: python3 sdes.py -e 1010001110 plain.docx cipher.out<br />
<br /><br />

- to decrypt ciphered file:<br />
python3 sdes.py -d <10-bit key> < ciphertextfile > < plaintextfile ><br />
eq: python3 sdes.py -d 1010001110 cipher.out plain.docx<br />
<br /><br />
the code still have some problem validating the 10-bit key binary. It should be an easy fix, but currently busy working on other projects.🙏
<br />
the Permutation function can also be simplified by creating an index swapping function.
