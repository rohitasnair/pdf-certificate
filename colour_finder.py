import xlrd
def colour(i):
    switcher={
                8:'Null',
                11:'Green',
                13:'Yellow',
                14:'Brown',
                10:'Red',
                52:'Orange',
                64:'White'
             }
    print switcher.get(i,"Invalid"),
book = xlrd.open_workbook("test1.xls", formatting_info=True)
sheets = book.sheet_names()
#print sheets
print "sheets are:", sheets
for index, sh in enumerate(sheets):
    sheet = book.sheet_by_index(index)
    print "Sheet:", sheet.name
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
            colour(bgx)
       	    print thecell
print 'end'
