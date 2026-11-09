import requests;

SERVER = "http://mustard.stt.rnl.tecnico.ulisboa.pt";

PORT = 25054;

#O link vai armazenar junto a string do SERVER + PORTA
link = f"{SERVER}:{PORT}"; # f informa que vamos preencher as chaves com o que estiver dentro dela

# Create a session to persist the cookies between the requests
s = requests.Session();

#Access the first link to set the user cookie

r = s.get(f"{link}/hello"); #Accessing the link on the tab /hello and storing it on the r variable




#loop de requests

while 1 :

    r_more_count = s.get(f"{link}/more");

    # Extração dos valores a cada refresh

    #Atribuimos todo o texto da página a variável texto
    texto = r_more_count.text;

    # Chamamos a função split que vai dividir o texto e armazenar no array partes, onde cada divisão é um elemento do array
    partes = texto.split("<br>");

    texto_target = partes[1]; # Em partes[1] temos "Your target is: 71"

    texto_target_dividido = texto_target.split(":"); #Vai separar o "Your target is: 71" onde tivermos o :

    numero_alvo = texto_target_dividido[1] #Pegamos o número que está na posição 1 do array

    alvo = int(numero_alvo); #Passamos de uma string para um int



    texto_target_atual = partes[2];

    texto_target_atual_dividido = texto_target_atual.split(":");

    numero_atual = texto_target_atual_dividido[1];

    atual = int(numero_atual);

    if atual == alvo:
        r_finish = s.get(f"{link}/finish")
        print(r_finish.text)
        break





