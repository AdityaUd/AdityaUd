# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 16:02:20 2023

@author: HP
"""

from textblob import TextBlob

from PyPDF2 import PdfReader

pdf_binary = PdfReader(r"C:\Users\HP\Desktop\Bhagavad_Gita_As_It_Is.pdf","rb")

def read_pdf(file):
    text = ""
    pdf = file  # Assuming pdf_binary is the PDF file object or path

    # Iterate over each page of the PDF
    for page in pdf.pages:
        text += page.extract_text()

    return text

whole_text = read_pdf(pdf_binary)



blob = TextBlob(whole_text)
print(blob.noun_phrases)



from pdfquery import PDFQuery


pdf = PDFQuery(r"C:\Users\HP\Documents\Aditya U Signed Offer Letter.pdf")
pdf.load()

line_elements = pdf.pq('LTTextLineHorizontal')

text = [t.text for t in line_elements]

print(text)