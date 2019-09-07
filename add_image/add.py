from Tkinter import *
from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from fpdf import FPDF

xname = int(input("x-axis: for name "))
yname = int(input("y-axis: for name "))
name = raw_input("Name ")
xevent = int(input("x-axis: for event "))
yevent = int(input("y-axis: for event "))
event = raw_input("Name ")
xs = int(input("x-axis: for sign "))
ys = int(input("y-axis: for sign "))

#font
pdfmetrics.registerFont(TTFont('Round', 'RoundhandBT.ttf'))

packet = StringIO.StringIO()
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=letter)
can.setFont('Round', 32)
can.drawString(xname, yname, name)
can.drawString(xevent, yevent, event)
imgPath = "logo.png"
can.drawImage(imgPath, xs, ys,mask='auto')

#can =canvas.Canvas(width=300, height=200, bg='black')
can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(file("2c.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = file("destination.pdf", "wb")
output.write(outputStream)
outputStream.close()


