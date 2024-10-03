# A python program to illustrate Vernam Cipher Technique.
print("#A python program to illustrate Vernam Cipher Technique.")

def Encrypt(message, key):
    message = str(message)
    m = message.upper()  # Convert to upper case
    encrypt = ""  
    for i in range(len(m)):
        letter = ord(m[i]) - 65  # Letter now ranges from 0-25
        s = key.upper()           # Ensure key is uppercase
        l = ord(s[i]) - 65
        letter = (letter + l) % 26  # Add the key, wrap around with modulo
        encrypt += chr(letter + 65)  # Convert back to character
    return encrypt

def Decrypt(message, key):
    message = str(message)
    m = message.upper()  # Convert to upper case
    decrypt = "" 
    for i in range(len(m)):
        le = ord(m[i]) - 65  # Letter now ranges from 0-25
        s = key.upper()       # Ensure key is uppercase
        letter = ord(s[i]) - 65
        le = (le - letter + 26) % 26  # Subtract key, wrap around with modulo
        decrypt += chr(le + 65)  # Convert back to character
    return decrypt

def Testing(Text, Key, E):
    Test = input("Do you want to Check what your Original Text was by Decrypting Message?\nType 'Yes' or 'No':\n")
    if Test == 'Yes':
        Technique = 'Decrypt'
        D = Decrypt(E, Key)
        print("Your Mode        : " + Technique)
        print("Your Cipher Text : " + E)
        print("Key              : " + Key)
        print("Decrypted Text   : " + D)
    elif Test == 'No':
        print("Thank You...!\n")
    else:
        print("Please Try Again...!\n")     

Technique = input("Enter Your Choice for Vernam Cipher Technique ('Encrypt' or 'Decrypt'):\n")
if Technique == 'Encrypt':
    Text = input("Enter the Text You want to be Converted:\n")
    Key = input("Enter The Key of your Choice:\n")
    E = Encrypt(Text, Key)
    print("Your Mode      : " + Technique)
    print("Your Text      : " + Text)
    print("Key            : " + Key)
    print("Encrypted Text : " + E)
    Testing(Text, Key, E)
elif Technique == 'Decrypt':
    Text = input("Enter the Vernam Cipher Text You want to be Decrypted:\n")
    Key = input("Enter the Key provided to You:\n")
    D = Decrypt(Text, Key)
    print("Your Mode                  : " + Technique)
    print("Your Vernam Cipher Text    : " + Text)
    print("Key                        : " + Key)
    print("Decrypted Text             : " + D) 
else:
    print("Wrong Choice Please Try Again ... ")
