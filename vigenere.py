# vigenere.py

def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    key_index = 0
    for char in plaintext.upper():
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
            key_index += 1
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    key_index = 0
    for char in ciphertext.upper():
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
            key_index += 1
        else:
            plaintext += char
    return plaintext

if __name__ == "__main__":
    print("=== Vigenere Cipher ===")
    plaintext = input("Masukkan plaintext: ")
    key = input("Masukkan key: ")

    cipher = vigenere_encrypt(plaintext, key)
    print("Ciphertext:", cipher)
    print("Hasil dekripsi:", vigenere_decrypt(cipher, key))