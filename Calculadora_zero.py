# Implementar um código que tente dividir dois números inseridos pelo usuário 
# E trate divisões por zero

print("Início do programa!\n")
while(True):
    qct = 0
    
    try:
        N1 = float(input("Digite o dividendo: "))
        N2 = float(input("Digite o divisor: "))
        qct = N1 / N2
    except ZeroDivisionError:
        print("Não foi possível definir a divisão por zero.")
    except ValueError:
        print("Você não digitou um número. Tente novamente.")
        continue
    else:
        print(f"O resultado da divisão é {qct: .2f}")
    
    op = input("Quer realizar o programa novamente (digite 'sair' para encerrar)? ")
    if op.lower() == 'sair':
        print("Programa encerrado!")
        break
    print("-="*30)
