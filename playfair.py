def generate_playfair_key(key):
    key = "".join(sorted(set(key.upper()), key=key.index))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = ""
    for c in key:
        if c in alphabet:
            matrix += c
            alphabet = alphabet.replace(c, "")
    matrix += alphabet
    return [list(matrix[i:i+5]) for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == char:
                return i, j
    return None, None

def playfair_encrypt(plaintext, key):
    plaintext = plaintext.upper().replace("J", "I")
    matrix = generate_playfair_key(key)
    result = ""
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        b = plaintext[i+1] if i+1 < len(plaintext) else "X"
        if a == b:
            b = "X"
            i += 1
        else:
            i += 2

        ax, ay = find_position(matrix, a)
        bx, by = find_position(matrix, b)

        # Enkripsi aturan Playfair
        if ax == bx:  # sama baris
            result += matrix[ax][(ay+1)%5] + matrix[bx][(by+1)%5]
        elif ay == by:  # sama kolom
            result += matrix[(ax+1)%5][ay] + matrix[(bx+1)%5][by]
        else:  # bentuk persegi
            result += matrix[ax][by] + matrix[bx][ay]
    return result

def playfair_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper().replace("J", "I")
    matrix = generate_playfair_key(key)
    result = ""
    i = 0
    while i < len(ciphertext):
        a = ciphertext[i]
        b = ciphertext[i+1] if i+1 < len(ciphertext) else "X"
        i += 2

        ax, ay = find_position(matrix, a)
        bx, by = find_position(matrix, b)

        # Dekripsi aturan Playfair
        if ax == bx:  # sama baris
            result += matrix[ax][(ay-1)%5] + matrix[bx][(by-1)%5]
        elif ay == by:  # sama kolom
            result += matrix[(ax-1)%5][ay] + matrix[(bx-1)%5][by]
        else:  # bentuk persegi
            result += matrix[ax][by] + matrix[bx][ay]
    return result

if __name__ == "__main__":
    print("=== Playfair Cipher ===")
    mode = input("Pilih mode (E = Enkripsi, D = Dekripsi): ").upper()
    key = input("Masukkan key: ")

    if mode == "E":
        plaintext = input("Masukkan plaintext: ")
        cipher = playfair_encrypt(plaintext, key)
        print("Ciphertext:", cipher)
    elif mode == "D":
        ciphertext = input("Masukkan ciphertext: ")
        plain = playfair_decrypt(ciphertext, key)
        print("Plaintext:", plain)
    else:
        print("Mode tidak valid! Pilih 'E' untuk enkripsi atau 'D' untuk dekripsi.")
