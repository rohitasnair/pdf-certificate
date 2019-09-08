import xlrd
def null():
    #print "Null",
    return "Null"
def green():
    #print "Greeen",
    return "Greeen"
def yellow():
    #print "Yellow",
    return "Yellow"
def brown():
    #print "Brown",
    return "Brown"
def red():
    #print "Red",
    return "Red"
def orange():
    #print "Orange",
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
                10:red(),
                52:orange(),
                64:white()
             }
    return switcher.get(i,"Invalid")


book = xlrd.open_workbook("test1.xls", formatting_info=True)
sheets = book.sheet_names()
#print sheets
print "sheets are:", sheets
for index, sh in enumerate(sheets):
    sheet = book.sheet_by_index(index)
    
    rows, cols = 15, 14
    print "Number of rows: %s   Number of cols: %s" % (rows, cols)
    for row in range(rows):
        for col in range(cols):
            xfx = sheet.cell_xf_index(row, col)
            xf = book.xf_list[xfx]
            bgx = xf.background.pattern_colour_index
            a=bgx
            thecell = sheet.cell(row, col).value
            if thecell=='':
                continue
            print(colour(bgx))
       	    print thecell
print 'end'
print "Sheet:", sheet.name 
