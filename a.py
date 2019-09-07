import xlrd
book = xlrd.open_workbook("test.xls", formatting_info=True)
sheets = book.sheet_names()
print "sheets are:", sheets
for index, sh in enumerate(sheets):
    sheet = book.sheet_by_index(index)
    print "Sheet:", sheet.name
    rows, cols = 15, 14
    print "Number of rows: %s   Number of cols: %s" % (rows, cols)
    for row in range(rows):
        for col in range(cols):
            print "row, col is:", row+1, col+1,
            thecell = sheet.cell(row, col)      
            print thecell.value,
            xfx = sheet.cell_xf_index(row, col)
            xf = book.xf_list[xfx]
            bgx = xf.background.pattern_colour_index
            print bgx
            if bgx=='10':
                continue