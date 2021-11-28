import zipfile

#Base64 
def base64(ciphertext):
    b64set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/" #character set

    binary = ""

    for i in ciphertext:
        if i in b64set:
            index = b64set.index(i) #obtain position in character set
            binary += (bin(index).lstrip("0b")).zfill(6) #append the 6-bit binary representation of character

    decoded = ""
    for i in range(0, len(binary), 8):
        group = binary[i:(i+8)]  #group 8 bits at a time
        decoded += chr(int(group, 2)) #append character corresponding to the ASCII value
        i += 8
    
    return decoded

#Caesar Cipher, key = 4
def caesar(ciphertext):
    key = 4
    ans = ""
    for i in ciphertext:
        if i!=' ' and i!="\n":
            ch = chr(65 + (ord(i)-65+key)%26) #right-shift by 4 positions
            ans += ch
        else:
            ans += ch
    
    return ans

#Playfair Cipher, key = "ABCDE"
def getIndex(key, c1, c2):
    loc = [0]*4
    for i in range(0, 5):
        for j in range(0, 5):
            if key[i][j] == c1:
                loc[0] = i
                loc[1] = j
            if key[i][j] == c2:
                loc[2] = i
                loc[3] = j
    return loc

def find(key, index):
    pair = ""
    i1, j1, i2, j2 = 0,0,0,0
    if index[0] == index[2]: #same row
        i1, i2 = index[0], index[0]
        j1 = (index[1] - 1)%5
        j2 = (index[3] - 1)%5
    elif index[1] == index[3]: #same column
        j1, j2 = index[1], index[1]
        i1 = (index[0] - 1)%5
        i2 = (index[2] - 1)%5
    else: #different row and col
        i1 = index[0]
        j1 = index[3]
        i2 = index[2]
        j2 = index[1]
    pair += key[i1][j1] + key[i2][j2]

    return pair

def playfair(ciphertext):
    ch = 'A'
    key = [[None for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if ch=='J':
                ch = chr(ord(ch)+1)
            key[i][j] = ch
            ch = chr(ord(ch)+1)

    index = [0]*4
    ans = ""
    for i in range(0, len(ciphertext), 2):
        if i+1 < len(ciphertext):
            index = getIndex(key, ciphertext[i], ciphertext[i+1])
        else:
            index = getIndex(key, ciphertext[i], 'X')
        ans += find(key, index)

    return ans

#RSA Encryption
def rsa(text, n, e):
    encrypt = pow(text, e)%n
    return encrypt

#Caesar Cipher, key = 5
def caesar5(text):
    ans = ""
    key = 5
    for i in text:
        if i>="A" and i<="Z":
            ans += chr(65+ (ord(i)-65 - key)%26) #right-shift alphabet by 5 positions
        else:
            ans += i #directly append the spaces
    return ans
    
def main():
    print("Enter ciphertext: ")
    s = input()
    x1 = base64(s)

    startIndex = x1.find(":") #index after which ciphertext begins
    x2 = caesar(x1[startIndex+2:])

    startIndex = x2.find("J") #index after which ciphertext begins
    x3 = playfair(x2[startIndex+2:])

    text = 243 #values obtained on reading message.
    n = 2419
    e = 11
    password = rsa(text, n, e)
 
    line = ""
    #extract zip file contents, read file
    with zipfile.ZipFile(r"C:\Users\KavyaBhat\Downloads\dontopen.zip","r") as zip_ref:
        zip_ref.extractall(r"C:\Users\KavyaBhat\Downloads", pwd=bytes(str(password), encoding='utf-8'))
        line += zip_ref.read("dontsee.txt", pwd=bytes(str(password), encoding = 'utf-8')).decode('utf-8')

    decode = caesar5(line)
    print("\n" + decode)

if __name__ == "__main__":
    main()