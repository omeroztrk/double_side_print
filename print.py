#!/bin/python3

# This program creates a printer query for double side printing for a file
# First parses a PDF file to odd and even pages. Then creates to pdf files

# read pdf file

import pypdf
import uuid
import sys

try:
    filename = sys.argv[1]
except IndexError:
    print(f"Usage: {sys.argv[0]} <filename>")
    sys.exit(1)

evenname = "/tmp/" + str(uuid.uuid4()) + ".pdf"
oddname = "/tmp/" + str(uuid.uuid4()) + ".pdf"

# create odd.pdf
pdfFileObj = open(filename, 'rb')
pdfReader = pypdf.PdfReader(pdfFileObj)
pdfWriter_odd = pypdf.PdfWriter()
pdfWriter_even = pypdf.PdfWriter()


# if page number is not even, add blank page at the end
if len(pdfReader.pages) % 2 != 0:
    pdfWriter_even.add_blank_page(pdfReader.pages[0].mediabox.width, pdfReader.pages[0].mediabox.height)

for pageNum in range(0, len(pdfReader.pages), 2):
    pageObj = pdfReader.pages[pageNum]
    pdfWriter_odd.add_page(pageObj)

for pageNum in range(1, len(pdfReader.pages), 2)[::-1]:
    pageObj = pdfReader.pages[pageNum]
    pdfWriter_even.add_page(pageObj)

pdfOutputFile_odd = open(oddname, 'wb')
pdfWriter_odd.write(pdfOutputFile_odd)
pdfOutputFile_odd.close()

pdfOutputFile_even = open(evenname, 'wb')
pdfWriter_even.write(pdfOutputFile_even)
pdfOutputFile_even.close()

pdfFileObj.close()

import cups
conn = cups.Connection()
printers = conn.getPrinters()
i = 0
for printer in printers:
    print(f"{i} : {printer}")
    i += 1

choice = int(input("Enter your choice: "))
choice = list(printers.keys())[choice]
print(f"Printing with {printers[choice]['printer-make-and-model']}")
jobID = conn.printFile(choice, oddname, "test.pdf odd pages", {})
print(f"Job ID: {jobID}")

r = ""
while r != "r":
    r = input("Press \"r\" and enter to print even pages: ")

jobID = conn.printFile(choice,evenname, "test.pdf even pages", {})
print(f"Job ID: {jobID}")
# remove the files
