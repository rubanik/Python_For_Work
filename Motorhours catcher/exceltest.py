from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from datetime import datetime

now = datetime.now() # current date and time
date_time = now.strftime("%d.%m.%Y %H-%M-%S")

wb = Workbook()
#dest_filename = './Output/Данные о моточасах за [ %s ].xlsx' % (date_time)

dest_filename1 = u'Y:/RRP Operations/RRP Technical Services/SECONDARY/10 EQUIPMENT MOTOR HOURS/Данные о моточасах за [ %s ].xlsx' % (date_time)
dest_filename2 = u'O:/RRP Operations/RRP Technical Services/SECONDARY/10 EQUIPMENT MOTOR HOURS/Данные о моточасах за [ %s ].xlsx' % (date_time)

ws1 = wb.active
ws1.title = 'Data from all lines'
ws1.column_dimensions['A'].width = 40
ws1.append(["Equipment", "Hours"])


def save():
    try:
        wb.save(filename = dest_filename1)
        print('Saved as -''%s' % dest_filename1)
    except:
        wb.save(filename = dest_filename2)
        print('Saved as -''%s' % dest_filename2)
    
def saveToExcell(dictData):
    arr = []
    for x in dictData:
        name = x
        val = dictData[x][1]
        arr1 = [name, val]
        arr.append(arr1)

    for val in arr:
        ws1.append(val)

    save()
