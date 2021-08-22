"""
Данный скрипт необходим для выборки запчастей из каталогов GD, которые лежат вместе с 
электросхемами. 
"""
import re
import os
import io
import PyPDF2
from openpyxl import Workbook


def get_names_list():
    """
    #Смотрим какие файлы есть в текущем каталоге
    """
    name_list = []
    for name in os.listdir():
        if 'Liste' in name: # Если в имени есть Liste - значит это наш клиент
            name_list.append(name)
    print('Обнаружены файлы:', name_list,'\n')

    return name_list

def get_lines_from_pdf(path):
    """
    Первая версия. Отсеевание идёт с права на лево
    Парсим пдф файл и в соответствии с его форматированием вытаскиваем нужные данные
    Естесственно подходит только для имеющихся каталогов GD
    """
    pdf_file = open(path,'rb')
    prd_reader = PyPDF2.pdf_fileReader(pdf_file)
    num = prd_reader.getNumPages()
    page = prd_reader.getPage(26)
    #text = page.extractText()

    result = []
    print( f'Обрабатыываем {path}')
    for page in range(num):
        page_act = prd_reader.getPage(page)
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
    pdf_file.close()
    return result

def get_lines_from_pdf_v2(path):
    """
    Вторая версия, актуальная. Отсеевание идёт с лева на право.
    Парсим пдф файл и в соответствии с его форматированием вытаскиваем нужные данные
    Естесственно подходит только для имеющихся каталогов GD
    """
    pdf_file = open(path,'rb')
    prd_reader = PyPDF2.pdf_fileReader(pdf_file)
    num = prd_reader.getNumPages()
    page = prd_reader.getPage(26)
    #text = page.extractText()

    result = []
    print( f'Обрабатыываем {path}')
    
    for page in range(num):
        page_act = prd_reader.getPage(page)
        text_act = page_act.extractText()
        for line in io.StringIO(text_act):
            linez = line.split('\n')
            if re.fullmatch(r'\d{1} ',linez[0][-2:]):
                if linez[0][0:5] == '     ':
                    linez[0] = change_empty_name(last_line, linez[0])
                last_line = linez[0]
                result.append(linez)
                print(linez)
    
    pdf_file.close()
    return result

def change_empty_name(last,current):
    """
    Во время обработки(да и в оригинальном файле) после названия компонента идут строки,
    которые начинаются с "". Здесь мы заподняем эти строки предидущим названием. Необходимо,
    что бы в дальнейшем нормально фильтровалос в Excel.

    До:
    11AB13      Sensor  Phoenix
                Cable   Cable
                Socket  3x5

    После:
    11AB13      Sensor  Phoenix
    11AB13      Cable   Cable
    11AB13      Socket  3x5

    """
    new_line_with_name = ' ' + last.split()[0] + current[len(last.split()[0])+1:]
    return new_line_with_name

print('Создаём папку Export в корневом каталоге\n')
os.mkdir('Export')

for path in get_names_list():

    equipment = get_lines_from_pdf_v2(path)
    
    wb = Workbook()
    ws = wb.active
    
    for line in equipment:
        ws.append(line)

    wb.save(f'.\\Export\\{path}.xlsx')
