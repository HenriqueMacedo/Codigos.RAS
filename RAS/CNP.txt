#Loop para saber até onde o usuário quer realizar o código
a=True
while (a):
    #Entrada da informação
    numero = int(input('Digite um número: '))
    div = 0
    resp = 0
    #Início do loop
    for p in range(1, numero + 1):
    #Identificando se o nuúmero será divisível apenas por 1 e por ele mesmo
        if numero % p == 0:
    #Identificar a quantidade de divisíveis
            div += 1
        print('{} '.format(p), end=' ')

    #Saída da informação
    print('\nO número {} foi divisível {} vezes.'.format(numero, div))
    if div == 2:
        print('E por isso ele é um número primo!')
    else:
        print('E por isso ele não é um número primo!')
    resp = input('Você quer continuar(Sim ou Não)? ')

    if resp.lower() != 'sim':
        break
