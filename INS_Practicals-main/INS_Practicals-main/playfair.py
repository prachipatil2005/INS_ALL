import re
print ("\n#A python program to illustrate Playfair Cipher Technique.")
def generateTable(key=''):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    table = [[0] * 5 for row in range(5)]
    key = re.sub(r'[\WJ]', '', key.upper())
    for row in range(5):
        for col in range(5):
            if len(key):
                table[row][col] = key[0]
                alphabet = alphabet.replace(key[0], '')
                key = key.replace(key[0], '', -1)
            else:
                table[row][col] = alphabet[0]
                alphabet = alphabet[1:]
    return table
def Encrypt(words, key):
    table = generateTable(key)
    cipher = ''
    words = re.sub(r'[\WJ]', '', words.upper())
    text = ''    
    for i in range(0, len(words) - 1):
        text += words[i]
        if words[i] == words[i+1]:
            text += 'X'
    text += words[i+1]
    for i in range(0, len(text), 2):
        digraphs = text[i:i+2]
        a, b = digraphs[0], 'X'
        if len(digraphs) > 1:
            b = digraphs[1]
        a = position(table, a)
        b = position(table, b)
        if (a[0] == b[0]):
            cipher += table[a[0]][(a[1] + 1)] + table[b[0]][(b[1] + 1)]
        elif (a[1] == b[1]):
            cipher += table[(a[0] + 1)][a[1]] + table[(b[0] + 1)][b[1]]
        else:
            cipher += table[a[0]][b[1]] + table[b[0]][a[1]]
    return cipher;
def Decrypt(text, key):
    table = generateTable(key)
    text = re.sub(r'[\WJ]', '', text.upper())
    words = ''
    for i in range(0, len(text), 2):
        digraphs = text[i:i+2]
        if len(digraphs) != 2:
            print('cipher text is not right');
            quit(-1)
        a, b = digraphs[0], digraphs[1]
        a = position(table, a)
        b = position(table, b)
        if (a[0] == b[0]):
            words += table[a[0]][(a[1] - 1) % 5] + table[b[0]][(b[1] - 1) % 5]
        elif (a[1] == b[1]):
            words += table[(a[0] - 1) % 5][a[1]] + table[(b[0] - 1) % 5][b[1]]
        else:
            words += table[a[0]][b[1]] + table[b[0]][a[1]]
    return words
def position(table, ch):
    for row in range(5):
        for col in range(5):
            if table[row][col] == ch:
                return [row, col]
    return [row, col]
def Testing(Text,Key,E):
    Test = input("\n\nDo you want to Check what your Original Text was by Decrypting Message?\n\ni.e.(Type 'Yes'/'No')\n\n")
    if Test == 'Yes':
        Technique = 'Decrypt'
        myKey = Key
        Key = myKey
        myMessage = E
        Text = myMessage
        D = Decrypt(Text, Key)
        print ("\nYour Mode : " + Technique)
        print ("\nYour Cipher Text : " + Text)
        print ("\nKey  : " + Key)
        print ("\nDecrypted Text   : " + D)
    elif Test == 'No':
        print ("\nThank You...!\n")
    else:
        print ("\nPlease Try Again...!\n")
        Testing(Text,Key,E)
Technique = input("\n\nEnter Your Choice for Playfair Cipher Technique, \n\ni.e. Either Encrypt or Decrypt, Type ('Encrypt' or 'Decrypt').\n\n")
if Technique =='Encrypt':
    Text = input("\nEnter the Text You want to be Converted...\n\n")
    Key = input("\nEnter The Key of your Choice\n\n")
    E = Encrypt(Text,Key)
    print ("\nYour Mode: " + Technique)
    print ("\nYour Text : " + Text)
    print ("\nKey : " + Key)
    print ("\nEncrypted Text : " + E)
    Testing(Text,Key,E)
elif Technique =='Decrypt':
    Text = input("\nEnter the Playfair Cipher Text You want to be Decrypted...\n\n")
    Key = input("\nEnter the Key provided to You...\n\n")
    D = Decrypt(Text,Key)
    print ("\nYour Mode  : " + Technique)
    print ("\nYour Playfair Cipher Text    : " + Text)
    print ("\nKey  : " + Key)
    print ("\nDecrypted Text: " + D)
else :
    print ("Wrong Choice Please Try Again ... ")
