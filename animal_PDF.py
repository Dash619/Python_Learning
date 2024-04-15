from fpdf import FPDF
from pathlib import Path
import glob

pdf = FPDF(orientation="P", unit="mm", format="A4")
filepaths = glob.glob("Animals/*.txt")
for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem.capitalize()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"{filename}", ln=1)
    with open(filepath, 'r') as file:
        content = file.read()
        pdf.set_font(family="Times", size=12)
        pdf.multi_cell(w=0, h=6, txt=content)

pdf.output(f"Animals/output.pdf")
