# affine.py

def affine_encrypt(plaintext, a, b):
    ciphertext = ""
    for char in plaintext.upper():
        if char.isalpha():
            ciphertext += chr(((a * (ord(char) - 65) + b) % 26) + 65)
        else:
            ciphertext += char
    return ciphertext

def affine_decrypt(ciphertext, a, b):
    plaintext = ""
    a_inv = pow(a, -1, 26)
    for char in ciphertext.upper():
        if char.isalpha():
            plaintext += chr(((a_inv * ((ord(char) - 65 - b)) % 26) + 65))
        else:
            plaintext += char
    return plaintext

if __name__ == "__main__":
    print("=== Affine Cipher ===")
    plaintext = input("Masukkan plaintext: ")
    a = int(input("Masukkan nilai a (coprime dengan 26): "))
    b = int(input("Masukkan nilai b: "))

    cipher = affine_encrypt(plaintext, a, b)
    print("Ciphertext:", cipher)
    print("Hasil dekripsi:", affine_decrypt(cipher, a, b))
