# playfair.py

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
        if ax == bx:
            result += matrix[ax][(ay+1)%5] + matrix[bx][(by+1)%5]
        elif ay == by:
            result += matrix[(ax+1)%5][ay] + matrix[(bx+1)%5][by]
        else:
            result += matrix[ax][by] + matrix[bx][ay]
    return result

if __name__ == "__main__":
    print("=== Playfair Cipher ===")
    plaintext = input("Masukkan plaintext: ")
    key = input("Masukkan key: ")

    cipher = playfair_encrypt(plaintext, key)
    print("Ciphertext:", cipher)
