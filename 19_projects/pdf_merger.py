from PyPDF2 import PdfMerger
import os

print("Current working directory:", os.getcwd())

merger = PdfMerger()
pdfs = []
n = int(input("how many pdf do you want to merge\n"))
for i in range(n):
    name = input(f"the pdf name is {i + 1}: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()