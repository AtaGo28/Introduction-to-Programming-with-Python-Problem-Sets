from fpdf import FPDF

pdf = FPDF()

name = input("Name: ")
pdf.add_page()
pdf.set_font("helvetica", "", 50)
pdf.cell(0, 60, "CS50 Shirtificate", align="C")
pdf.image("shirtificate.png", w=183, h=182, x=12, y=70)
pdf.set_text_color(255, 255, 255)
pdf.set_font_size(25)
pdf.text(x=55, y=140, txt=f"{name} took CS50")
pdf.output("shirtificate.pdf")