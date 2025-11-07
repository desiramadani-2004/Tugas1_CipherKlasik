import numpy as np

def mod_inverse(a, m):
    a = a % m
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def hill_encrypt(plain, key):
    plain = plain.upper().replace(" ", "")
    n = len(key)
    while len(plain) % n != 0:
        plain += 'X'
    cipher = ""
    for i in range(0, len(plain), n):
        block = [ord(x) - 65 for x in plain[i:i+n]]
        enc = np.dot(key, block) % 26
        for num in enc:
            cipher += chr(int(num) + 65)
    return cipher

def hill_decrypt(cipher, key):
    cipher = cipher.upper().replace(" ", "")
    n = len(key)
    det = int(round(np.linalg.det(key))) % 26
    det_inv = mod_inverse(det, 26)
    if det_inv is None:
        print("Kunci tidak memiliki invers mod 26!")
        return ""
    adj = np.round(det * np.linalg.inv(key)).astype(int) % 26
    inv_key = (det_inv * adj) % 26
    plain = ""
    for i in range(0, len(cipher), n):
        block = [ord(x) - 65 for x in cipher[i:i+n]]
        dec = np.dot(inv_key, block) % 26
        for num in dec:
            plain += chr(int(num) + 65)
    return plain

if __name__ == "__main__":
    print("=== Hill Cipher ===")
    mode = input("Pilih mode (E = Enkripsi, D = Dekripsi): ").upper()
    key = np.array([[3,3],[2,5]])

    if mode == "E":
        p = input("Masukkan plaintext: ")
        c = hill_encrypt(p, key)
        print("Ciphertext:", c)
    elif mode == "D":
        c = input("Masukkan ciphertext: ")
        p = hill_decrypt(c, key)
        print("Plaintext:", p)
    else:
        print("Mode salah, pilih E atau D.")
