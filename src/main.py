import os
from pdf import *
from utils import viewLog, convert2docx, log

while True:
    print("MENU: \n1 - Gerar Documento\n2 - Editar Documento no Word\n3 - Visualizar Documento\n4 - Salvar Documento\n5 - Exibir Logs")
    while True:
        try:
            opc = int(input("Digite a opção desejada: "))
            break
        except ValueError:
            print("Valor inválido, tente novamente!")

    if opc == 1:
        print("\n-> Dados do contrato")
        nome = input("Nome Completo: ")
        rg = input("RG: ")
        emissor = input("Emissor RG: ")
        cpf = input("CPF: ")
        dataIn = input("Data de Entrada: ")
        dataOut = input("Data de Saída (se saída for no mesmo dia digite 0): ")
        evento = input("Nome do Evento: ")
        valor = input("Valor do Aluguel: ")
        dataAss = input("Data para Assinatura: ")

        newPDF(nome, rg, emissor, cpf, dataIn, dataOut, evento, valor, dataAss)

    elif opc == 2:
        print("\n")
        convert2docx("document.pdf", "document.docx")
        try:
            os.startfile("document.docx")
        except Exception as e:
            print("-> Houve um problema ao abrir o documento no Word.")
            log(e)

    elif opc == 3:
        try:
            os.startfile("document.pdf")
        except Exception as e:
            print("-> Houve um problema ao abrir o documento.")
            log(e)

    elif opc == 4:
        print("\n")
        convert2docx("document.pdf", "document.docx")
        filename = os.path.join(os.environ["HOMEDRIVE"], os.environ["HOMEPATH"], "Desktop", "test.csv")

    elif opc == 5:
        viewLog()

    else:
        print("Opção inválida, tente novamente!")

    print("")