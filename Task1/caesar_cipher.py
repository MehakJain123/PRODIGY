def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# User input
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

if choice == 'e':
    encrypted_msg = encrypt(message, shift)
    print("Encrypted message:", encrypted_msg)
elif choice == 'd':
    decrypted_msg = decrypt(message, shift)
    print("Decrypted message:", decrypted_msg)
else:
    print("Invalid choice!")
