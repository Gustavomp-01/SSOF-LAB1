from pwn import * #De pwn importe tudo

HOST = "mustard.stt.rnl.tecnico.ulisboa.pt"

PORT = 25055

conn = remote(HOST,PORT) #Mesma coisa do link para python_requests

primeiro_connect = conn.recvuntil(b"FINISH)?\n") #Vai armazenar na variável todos os bytes até finish)?

texto_inicial = primeiro_connect.decode() # Vai transformar esses bytes em texto

linhas = texto_inicial.split("\n")

linha_alvo = linhas[1]

linha_alvo_split = linha_alvo.split("to")

numero_alvo = linha_alvo_split[1]

numero_alvo = numero_alvo.strip(" .") # Remove os espaços e pontos

alvo = int(numero_alvo) # Agora já temos o número alvo

print(alvo)

while 1:
    conn.sendline(b"MORE") #Função sendline para enviar inputs o b é para informar que enviamos em bytes e não string

    bloco_texto = conn.recvuntil(b"FINISH)?\n")

    #Passamos a linha para string
    texto_resposta = bloco_texto.decode()

    array_linhas = texto_resposta.split("\n")

    linha_desejada = array_linhas[2]

    linha_desejada_split= linha_desejada.split(" =")

    numero_atual = linha_desejada_split[1]

    numero_atual = numero_atual.strip(" .")

    atual = int(numero_atual)

    if atual == alvo:
        conn.sendline(b"FINISH") 
        bloco_texto_resposta_FINISH = conn.recvall()
        texto_resposta_FINISH = bloco_texto_resposta_FINISH.decode()
        print(texto_resposta_FINISH)
        break

    


    

    


    






