def vigenere_encrypt(plain, key):
    cipher = ""
    key = key.upper()
    idx = 0
    for ch in plain.upper():
        if ch.isalpha():
            shift = ord(key[idx % len(key)]) - 65
            cipher += chr((ord(ch) - 65 + shift) % 26 + 65)
            idx += 1
        else:
            cipher += ch
    return cipher

def vigenere_decrypt(cipher, key):
    plain = ""
    key = key.upper()
    idx = 0
    for ch in cipher.upper():
        if ch.isalpha():
            shift = ord(key[idx % len(key)]) - 65
            plain += chr((ord(ch) - 65 - shift) % 26 + 65)
            idx += 1
        else:
            plain += ch
    return plain

if __name__ == "__main__":
    print("=== Vigenere Cipher ===")
    mode = input("Pilih mode (E = Enkripsi, D = Dekripsi): ").upper()
    key = input("Masukkan key: ")

    if mode == "E":
        teks = input("Masukkan plaintext: ")
        hasil = vigenere_encrypt(teks, key)
        print("Ciphertext:", hasil)
    elif mode == "D":
        teks = input("Masukkan ciphertext: ")
        hasil = vigenere_decrypt(teks, key)
        print("Plaintext:", hasil)
    else:
        print("Mode tidak dikenali, pilih E atau D.")
