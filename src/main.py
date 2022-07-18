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
            print("-> Valor inválido, tente novamente!\n")

    if opc == 1:
        print("\n-> Dados do contrato")
        nome = input("Nome Completo: ")
        rg = input("RG: ")
        emissor = input("Emissor RG: ")
        cpf = input("CPF: ")
        dataIn = input("Data de Entrada: ")
        dataOut = input("Data de Saída (se saída for no mesmo dia digite 0): ")
        dataAss = input("Data para Assinatura: ")
        evento = input("Nome do Evento: ")
        valor = input("Valor do Aluguel: ")
        while True:
            aux = int(input("\n1 - À vista\n2 - A prazo\nPagamento: "))
            if aux == 1 or aux == 2:
                break
            else:
                print("-> Valor inválido.")

        newPDF(nome, rg, emissor, cpf, dataIn, dataOut, dataAss, evento, valor, aux)

    elif opc == 2:
        if viewCounter() != 0:
            print("\n1 - Editar último documento\n2 - Editar documentos anteriores")
            try:
                opc = int(input("Opção: "))
            except ValueError:
                print("-> Valor inválido.")
            
            if opc == 1:
                for i in range(len(os.listdir())):
                    aux = os.listdir()[i]

                    if aux[:4] == str(viewCounter()) and aux[-3:] == "pdf":
                        docx = (aux[:-4] + ".docx")
                        convert2docx(aux, docx)
                        try:
                            os.startfile(docx)
                        except Exception as e:
                            print("-> Houve um problema ao abrir o documento no Word.")
                            log(e)
            
            elif opc == 2:
                print("")
                for i in range(len(os.listdir())):
                    aux = os.listdir()[i]
                    auy = (aux[-3:])
                    if auy == "pdf":
                        print(aux[:-4] + " - " +
                                str((datetime.datetime.fromtimestamp(os.path.getctime(os.listdir()[i])).strftime('%d/%m/%Y %H:%M'))))

                if(aux != 0):
                    opc = input("Digite o número do arquivo que deseja editar: ")
                    
                    docx = None
                    for i in range(len(os.listdir())):
                        aux = os.listdir()[i]
                        if opc == aux[:4] and aux[-3:] == "pdf":
                            docx = (aux[:-4] + ".docx")

                            print("")
                            convert2docx(aux, docx)
                            try:
                                os.startfile(docx)
                            except Exception as e:
                                print("-> Houve um problema ao abrir o documento no Word.")
                                log(e)
                            break

                    if docx == None:
                        print("Arquivo inexistente.")
            else:
                print("Opção Inválida.")
        else:
            print("Você precisa gerar um arquivo antes de poder editá-lo.")

    elif opc == 3:
        if viewCounter() != 0:
            print("\n1 - Visualizar último documento\n2 - Visualizar documentos anteriores")
            try:
                opc = int(input("Opção: "))
            except ValueError:
                print("Opção inválida.")
            
            if opc == 1:
                for i in range(len(os.listdir())):
                    aux = os.listdir()[i]

                    if aux[:4] == str(viewCounter()) and aux[-3:] == "pdf":
                        try:
                            os.startfile(aux)
                        except Exception as e:
                            print("-> Houve um problema ao abrir o documento.")
                            log(e)
            
            elif opc == 2:
                print("")
                for i in range(len(os.listdir())):
                    aux = os.listdir()[i]
                    auy = (aux[-3:])
                    if auy == "pdf":
                        print(aux[:-4] + " - " +
                                str((datetime.datetime.fromtimestamp(os.path.getctime(os.listdir()[i])).strftime('%d/%m/%Y %H:%M'))))
                        
                if(aux != 0):
                    opc = input("Digite o número do arquivo que deseja visualizar: ")
                    
                    cont = 0
                    for i in range(len(os.listdir())):
                        aux = os.listdir()[i]
                        if opc == aux[:4] and aux[-3:] == "pdf":
                            cont = 1

                            try:
                                os.startfile(aux)
                            except Exception as e:
                                print("-> Houve um problema ao abrir o documento.")
                                log(e)
                            break
                    if cont != 1:
                        print("Arquivo inexistente.")
            else:
                print("Opção inválida.")
        else:
            print("Você precisa gerar um arquivo antes de poder visualizá-lo.")

    elif opc == 4:
        viewLog()

    elif opc == 5:
        opc = input("Tem certeza que deseja deletar todos os documentos?\n[sim/cancelar]: ")
        if opc.lower() == "sim":
            deleteAll()
        else:
            print("-> Cancelado.")

    else:
        print("Opção inválida, tente novamente!")

    print("")