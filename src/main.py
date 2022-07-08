import os
import datetime
from pdf import *
from utils import viewCounter, viewLog, convert2docx, log, deleteAll

while True:
    print("MENU: \n1 - Gerar Documento\n2 - Editar Documento no Word\n3 - Visualizar Documento\n4 - Exibir Logs\n5 - Apagar todos documentos salvos")
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
        if viewCounter() != 0:
            print("\n1 - Editar último documento\n2 - Editar documentos anteriores")
            try:
                opc = int(input("Opção: "))
            except Exception as e:
                print("Valor inválido.")
            
            if opc == 1:
                pdf = ("document" + str(viewCounter()) + ".pdf")
                docx = ("document" + str(viewCounter()) + ".docx")

                convert2docx(pdf, docx)
                try:
                    os.startfile(docx)
                except Exception as e:
                    print("-> Houve um problema ao abrir o documento no Word.")
                    log(e)
            
            if opc == 2:
                aux = 0
                print("")
                for i in range(viewCounter()):
                    i = str(i + 1)
                    if os.path.exists("document" + i + ".pdf"):
                        print(i + " - Documento " + i + " - " + str(datetime.datetime.fromtimestamp(os.path.getctime("document" + i + ".pdf"))))
                        aux = aux + 1
                if(aux != 0):
                    try:
                        opc = int(input("Digite o arquivo que deseja editar: "))

                        if opc <= viewCounter():
                            pdf = ("document" + str(opc) + ".pdf")
                            docx = ("document" + str(opc) + ".docx")

                            print("")
                            convert2docx(pdf, docx)
                            try:
                                os.startfile(docx)
                            except Exception as e:
                                print("-> Houve um problema ao abrir o documento no Word.")
                                log(e)
                        else:
                            print("Arquivo inexistente.")
                    except Exception as e:
                        print("Valor inválido.")
        else:
            print("Você precisa gerar um arquivo antes de poder editá-lo.")

    elif opc == 3:
        if viewCounter() != 0:
            print("\n1 - Visualizar último documento\n2 - Visualizar documentos anteriores")
            try:
                opc = int(input("Opção: "))
            except Exception as e:
                print("Opção inválida.")
            
            if opc == 1:
                pdf = ("document" + str(viewCounter()) + ".pdf")

                try:
                    os.startfile(pdf)
                except Exception as e:
                    print("-> Houve um problema ao abrir o documento.")
                    log(e)
            
            if opc == 2:   
                aux = 0
                print("")
                for i in range(viewCounter()):
                    i = str(i + 1)
                    if os.path.exists("document" + i + ".pdf"):
                        print(i + " - Documento " + i + " - " + str(datetime.datetime.fromtimestamp(os.path.getctime("document" + i + ".pdf"))))
                        aux = aux + 1
                if(aux != 0):
                    try:
                        opc = int(input("Digite o arquivo que deseja visualizar: "))

                        if opc <= viewCounter():
                            pdf = ("document" + str(opc) + ".pdf")

                            try:
                                os.startfile(pdf)
                            except Exception as e:
                                print("-> Houve um problema ao abrir o documento.")
                                log(e)
                        else:
                            print("Arquivo inexistente.")
                    except Exception as e:
                        print("Valor inválido.")
        else:
            print("Você precisa gerar um arquivo antes de poder visualizá-lo.")

    elif opc == 4:
        viewLog()

    elif opc == 5:
        opc = input("Tem certeza que deseja deletar todos os documentos? [sim/cancelar]\n")
        if opc.lower() == "sim":
            deleteAll()

    else:
        print("Opção inválida, tente novamente!")

    print("")