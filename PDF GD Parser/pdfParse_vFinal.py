import PyPDF2
import re, os
import io
from openpyxl import Workbook


def get_names_list():
    #Смотрим какие файлы есть в текущем каталоге
    name_list = []
    for name in os.listdir(): 
        if 'Liste' in name: # Если в имени есть Liste - значит это наш клиент
            name_list.append(name)
    print('Обнаружены файлы:', name_list,'\n')

    return name_list
    

def get_lines_from_pdf(path):
    # Парсим построчно пдф файл и отсееваем мусор
    
    pdfFile = open(path,'rb')
    prdReader = PyPDF2.PdfFileReader(pdfFile)
    num = prdReader.getNumPages()
    page = prdReader.getPage(26)
    text = page.extractText()

    result = []
    print( f'Обрабатыываем {path}')
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

    pdfFile.close()
    return result

def get_lines_from_pdf_v2(path):

    # Парсим построчно пдф файл и отсееваем мусор
    
    pdfFile = open(path,'rb')
    prdReader = PyPDF2.PdfFileReader(pdfFile)
    num = prdReader.getNumPages()
    page = prdReader.getPage(26)
    text = page.extractText()

    result = []
    print( f'Обрабатыываем {path}')
    
    for page in range(num):
        page_act = prdReader.getPage(page)
        text_act = page_act.extractText()
        
        for line in io.StringIO(text_act):
            linez = line.split('\n')
            if re.fullmatch(r'\d{1} ',linez[0][-2:]):
                if linez[0][0:5] == '     ':
                    linez[0] = change_empty_name(last_line, linez[0])
                last_line = linez[0]
                result.append(linez)
                print(linez)
    
    pdfFile.close()
    return result


def change_empty_name(last,current):

    new_line_with_name = ' ' + last.split()[0] + current[len(last.split()[0])+1:]
    return new_line_with_name
   
#get_lines_from_pdf_v2('FR1618503_002_78_Liste_Catalogo.pdf')


print('Создаём папку Export в корневом каталоге\n')
os.mkdir('Export')

for path in get_names_list():

    equipment = get_lines_from_pdf_v2(path)
    
    wb = Workbook()
    ws = wb.active
    
    for line in equipment:
        ws.append(line)
        pass

    wb.save(f'.\Export\{path}.xlsx')

###get_lines_from_pdf(path2)    
##get_lines_from_pdf(path3)    
##                                        
