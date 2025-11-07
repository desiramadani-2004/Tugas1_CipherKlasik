def affine_encrypt(plain, a, b):
    cipher = ""
    for ch in plain.upper():
        if ch.isalpha():
            cipher += chr(((a * (ord(ch) - 65) + b) % 26) + 65)
        else:
            cipher += ch
    return cipher

def affine_decrypt(cipher, a, b):
    plain = ""
    try:
        a_inv = pow(a, -1, 26)
    except ValueError:
        print("Nilai a tidak memiliki invers modulo 26, ganti dengan yang koprima.")
        return ""
    for ch in cipher.upper():
        if ch.isalpha():
            plain += chr(((a_inv * ((ord(ch) - 65 - b)) % 26) + 65))
        else:
            plain += ch
    return plain

if __name__ == "__main__":
    print("=== Affine Cipher ===")
    mode = input("Pilih mode (E = Enkripsi, D = Dekripsi): ").upper()

    a = int(input("Masukkan nilai a (harus koprima dengan 26): "))
    b = int(input("Masukkan nilai b: "))

    if mode == "E":
        teks = input("Masukkan plaintext: ")
        hasil = affine_encrypt(teks, a, b)
        print("Ciphertext:", hasil)
    elif mode == "D":
        teks = input("Masukkan ciphertext: ")
        hasil = affine_decrypt(teks, a, b)
        print("Plaintext:", hasil)
    else:
        print("Mode tidak dikenali, pilih E atau D.")
