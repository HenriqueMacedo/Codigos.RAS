#Criar uma lista de números e imprimir apenas os números pares

#Função para separar os números pares
def separar(lista):
    lista_pares = list([])
    for i in range(len(lista)):
        if((lista[i] % 2) == 0):
            lista_pares.append(lista[i])
    return lista_pares

#Loop para perguntar se o usuário quer continuar o programa
a = True
while (a):
    lista = []

#Definição dos números da lista
    while(True):
 
 #Uso do try-except para não deixar o usuário digitar uma letra
        try:
            num = int(input('Insira um número (digite 0 para sair): '))
            if(num == 0 ):
                break 
        except ValueError:
            print('Você não digitou um número. Tente novamente!')
        lista.append(num)

 #Imprimir resultado
    resultado = separar(lista)
    print(resultado)

    resposta = input('Você quer continuar(Sim ou Não)? ')
    if resposta.lower() != 'sim':
     break