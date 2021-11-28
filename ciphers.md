
### Base64

The original ciphertext is encoded in base64 format. Base64 encoding converts binary data to an ASCII string format,
by converting 8-bit sequences into a base 64 representation, in which each character has 6 bits. 
3 bytes(=24 bits) can be represented by 4 characters in base64, as 4*6 = 24 bits. The character set in base64 representation is "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/". 


While decoding, we convert the entire ciphertext to their corresponding binary value according to the character set. Move along the string from left to right and group the bits into 8-bit binary, discarding the characters that do not have 8 complete bits(present at the end of the string). We can do so because these 0s are appended during encoding, and do not have any significance in the original plaintext. On converting these 8-bit binary groups to their ASCII values, we obtain the original string.

### Caesar Cipher

The Caesar Cipher is a substitution cipher in which each letter of the plaintext is rotated by a certain number of letters, either left or right. 

In the second step of decryption, we find that the plaintext is obtained by rotating the letters to the right by 4 positions, so the key is 4. In case the letter goes beyond Z, we begin again from A, that is, it wraps around to the beginning of the alphabet.

In the last step of decryption, the plaintext is obtained by rotating the letters to the right by 5(the key = 5).
This approach can be coded using modular arithmetic, where: each letter of the plaintext = (position of character in ciphertext + key)%26.

As the shift remains constant throughout, the Caesar Cipher is a type of monoalphabetic substitution. 

### Playfair Cipher

The Playfair cipher is a digraph substitution cipher, where pairs of alphabets (digraphs) are encrypted at a time. A 5x5 keysquare is used, with one letter of the alphabet (in this case, 'J') omitted. The unique letters of the keyword are entered into the table, followed by the remaining letters of the alphabet in order. 

During decryption, we group the letters of the ciphertext into pairs. In case the last letter is a singleton, it is paired with 'X'. The rules for decryption are as follows:
1. If the letters lie on the same row, substitute each letter with the letter to its left(move to the rightmost letter if at the leftmost position)
2. If the letters lie on the same column, substitute each letter with the letter above it(move to the bottommost letter if at the uppermost position)
3. Else, form a square with the given letters as the two corners. Substitute the opposite letters along the rows, to obtain the plaintext pair.

### RSA Encryption

RSA(Rivest-Shamir-Adleman) encryption is an asymmetric key cryptographic technique. This means that there are 2 keys - a public key, used for encryption and a private key, used for decryption.

The public key consists of a pair of two numbers, (n,e). In this case, both n and e values have been given, so we can directly calculate the value after encryption. 

The number after encryption, say X, is calculated as X = pow(m, e) mod n ; where m is the number to be encrypted.

The private key, (p, q, d) is determined by the following: 
1. p and q are the prime factors of n. 
2. phi = (p-1)(1-1)
3. d is calculated so as to satisfy de = 1 (mod phi)

Decryption is done using the private key. The original number, m = pow(X, d) mod n. 
It is preferred to use larger primes as it increases the difficulty of decryption without a readily available private key.