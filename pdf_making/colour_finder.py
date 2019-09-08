import xlrd
from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
import os
import PyPDF2
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def pdf(names,event_name,certitype):
    if certitype==1:
        print certitype
        frontsheet="1.pdfs"
        namex=200
        namey=510
        eventx=225
        eventy=438
    else:
        print certitype
        frontsheet="2.pdfs"
        namex=205
        namey=480
        eventx=120
        eventy=427

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
    can.drawString(namex, namey, names.replace(".", " ").upper())
    can.drawString(eventx, eventy, event_name.upper())

    can.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read your existing PDF

    existing_pdf = PdfFileReader(file(frontsheet, "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    mycwd = os.getcwd()
    #os.makedirs(event_name)
    #os.chdir(event_name)
    # finally, write "output" to a real file
    outputStream = file("destination.pdf", "wb")
    output.write(outputStream)
    outputStream.close() 
    pdfs = ['destination.pdf', 'end.pdfs'] 
    output = names.upper()+'.pdf'
    PDFmerge(pdfs = pdfs, output = output) 
    os.remove("destination.pdf")
    #os.chdir(mycwd) 
def null():
    #print "Null",
    return "Null"
def green():
    #print "Greeen",
    #return 
    tempname=sheet.cell(row, col).value
    temps=sheet.name
    pdf(tempname,temps,2)
    return "Greeen"
def yellow():
    #print "Yellow",
    tempname=sheet.cell(row, col).value
    temps=sheet.name
    #pdf(tempname,temps,"winner")
    return "Yellow"
def brown():
    #print "Brown",
    tempname=sheet.cell(row, col).value
    temps=sheet.name
    pdf(tempname,temps,2)
    return "Brown"
def orange():
    #print "Orange",
    tempname=sheet.cell(row, col).value
    temps=sheet.name
    pdf(tempname,temps,2)
    return "Orange"
def white():
    #print "White",
    return "White"
def colour(i):
    switcher={
                8:null(),
                11:green(),
                13:yellow(),
                16:brown(),
                52:orange(),
                64:white()
             }
    return switcher.get(i,"Invalid")


book = xlrd.open_workbook("test.xls", formatting_info=True)
sheets = book.sheet_names()
#print sheets
print "sheets are:", sheets
for index, sh in enumerate(sheets):
    sheet = book.sheet_by_index(index)
    
    rows, cols = 11, 2
    print "Number of rows: %s   Number of cols: %s" % (rows, cols)
    for row in range(rows):
        for col in range(cols):
            xfx = sheet.cell_xf_index(row, col)
            xf = book.xf_list[xfx]
            bgx = xf.background.pattern_colour_index
            thecell = sheet.cell(row, col).value
            if thecell=='':
                continue
            print(colour(bgx)),
       	    print thecell
print 'end'
print "Sheet:", sheet.name 

