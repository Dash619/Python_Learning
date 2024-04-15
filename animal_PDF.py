from fpdf import FPDF
from pathlib import Path
import glob

pdf = FPDF(orientation="P", unit="mm", format="A4")
filepaths = glob.glob("Animals/*.txt")
for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem.capitalize()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"{filename}")

pdf.output(f"output.pdf")
