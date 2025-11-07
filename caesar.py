def caesar_encrypt(plain, shift):
    hasil = ""
    for ch in plain.upper():
        if ch.isalpha():
            hasil += chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            hasil += ch
    return hasil

def caesar_decrypt(cipher, shift):
    hasil = ""
    for ch in cipher.upper():
        if ch.isalpha():
            hasil += chr((ord(ch) - 65 - shift) % 26 + 65)
        else:
            hasil += ch
    return hasil

if __name__ == "__main__":
    print("=== Caesar Cipher ===")
    mode = input("Pilih mode (E = Enkripsi, D = Dekripsi): ").upper()
    shift = int(input("Masukkan nilai shift: "))

    if mode == "E":
        teks = input("Masukkan plaintext: ")
        hasil = caesar_encrypt(teks, shift)
        print("Ciphertext:", hasil)
    elif mode == "D":
        teks = input("Masukkan ciphertext: ")
        hasil = caesar_decrypt(teks, shift)
        print("Plaintext:", hasil)
    else:
        print("Mode tidak dikenali, pilih E atau D.")
