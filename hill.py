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

def hill_decrypt(ciphertext, key_matrix):
    n = len(key_matrix)
    det = int(round(np.linalg.det(key_matrix)))
    det_inv = pow(det % 26, -1, 26)

    # cari matriks inverse modulo 26
    adjugate = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    inv_matrix = (det_inv * adjugate) % 26

    plaintext = ""
    for i in range(0, len(ciphertext), n):
        block = [ord(c) - 65 for c in ciphertext[i:i+n]]
        dec_block = np.dot(inv_matrix, block) % 26
        plaintext += ''.join(chr(int(num) + 65) for num in dec_block)
    return plaintext


if __name__ == "__main__":
    print("=== Hill Cipher ===")

    plaintext = "DESIRAMADANI"
    key_matrix = np.array([[3, 3], [2, 5]])

    print("Plaintext:", plaintext)
    print("Key Matrix:\n", key_matrix)

    cipher = hill_encrypt(plaintext, key_matrix)
    print("Ciphertext:", cipher)
    print("Hasil dekripsi:", hill_decrypt(cipher, key_matrix))

