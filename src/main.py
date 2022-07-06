import os
from pdf import *
from utils import viewLog, convert2docx, log

while True:
    print("MENU: \n1 - Gerar Documento\n2 - Editar Documento no Word\n3 - Visualizar Documento\n4 - Exibir Logs")
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
        if os.path.exists('./document.pdf'):
            convert2docx("document.pdf", "document.docx")
            try:
                os.startfile("document.docx")
            except Exception as e:
                print("-> Houve um problema ao abrir o documento no Word.")
                log(e)
        else:
            print("-> Você deve gerar um documento para poder editá-lo.")

    elif opc == 3:
        if os.path.exists('./document.pdf'):
            try:
                os.startfile("document.pdf")
            except Exception as e:
                print("-> Houve um problema ao abrir o documento.")
                log(e)
        else:
            print("-> Você deve gerar um documento para poder visualiza-lo.")

    elif opc == 4:
        viewLog()

    else:
        print("Opção inválida, tente novamente!")

    print("")