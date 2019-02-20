from visidata import vd, asyncthread

def open_xlsb(p):
    push_xlsb(p)
    return vd.push(vd.sheetsSheet)

@asyncthread
def push_xlsb(p):
    import pyxlsb

    wb = pyxlsb.open_workbook(p.resolve())
    for name in wb.sheets:
        vs = wb.get_sheet(name, True)
        vs.reload()
        vd.sheets.append(vs)
