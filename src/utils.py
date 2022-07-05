import os
from pdf2docx import parse
from typing import Tuple
from datetime import datetime
from num2words import num2words

def number2words(number_p):
    if number_p.find(',')!=-1:
        number_p = number_p.split(',')
        number_p1 = int(number_p[0].replace('.',''))
        number_p2 = int(number_p[1])
    else:
        number_p1 = int(number_p.replace('.',''))
        number_p2 = 0
        
    if number_p1 == 1:
        aux1 = ' real'
    else:
        aux1 = ' reais'
        
    if number_p2 == 1:
        aux2 = ' centavo'
    else:
        aux2 = ' centavos'
        
    text1 = ''
    if number_p1 > 0:
        text1 = num2words(number_p1,lang='pt_BR') + str(aux1)
    else:
        text1 = ''
    
    if number_p2 > 0:
        text2 = num2words(number_p2,lang='pt_BR') + str(aux2) 
    else: 
        text2 = ''
    
    if (number_p1 > 0 and number_p2 > 0):
        result = text1 + ' e ' + text2
    else:
        result = text1 + text2

    return result

def convert2docx(input_file: str, output_file: str, pages: Tuple = None):
    if pages:
        pages = [int(i) for i in list(pages) if i.isnumeric()]
    parse(pdf_file=input_file,
                   docx_with_path=output_file, pages=pages)
    summary = {
        "File": input_file, "Pages": str(pages), "Output File": output_file
    }

    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    os.startfile("document.docx")

def log(error) -> None:
    data = open("logger.log", "a")
    time = datetime.now()
    data.write(str(time))
    data.write(" -> ")
    data.write(str(error))
    data.write("\n")
    data.close()

def viewLog() -> None:
    print("\nLogs:")
    if os.path.exists('./logger.log'):
        data = open("logger.log", "r")
        log = data.readlines()
        for i in range(len(log)):
            print(log[i].strip('\n'))
        data.close()
    else:
        print("Empty Log")