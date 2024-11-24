from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")
for index, row in df.iterrows():
    pdf.add_page()

    # Set the header
    pdf.set_font(family="Times", style="B", size=30)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    # pdf.line(10, 22, 200, 22) # For only one line at header
    for y in range(20, 298, 10): # For lines in all the page
        pdf.line(10, y, 200, y)

    # Set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=11)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for items in range(row["Pages"] - 1):
        pdf.add_page()

        # Set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=11)
        pdf.set_text_color(50, 50, 50)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        for y in range(20, 298, 10):  # For lines in all the doc
            pdf.line(10, y, 200, y)

pdf.output("output_lines.pdf")