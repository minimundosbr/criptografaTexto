#Var para guardar texto; Var para criptografar, descriptografar; Limitar a 128 caracteres; 
#Preciso mandar na tela do usuario = Insira a mensagem que deseja criptografar;
#Preciso salvar a mensagem do usuario em uma variavel;

def cifraCesar(msgCriptografar, chave):
    textoCifrado = "" #Texto que iremos retornar no final.
    for char in msgCriptografar:
        if 'a' <= char <= 'z':
                      #ord = Transforma letra em numero tabela ASCII    
            posicao = ord(char) - ord('a') #Pega valor da tabela ASCII de 'char' [definiremos] e subtrai por ascII de 'a';
            novaPosicao = (posicao + chave) % 26 # Soma valor da funcao "posicao" com a chave que o usuario desejar criptografar e realizar a divisao por 26 (qtdNumero alfabeto), e obter o resto
                       #chr = Transforma o numero da tabela ASCII em letra.
            novoChar = chr(novaPosicao + ord('a')) #soma o valor gerado com o valor da tabela ASCII de 'a' para retornar a nova letra.
            textoCifrado += novoChar #Retorna a letra criptografada para o textoCifrado.
        elif 'A' <= char <=('Z'):
            posicao = ord(char) - ord('A')
            novaPosicao = (posicao + chave) % 26
            novoChar = chr(novaPosicao + ord('A'))
            textoCifrado += novoChar
        else:
            #Aqui nao mexeremos em informacoes que nao sao caracteres.
            textoCifrado += char 
    return textoCifrado

msgCriptografada = ""
msgCriptografar = "" #Inicializacao da variavel
chave = 0

while True: #enquanto verdade, faca:
    msgCriptografar = input("Insira a mensagem que deseja criptografar: ") #salva a mensagem
    chave = int(input("Insira a chave para a cifra: ")) #salva o numero
    if len(msgCriptografar) <= 128: #valida se a mensagem é menor que 128 caracteres
        print("Sua mensagem foi: " , msgCriptografar) 
        msgCriptografada = cifraCesar(msgCriptografar, chave)
        print(f"Sua mensagem codificada: {msgCriptografada}")
        break # força a parada do código
    print("Sua mensagem foi muito longa, abrevie-a!") #Retorno para o erro.
