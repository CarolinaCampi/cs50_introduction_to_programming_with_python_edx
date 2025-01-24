from fpdf import FPDF, Align

def main():
    name = input("Name: ")
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.ln(h=10)
    pdf.set_font('helvetica', size=40)
    pdf.cell(text="CS50 Shirtificate", align=Align.C, center=True)
    pdf.image("shirtificate.png", x=Align.C, y=50, w=pdf.epw)
    pdf.ln(h=95)
    pdf.set_font("helvetica", size=24)
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.cell(text=f"{name} took CS50", align=Align.C, center=True)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
