def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext.upper():
        if char.isalpha():
            ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

if __name__ == "__main__":
    print("=== Caesar Cipher ===")

    plaintext = "DESI RAMADANI"
    shift = 2

    print("Plaintext:", plaintext)
    print("Shift:", shift)

    cipher = caesar_encrypt(plaintext, shift)
    print("Ciphertext:", cipher)
    print("Hasil dekripsi:", caesar_decrypt(cipher, shift))
