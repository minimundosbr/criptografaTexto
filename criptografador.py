def textToChar(txt):
    #Conversion of char to ASCII (Here we are taking char by char and saving the respective ASCII code).
    bytesList = [ord(char) for char in txt]

    #Applying padding untill it fill up 16 bytes.
    while len(bytesList) % 16 != 0: #PT-BR: Enquanto o valor da lista de bytes dividida por 16 for diferente de 0, preencha com o padding.
        bytesList.append(16 - (len(bytesList) % 16)) #Realizando o preenchimento do padding 

    #Creating a matrix 4x4 (filled up col by col)
    matrix = [[0] * 4 for _ in range(4)]
    for i in range(16):
        row = i % 4
        column = i // 4
        matrix[row][column] = bytesList[i]

    return matrix


def charToText(matrix):
    #Rebuilding the bytes list (col by col again)
    bytesList = []
    for column in range(4):
        for row in range(4):
            bytesList.append(matrix[row][column])
    
    #Removing the padding
    padding = bytesList[-1]
    if padding <16:
        bytesList = bytesList[:-padding]

    #Conversion of ASCII to Char, generating our text again
    txt = "".join(chr(b) for b in bytesList)

    return txt

#Piece of code to test the code.
message = input("Digite o texto a ser convertido: ")
matrix = textToChar(message)
print("Matrix generated: ")
for row in matrix:
    print(row)

txt = charToText(matrix)
print("\nText reconstructed: ", txt)