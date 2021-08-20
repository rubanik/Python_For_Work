import PyPDF2
import re
import io

from openpyxl import Workbook




path = r'\\pmiruspbfnp60\Secondary\Documentation\7. LU07\GD (touchpad)\FR\FR1618503_002_78_Liste_Catalogo.pdf'
path2 = r'\\pmiruspbfnp60\Secondary\Documentation\7. LU07\GD (touchpad)\FR\FR1618502_002_7_Liste_Catalogo.pdf'
paths = [
    r'\\pmiruspbfnp60\Secondary\Documentation\7. LU07\GD (touchpad)\MC1\MC1605902_004_29_Liste_Catalogo.pdf',
    r'\\pmiruspbfnp60\Secondary\Documentation\7. LU07\GD (touchpad)\MC1\M11605802_001_25_Liste_Catalogo.pdf',
    r'\\pmiruspbfnp60\Secondary\Documentation\7. LU07\GD (touchpad)\MC1\M21605802_001_20_Liste_Catalogo.pdf',
    r'\\pmiruspbfnp60\Secondary\Documentation\7. LU07\GD (touchpad)\MC1\M31605802_001_90_Liste_Catalogo.pdf'
    ]
path3 = r'\\pmiruspbfnp60\Secondary\Documentation\7. LU07\GD (touchpad)\MC1\M21605802_001_20_Liste_Catalogo.pdf'
path4 = r'\\pmiruspbfnp60\Secondary\Documentation\7. LU07\GD (touchpad)\MC1\M31605802_001_90_Liste_Catalogo.pdf'
path5 = r'\\pmiruspbfnp60\Secondary\Documentation\7. LU07\GD (touchpad)\MC1\MC1605902_004_29_Liste_Catalogo.pdf'
path3 = r'\\pmiruspbfnp60\Secondary\Documentation\7. LU07\GD (touchpad)\MC1\M11605802_001_25_Liste_Catalogo.pdf'
def get_lines_from_pdf(path):

    pdfFile = open(path,'rb')
    prdReader = PyPDF2.PdfFileReader(pdfFile)
    num = prdReader.getNumPages()
    page = prdReader.getPage(26)
    text = page.extractText()

    result = []
    
    for page in range(num):
        page_act = prdReader.getPage(page)
        text_act = page_act.extractText()
        for line in io.StringIO(text_act):
            linez = line.split('\n')
            if linez[0][0:3] != '   ':
                if linez[0][0:3] != '---':
                    if linez[0][0:9] != 'G.D_s.p.a':
                        if linez[0][0:8] != ' S I G N':
                            if linez[0][0] == ' ':
                                if linez[0][0:4] != ' G.D':
                                    if linez[0][0:4] != '  **':
                                        if linez[0][0:4] != ' UFF':
                                            result.append(linez)
    pdfFile.close()
    return result

wb = Workbook()
ws = wb.active

for path in paths:

    equipment = get_lines_from_pdf(path)    

    for line in equipment:
        ws.append(line)



wb.save('MC1605902_004_29_Liste_Catalogo.xlsx')

#get_lines_from_pdf(path2)    
#get_lines_from_pdf(path3)    
                                        
