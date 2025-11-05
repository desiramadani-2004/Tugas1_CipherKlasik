# hill.py
import numpy as np

def hill_encrypt(plaintext, key_matrix):
    plaintext = plaintext.upper().replace(" ", "")
    n = len(key_matrix)
    while len(plaintext) % n != 0:
        plaintext += 'X'

    ciphertext = ""
    for i in range(0, len(plaintext), n):
        block = [ord(c) - 65 for c in plaintext[i:i+n]]
        enc_block = np.dot(key_matrix, block) % 26
        ciphertext += ''.join(chr(num + 65) for num in enc_block)
    return ciphertext

if __name__ == "__main__":
    print("=== Hill Cipher ===")
    plaintext = input("Masukkan plaintext: ").upper()
    print("Gunakan matriks 2x2: ")
    key_matrix = np.array([[3, 3], [2, 5]])

    cipher = hill_encrypt(plaintext, key_matrix)
    print("Ciphertext:", cipher)
