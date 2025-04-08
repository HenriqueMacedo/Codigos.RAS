# Manipular arquivos
# Mode
# r = Leitura
# A = Append / Incrementar
# w = Escrita
# x = Criar Arquivo
# r+ = Leitura + Escrita

arquivo = open("caminho", "Mode")

#print(arquivo.readable()) - Verifica se está sendo lido
#print(arquivo.read()) - retorna todo o arquivo
#print(arquivo.readline()) - vai ler a primeira linha do arquivo
#print(arquivo.readline()) - vai ler a segunda linha do arquivo

#lista = arquivo.readlines() - Vai tronsformar as informações em uma lista
#print(lista)
#print(lista[3]) - Vai ler a terceira opção da lista / linha do arquivo

#arquivo.write(" ") - Vai realizar a função do Mode que você escolheu

arquivo.close()

# Tem como excluir arquivos, mas para isso é necessário usar uma biblioteca "os"