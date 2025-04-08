# Escrever um programa que leia um arquivo .txt e exiba seu conteúdo.

while(True):
# Selecionando o arquivo que será lido
    selec_arq = input("Coloque o caminho do arquivo que você deseja ler (lembre de colocar o .txt no final): ")

# Abrindo o arquivo
    try:
        arquivo = open(selec_arq, "r")
        print("\nConteúdo do arquivo:")
        print(arquivo.read())
        if arquivo.readable() == True:
            print("\nO arquivo selecionado foi lido com sucesso!")
        arquivo.close()
    except FileNotFoundError:
        print("\nO arquivo não foi encontrado. Veja se selecionou corretamento o arquivo!")
 
    Op = str(input("Deseja fazer a leitura de outro arquivo (digite 'sair' para encerrar)? "))
    if Op.lower() == 'não':
        print("Programa finalizado.")
        break
    print("-="*30)