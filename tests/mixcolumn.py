def xtime(a):
    """Multiplica um byte por 2 em GF(2^8)"""
    return((a << 1) ^ 0x1B) & 0xFF if a & 0x80 else (a << 1)

def mixSingleColumn(col):
    """Col recebe [b0, b1, ...] e retorna [c0, c1, ...]
    fazendo com que fique mais proximo do AES real."""

    b0, b1, b2, b3 = col

    c0 = xtime(b0) ^ (xtime(b1)^ b1) ^ b2 ^ b3
    c1 = b0 ^ xtime(b1) ^ (xtime(b2) ^ b2) ^ b3
    c2 = b0 ^ b1 ^ xtime(b2) ^ (xtime(b3) ^ b3)
    c3 = (xtime(b0) ^ b0) ^ b1 ^ b2 ^ xtime(b3)
    return [c0, c1, c2, c3]

def mixColumns(state):
    for c in range(4):
        col = [state[r][c] for r in range(4)]
        col = mixSingleColumn(col)
        for r in range(4):
            state[r][c] = col[r]


#Teste CLI

if __name__ == "__main__":
    state= [
        [0x87, 0xF2, 0x4D, 0x97],
        [0x6E, 0x4C, 0x90, 0xEC],
        [0x46, 0xE7, 0x4A, 0xC3],
        [0xA6, 0x8C, 0xD8, 0x95]
        ]
    print("Matriz original: ")
    for linha in state:
        print([hex(x) for x in linha])

        mixColumns(state)

        print("\nMatriz apos MixColumns:")
        for linha in state:
            print([hex(x) for x in linha])