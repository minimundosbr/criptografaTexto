def addRoundKey(state, round_key):
    for i in range (4):
        for j in range(4):
            state[i][j] ^= round_key[i][j]

def invAddRoundKey(state, round_key):
    addRoundKey(state, round_key)

    
