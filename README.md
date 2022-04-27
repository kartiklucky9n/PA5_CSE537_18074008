# elgamalcrypto
Simple Python Elgamal Encryption and Decryption Tool

This script was mostly used for me to learn how Elgamal works.

## Helpful Resources:
- Christof Paar's video on Elgamal - https://www.youtube.com/watch?v=tKNY1zhK3sQ
- Christof Paar's book on Cryptography - https://www.amazon.com/Understanding-Cryptography-Textbook-Students-Practitioners/dp/3642041000/


## Example

```
Enter message to encrypt: a secret message
-------------------------------------  --------------------------------------------------
MESSAGE by Bob         :               a secret message
MESSAGE converted to an int (M) :      129103609600536100655502058853916305253
A random Prime number (P)      :       17399918714963399283140457062142519720612521390919
The generator Generator (G)         :  1827178909982224099933892317951250059877141690539
Alice's genrated private key (X) :     6120736563726574206d657373616765
Bob's generated private key (R) :      17106961568938184622314428513362401099249091283444
Shared secret (H)     :                13535287939588736019692026449407657368393420938481
Encrypted Message (C1):                6147182437054136963664182136473303530625104037644
Encrypted Message (C2):                3161475026220550691236852931572571273559982267509
Decrypted Integer (dm):                129103609600536100655502058853916305253
Decrypted Hex (x)     :                6120736563726574206d657373616765
Decrypted Message     :                b'a secret message'
-------------------------------------  --------------------------------------------------
```


