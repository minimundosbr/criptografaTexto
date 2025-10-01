# --- operações em GF(2^8) ---
def gf_mul(a, b):
    res = 0
    for _ in range(8):
        if b & 1:
            res ^= a
        carry = a & 0x80
        a = (a << 1) & 0xFF
        if carry:
            a ^= 0x1B 
        b >>= 1
    return res

def gf_pow(a, e):
    res = 1
    base = a
    while e > 0:
        if e & 1:
            res = gf_mul(res, base)
        base = gf_mul(base, base)
        e >>= 1
    return res

def gf_inv(a):
    return 0 if a == 0 else gf_pow(a, 254)

# --- transformação afim usada no AES ---
def affine_transform(x):
    c = 0x63
    out = 0
    # bits: LSB = bit 0
    for i in range(8):
        # XOR de b_i, b_{i+4}, b_{i+5}, b_{i+6}, b_{i+7}, e c_i
        bit = ((x >> i) & 1) ^ ((x >> ((i+4) % 8)) & 1) ^ ((x >> ((i+5) % 8)) & 1) \
              ^ ((x >> ((i+6) % 8)) & 1) ^ ((x >> ((i+7) % 8)) & 1) ^ ((c >> i) & 1)
        out |= (bit << i)
    return out

# --- gerar S-box e inv S-box ---
sbox = [0] * 256
inv_sbox = [0] * 256
for a in range(256):
    inv = gf_inv(a)
    s = affine_transform(inv)
    sbox[a] = s
    inv_sbox[s] = a

# teste rápido (exemplo clássico)
print(hex(sbox[0x53]))  # deve imprimir 0xed
print(hex(sbox[0x00]))  # deve imprimir 0x63
