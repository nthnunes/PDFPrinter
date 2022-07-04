from fpdf import FPDF

def newPDF(nome, rg) -> None:
    pdf = FPDF(format='A4')  
    pdf.add_page()

    pdf.set_font("Arial", style = 'B', size = 15)
    pdf.cell(200, 10, txt = "CONTRATO DE LOCAÇÃO POR INSTRUMENTO PARTICULAR",
            ln = 1, align = 'C')
    pdf.ln(h = '')
        
    text = "Contrato de locação com condição que fazem de um lado, o "
    pdf.set_font("Arial", size = 13)
    pdf.write(5, text)

    pdf.set_font("Arial", style = 'B', size = 13)
    pdf.write(5, "LOCADOR(A): ")

    text = ("SÍTIO MANAJU em Ibaiti-PR, representada pela proprietária: JULIANE APARECIDA PEDRO E NUNES, portador(a) do RG: 4604817-2 - " +
    "SSP-PR e do CPF: 005846289-94 e de outro lado, o ")
    pdf.set_font("Arial", size = 13)
    pdf.write(5, text)

    pdf.set_font("Arial", style = 'B', size = 13)
    pdf.write(5, "LOCATÁRIO(A): ")

    pdf.set_font("Arial", size = 13)
    pdf.write(5, nome)

    pdf.set_font("Arial", size = 13)
    pdf.write(5, ", RG: ")

    pdf.set_font("Arial", size = 13)
    pdf.write(5, rg)


    pdf.output("document.pdf")