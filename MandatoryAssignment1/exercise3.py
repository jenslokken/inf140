secret = "Cybersecurity is an evolving process and is determined by the weakest link"
key = "human"
transpositon_key = "34681752"

def vigenere(text, key):
    text = text.lower().replace(" ", "") # stripping spaces, and lowering
    cipher = ""
    idx = 0
    for letter in text:
        cipher += chr(((ord(letter) - 97) + (ord(key[idx]) - 97)) % 26 + 97)
        idx = (idx + 1) % len(key)
    return cipher

print(vigenere(secret, key))


def column_transposition_cipher(text, key):
    text = text.lower()
    text = "".join([i for i in text if ord(i) >= 97 and ord(i) <= 122])
    grid = [[int(i) for i in key]]
    cipher = ""
    idx = 0
    for i in range(len(text) // len(key) + 1):
        row = []
        for j in range(len(key)):
            try:
                row.append(text[idx])
                idx += 1
            except:
                row.append(" ")
        grid.append(row)

    for r in grid:
        if r[0] == 3:
            continue
        last = 1
        for i in range(len(r)):
            cipher += r[grid[0].index(last)]
            last += 1
    return cipher 

print(column_transposition_cipher(secret, transpositon_key))



