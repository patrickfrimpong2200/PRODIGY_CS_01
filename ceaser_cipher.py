def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet letter
            shift_base = 65 if char.isupper() else 97  # ASCII value for 'A' (65) or 'a' (97)
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabet characters are added unchanged
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("Caesar Cipher Encryption & Decryption")
    
    # Input the message and shift value from the user
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value (positive integer): "))
    
    # Perform encryption
    encrypted_text = encrypt(text, shift)
    print(f"Encrypted text: {encrypted_text}")
    
    # Perform decryption
    decrypted_text = decrypt(encrypted_text, shift)
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
