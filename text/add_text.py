from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
import os
import PyPDF2
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
#import PyPDF2 

def PDFmerge(pdfs, output): 
	# creating pdf file merger object 
	pdfMerger = PyPDF2.PdfFileMerger() 
	
	# appending pdfs one by one 
	for pdf in pdfs: 
		with open(pdf, 'rb') as f: 
			pdfMerger.append(f) 
		
	# writing combined pdf to output pdf file 
	with open(output, 'wb') as f: 
		pdfMerger.write(f) 

pdfmetrics.registerFont(TTFont('Round', 'RoundhandBT.ttf'))

packet = StringIO.StringIO()
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=letter)
can.setFont('Round', 25)
can.drawString(205, 480, "QWERTYUOP")
can.drawString(140, 427, "Healthy Beverage Making")

can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(file("2.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = file("destination.pdf", "wb")
output.write(outputStream)
outputStream.close()

pdfs = ['destination.pdf', 'end.pdf'] 
output = 'final.pdf'
PDFmerge(pdfs = pdfs, output = output) 
os.remove("destination.pdf")
