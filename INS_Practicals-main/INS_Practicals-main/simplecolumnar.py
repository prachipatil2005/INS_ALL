def encode(key, plaintext):
    # Remove spaces and make plaintext uppercase for simplicity
    plaintext = plaintext.replace(" ", "").upper()
    
    # Padding if the text length isn't divisible by the key length
    while len(plaintext) % len(key) != 0:
        plaintext += 'X'  # Adding 'X' as padding
    
    # Split the plaintext into rows of length equal to the key
    rows = [plaintext[i:i + len(key)] for i in range(0, len(plaintext), len(key))]
    
    # Encrypt by reading columns in the order given by the key
    ciphertext = ""
    for index in key:
        col_index = int(index) - 1  # Convert key digit to 0-based index
        for row in rows:
            ciphertext += row[col_index]
    
    return ciphertext

# Input text and key
text = input("Enter text: ")
column_key = input("Enter column key (e.g., 3142 for 4 columns): ")

# Encrypt and print the result
print("Encrypted text:", encode(column_key, text))