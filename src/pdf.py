from fpdf import FPDF
from utils import number2words, counter, log

def newPDF(nome, rg, emissor, cpf, dataIn, dataOut, dataAss, evento, valor, pag) -> None:
    try:
        pdf = FPDF(format = 'A4')  
        pdf.add_page()

        pdf.set_top_margin(15)
        pdf.set_font("Arial", style = 'B', size = 17)

        pdf.cell(200, 10, txt = "CONTRATO DE LOCAÇÃO POR INSTRUMENTO PARTICULAR",
                ln = 1, align = 'C')
        pdf.ln(h = '')

        pdf.set_font("Arial", size = 15.1)

        pdf.write(5, '                                       ')
        text = ("\t\t\t\t\t\t\t\t\t\tContrato de locação com condição que fazem de um lado, o LOCADOR(A): SÍTIO MANAJU em Ibaiti-PR, representada pela proprietária: JULIANE APARECIDA PEDRO E NUNES, portador(a) do RG: 4604817-2 - " +
                    "SSP-PR e do CPF: 005846289-94 e de outro lado, o LOCATÁRIO(A): " + nome + ", RG: " + rg + " " + emissor + ", CPF: " + cpf + " na conformidade com as condições abaixo pactuadas.")
        pdf.multi_cell(0, 6, txt = text, border = 0, align = "J", fill = False)
        pdf.ln(h = '')

        if dataOut == "0":
            text = ("\t\t\t\t\t\t\t\t\tCLAUSULA PRIMEIRA: O(A)LOCADOR(A), loca ao(à) LOCATÁRIO(A), através do regime jurídico de locação, devidamente limpo as dependências da sede: CASA COM CHURRASQUEIRA, PISCINA, VESTIÁRIO E QUADRA DE " + 
                    "AREIA SEM ILUMINAÇÃO, para realização no dia " + dataIn + ", o evento denominado \"" + evento + "\".") 
        else:
            text = ("\t\t\t\t\t\t\t\t\tCLAUSULA PRIMEIRA: O(A)LOCADOR(A), loca ao(à) LOCATÁRIO(A), através do regime jurídico de locação, devidamente limpo as dependências da sede: CASA COM CHURRASQUEIRA, PISCINA, VESTIÁRIO E QUADRA DE " + 
                    "AREIA SEM ILUMINAÇÃO, para realização do dia " + dataIn + " até o dia " + dataOut + ", o evento denominado \"" + evento + "\".")
        pdf.multi_cell(0, 6, txt = text, align = "J", fill = False)
        pdf.ln(h = '')

        text = ("\t\t\t\t\t\t\t\t\tParágrafo I: O(A) LOCATÁRIO(A) fica ciente, da proibição de utilização de bandas musicais, sendo autorizado somente o \"SOM MECÂNICO\" ou \"SOM ACÚSTICO\".")
        pdf.multi_cell(0, 6, txt = text, border = 0, align = "J", fill = False)
        pdf.ln(h = '')

        text = ("\t\t\t\t\t\t\t\t\tParágrafo II: O(A)LOCATÁRIO(A) fica ciente, que é terminantemente proibido, a utilização do local afim de realização de baile, open bar e similares, com uso de portaria e cobrança de ingressos e utilização de pulseiras.")
        pdf.multi_cell(0, 6, txt = text, border = 0, align = "J", fill = False)
        pdf.ln(h = '')

        if dataOut == "0":
            text = ("\t\t\t\t\t\t\t\t\tParágrafo III: O(A) LOCATÁRIO(A) fica ciente, da utilização das dependências do Sítio Manaju no horário estipulado das 8h no dia " + dataIn + " até às 21h do mesmo dia e se compromete a entregar as chaves das dependências devidamente fechada, no horário estipulado, ao(à) LOCADOR(A).")
        else:
            text = ("\t\t\t\t\t\t\t\t\tParágrafo III: O(A) LOCATÁRIO(A) fica ciente, da utilização das dependências do Sítio Manaju no horário estipulado das 8h do dia " + dataIn + " até às 21h do dia " + dataOut + " e se compromete a entregar as chaves das dependências devidamente fechada, no horário estipulado, ao(à) LOCADOR(A).")
        pdf.multi_cell(0, 6, txt = text, border = 0, align = "J", fill = False)
        pdf.ln(h = '')

        text = ("\t\t\t\t\t\t\t\t\tParágrafo IV: O(A)LOCATÁRIO(A) fica ciente, da utilização das dependências do Sitio Manaju, por parte de decoração ou entregas de bebidas e comidas, dentro do horário estipulado.")
        pdf.multi_cell(0, 6, txt = text, border = 0, align = "J", fill = False)
        pdf.ln(h = '')

        if pag == 1:
            text = ("\t\t\t\t\t\t\t\t\tCLAUSULA SEGUNDA: O valor da locação será de " + valor + " (" + number2words(valor) + ") a ser pago da seguinte maneira: por transferência via pix para a chave \"043991113108\" no ato da assinatura do contrato.")
        else:
            text = ("\t\t\t\t\t\t\t\t\tCLAUSULA SEGUNDA: O valor da locação será de " + valor + " (" + number2words(valor) + ") a ser pago da seguinte maneira: por transferência via pix para a chave \"043991113108\" no ato da assinatura do contrato.")
        pdf.multi_cell(0, 6, txt = text, border = 0, align = "J", fill = False)
        pdf.ln(h = '')

        text = ("\t\t\t\t\t\t\t\t\tParágrafo I: Este contrato somente terá validade, mediante ao pagamento total da locação através de recibo ou comprovante de depósito, caso contrário, o mesmo se tornará nulo.")
        pdf.multi_cell(0, 6, txt = text, border = 0, align = "J", fill = False)
        pdf.ln(h = '')

        text = ("\t\t\t\t\t\t\t\t\tParágrafo II: Fica estipulado uma multa no valor de 30% do valor do aluguel em caso de cancelamento do contrato.")
        pdf.multi_cell(0, 6, txt = text, border = 0, align = "J", fill = False)
        pdf.ln(h = '')

        text = ("\t\t\t\t\t\t\t\t\tCLAUSULA TERCEIRA: O(A) LOCATÁRIO(A) fica sob exclusiva responsabilidade pela integridade física de terceiros, dentro das dependências do SÍTIO MANAJU de Ibaiti-PR.")
        pdf.multi_cell(0, 6, txt = text, border = 0, align = "J", fill = False)
        pdf.ln(h = '')

        text = ("\t\t\t\t\t\t\t\t\tCLAUSULA QUARTA: O(A) LOCATÁRIO(A) fica ciente da utilização da PISCINA, quando houver em contrato, que é para uso adulto de acordo com suas medidas, e que qualquer criança que venha a usar a PISCINA, deverá estar acompanhada de um adulto, e que também é terminantemente proibido a entrada com produtos oleosos " +
                    "e com roupas não apropriadas, ficando somente autorizado a entrada com roupas de banho.")
        pdf.multi_cell(0, 6, txt = text, border = 0, align = "J", fill = False)
        pdf.ln(h = '')

        text = ("\t\t\t\t\t\t\t\t\tCLAUSULA QUINTA: Será de responsabilidade do(a) LOCATÁRIO(A), e ficando proibido fornecer ainda que gratuitamente, entregar bebidas alcoólicas a criança ou adolescente (menores de 18 anos), nos termos do art. 63, da Lei Contravenções Penais c/c o Art. 81 e 243, da Lei 8.069-90 e também proibido o consumo de drogas " + 
                    "ilícitas dentro das dependências do SÍTIO MANAJU de Ibaiti-PR.")
        pdf.multi_cell(0, 6, txt = text, border = 0, align = "J", fill = False)
        pdf.ln(h = '')

        text = ("\t\t\t\t\t\t\t\t\tCLAUSULA SEXTA: O(A) LOCATÁRIO(A) obriga-se, sob exclusiva responsabilidade financeira, a repor ou consertar equipamentos e edificações eventualmente destruídos ou danificados durante o evento em razão de seu mau uso.")
        pdf.multi_cell(0, 6, txt = text, border = 0, align = "J", fill = False)
        pdf.ln(h = '')

        text = ("\t\t\t\t\t\t\t\t\tParágrafo I: O(A) LOCATÁRIO(A), obriga-se, sob exclusiva responsabilidade financeira, a repor ou consertar, quaisquer objetos ou valores, perdidos ou furtados de terceiros envolvidos no evento.")
        pdf.multi_cell(0, 6, txt = text, border = 0, align = "J", fill = False)
        pdf.ln(h = '')

        text = ("\t\t\t\t\t\t\t\t\tCLAUSULA SÉTIMA: Fica proibido o uso de fogos de artifício, rojões e similares durante o evento.")
        pdf.multi_cell(0, 6, txt = text, border = 0, align = "J", fill = False)
        pdf.ln(h = '')

        text = ("\t\t\t\t\t\t\t\t\tCLAUSULA OITAVA: O(A) LOCATÁRIO(A) se confessam conhecedores das condições estruturais do local da realização do evento, devendo colocar o número de pessoas compatíveis com esta estrutura, devendo ainda levar em conta as condições de tempo da oportunidade, responsabilizando-se exclusiva e inteiramente, por prejuízos " +
                    "que a não observância destas regras, causar à SÍTIO MANAJU de Ibaiti-PR ou a terceiros.")
        pdf.multi_cell(0, 6, txt = text, border = 0, align = "J", fill = False)
        pdf.ln(h = '')

        text = ("\t\t\t\t\t\t\t\t\tCLAUSULA NONA: O(A) LOCATÁRIO(A) se declara ciente quanto as normas ao combate do Covid-19 e deverá cumprir integralmente as normas e regras do último decreto vigente emitido pela Prefeitura Municipal de Ibaiti-Pr. E também da responsabilidade em buscar informações junto ao órgão da Prefeitura sobre o decreto " +
        "vigente sobre o combate ao Covid-19.")
        pdf.multi_cell(0, 6, txt = text, border = 0, align = "J", fill = False)
        pdf.ln(h = '')

        text = ("\t\t\t\t\t\t\t\t\tE, por estarem assim, justos e contratados, firmam o presente instrumento em duas vias, ficando o fórum da comarca de Ibaiti-PR, para que possam dirimir quaisquer dúvidas.")
        pdf.multi_cell(0, 6, txt = text, border = 0, align = "J", fill = False)
        pdf.ln(h = '')

        pdf.multi_cell(0, 6, txt = "\n\n\n\n\n\n\n\n", border = 0, align = "R", fill = False)

        pdf.cell(200, 10, txt = "____________________________",
            ln = 1, align = 'C')
        pdf.cell(200, 10, txt = "SÍTIO MANAJU",
            ln = 1, align = 'C')
        pdf.cell(200, 10, txt = "LOCADOR(A)",
            ln = 1, align = 'C')

        pdf.multi_cell(0, 6, txt = "\n\n\n\n\n\n\n", border = 0, align = "R", fill = False)

        pdf.cell(200, 10, txt = "____________________________",
            ln = 1, align = 'C')
        pdf.cell(200, 10, txt = nome.upper(),
            ln = 1, align = 'C')
        pdf.cell(200, 10, txt = "LOCATÁRIO(A)",
            ln = 1, align = 'C')

        pdf.multi_cell(0, 6, txt = "\n\n\n\n\n\n\n\n\n\n", border = 0, align = "R", fill = False)

        text = ("Ibaiti, " + dataAss + ".")
        pdf.multi_cell(0, 6, txt = text, border = 0, align = "R", fill = False)
        
        pdf.output((str(counter()) + " - " + nome + ".pdf"))
        print("-> Documento gerado com sucesso!")
    except Exception as e:
        log(e)
        print("-> Houve um problema ao gerar o documento.")