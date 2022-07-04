from shutil import ExecError
from pdf import *

while True:
    print("MENU: \n1 - Gerar Documento\n2 - Visualizar Documento\n3 - Imprimir Documento")
    while True:
        try:
            opc = int(input("Digite a opção desejada: "))
            break
        except ValueError:
            print("Valor inválido, tente novamente!")

    if opc == 1:
        nome = input("Nome: ")
        rg = input("RG: ")

        newPDF(nome, rg)

    elif opc == 2:
        pass

    elif opc == 3:
        pass

    else:
        print("Opção inválida, tente novamente!")

    print("")