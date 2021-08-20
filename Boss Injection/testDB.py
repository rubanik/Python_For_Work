import pyodbc
import datetime
import random

n = 24

#Возвращаем случайное число в пределах от 0 до n
def getRandom(n):
    a = random.randint(0,n)
    return a

#Вычитаем текущую дату и дельту, возвращаем дату аудита, отмотанную на *до 30 минут* назад
def makeItPast(now, delta):
    past = now - delta
    return past

#Возвращаем дельту со случайными : Минуты 0-30, секунды 0-59, микросекунды 0-100000
def getDelta():
    delta = datetime.timedelta(days=0,
                           seconds=random.randint(0,59),
                           microseconds=random.randint(0,100000),
                           minutes=random.randint(10,30),
                           hours=0,
                           weeks=0)
    return delta

def getLoginDate(curr):
    deltaLogin = datetime.timedelta(days=0,
                           seconds=random.randint(0,59),
                           microseconds=random.randint(0,100000),
                           minutes=random.randrange(2,10,2),
                           hours=0,
                           weeks=0)
    loginDate = curr - deltaLogin
    return loginDate
    
    
def getFinishList(good, bad):
    finalList =[]
    for i in range(2):
        finalList.append(good[random.randint(0,len(good)-1)])
    #finalList.append(bad[random.randint(0,len(bad)-1)])
    finalList.append(bad[random.randint(0,4)])
    return finalList

def getGood(listOfGoodPattern):
     goodList = [  makeItPast(currDate,getDelta()).date(),   # AuditDate ДАТА АУДИТА
                    makeItPast(currDate,getDelta()).time().strftime('%H:%M'),   # AuditTime ВРЕМЯ АУДИТА
                    50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
                    28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ В КОТОРОМ РАБОТАЮ - ВСЕГДА 28
                    27,                                        # ObsOpenCellID ЯЧЕЙКА К КОТОРОЙ ЗАКРЕПЛЁН - ВСЕГДА 0
                    2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
                    0,                                        # PerfJobID ДОЛЖНОСТЬ ТОГО КОГО НАБЛЮДАЕМ - ВСЕГДА 0
                    1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
                    None,                                     # PerfopenCellID ВСЕГДА NONE
                    '',                                       # ContractorName ИМЯ - ВСЕГДА ""
                    4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
                    listOfGoodPattern[0],                               # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА
                    listOfGoodPattern[1],                                # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
                    listOfGoodPattern[2],                               # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
                    listOfGoodPattern[3],                              # ViolationID ТИП НАРУШЕНИЯ
                    0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
                    0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
                    '',                                       # Comments КОМЕНТАРИЙ
                    '',                                       # Commitment ДОГОВОРЁННОСТЬ
                    '',                                       # Gratitude БЛАГОДАРНОСТЬ
                    int(currDate.strftime("%W")),                 # AuditWeek НЕДЕЛЯ АУДИТА
                    int(currDate.strftime("%m")),                                        # AuditMonth МЕСЯЦ АУДИТА
                    int(currDate.strftime("%Y")),                                     # AuditYear ГОД АУДИТА
                    'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
                    getLoginDate(currDate),                                 # LogDate КОГДА ЗАЛОГИНЕН
                    'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
                    ]
     return goodList
def getBad(listOfBadPattern):
     badList = [  makeItPast(currDate,getDelta()).date(),   # AuditDate ДАТА АУДИТА
                    makeItPast(currDate,getDelta()).time().strftime('%H:%M'),   # AuditTime ВРЕМЯ АУДИТА
                    50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
                    28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ В КОТОРОМ РАБОТАЮ - ВСЕГДА 28
                    27,                                        # ObsOpenCellID ЯЧЕЙКА К КОТОРОЙ ЗАКРЕПЛЁН - ВСЕГДА 0
                    2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
                    0,                                        # PerfJobID ДОЛЖНОСТЬ ТОГО КОГО НАБЛЮДАЕМ - ВСЕГДА 0
                    1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
                    None,                                     # PerfopenCellID ВСЕГДА NONE
                    '',                                       # ContractorName ИМЯ - ВСЕГДА ""
                    4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
                    listOfBadPattern[0],                      # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА
                    listOfBadPattern[1],                      # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
                    listOfBadPattern[2],                      # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
                    listOfBadPattern[3],                      # ViolationID ТИП НАРУШЕНИЯ
                    9,                                        # PrimReasonID ВИД НАРУШЕНИЯ
                    222,                                      # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
                    '',                                       # Comments КОМЕНТАРИЙ
                    getCommitment(),                                       # Commitment ДОГОВОРЁННОСТЬ
                    '',                                       # Gratitude БЛАГОДАРНОСТЬ
                    int(currDate.strftime("%W")),                 # AuditWeek НЕДЕЛЯ АУДИТА
                    int(currDate.strftime("%m")),                                        # AuditMonth МЕСЯЦ АУДИТА
                    int(currDate.strftime("%Y")),                                     # AuditYear ГОД АУДИТА
                    'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
                     getLoginDate(currDate),                                 # LogDate КОГДА ЗАЛОГИНЕН
                    'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
                    ]
     return badList

def sortLogDate(i):
    return i[n]
currDate = datetime.datetime.now() # Get current date
AuditDate = makeItPast(currDate,getDelta())


def getCommitment():
    return listOfCommitments[getRandom(4)]
    
listOfCommitments = ['Сделал замечание.',
                    'Обратная связь получена',
                    'ОК',
                    'Нет',
                    'Договорились'
                    ]
listOfGoodPatterns = [[45,0,21,186],# 0 Приветствие в офисе -            45,0,21,186
                    [310,0,11,94],  # 1 Ношение каскетки на группе 206 - 310,0,11,94
                    [311,0,11,94],  # 2 Ношение каскетки на группе 207 - 311,0,11,94
                    [93,0,11,94],   # 3 Ношение каскетки на группе 205 - 93,0,11,94
                    [310,0,11,87],  # 4 Ношение берушей на группе 206 -  310,0,11,87
                    [311,0,11,87],  # 5 Ношение берушей на группе 207 -  311,0,11,87
                    [93,0,11,87],   # 6 Ношение берушей на группе 205 -  93,0,11,87
                    [310,0,11,89],  # 7Ношение перчаток на группе 206 -  310,0,11,89
                    [311,0,11,89],  # 8 Ношение перчаток на группе 207 - 311,0,11,89
                    [93,0,11,89],   # 9 Ношение перчаток на группе 205 - 93,0,11,89
                    [22,0,21,185]   # 10 Чихание в столовой -            22,0,21,185
                    ]
listOfBadPatterns = [[45,1,21,186],# 0 Приветствие в офисе -             45,1,21,186
                    [22,1,21,185], # 10 Чихание в столовой -             22,1,21,185
                    [39,1,1,2],    # Телефон на пешеходной дорожке       39,1,1,2
                    [45,1,3,24],   # Курение в офисном помещении RRP     45,1,3,24
                    [39,1,1,3],    # Вне пешеходной дорожка\бег          39,1,1,3
                    [310,1,11,94], # 1 Ношение каскетки на группе 206 -  310,1,11,94
                    [311,1,11,94], # 2 Ношение каскетки на группе 207 -  311,1,11,94
                    [93,1,11,94],  # 3 Ношение каскетки на группе 205 -  93,1,11,94
                    [310,1,11,87], # 4 Ношение берушей на группе 206 -   310,1,11,87
                    [311,1,11,87], # 5 Ношение берушей на группе 207 -   311,1,11,87
                    [93,1,11,87],  # 6 Ношение берушей на группе 205 -   93,1,11,87
                    [310,1,11,89], # 7Ношение перчаток на группе 206 -   310,1,11,89
                    [311,1,11,89], # 8 Ношение перчаток на группе 207 -  311,1,11,89
                    [93,1,11,89]   # 9 Ношение перчаток на группе 205 -  93,1,11,89
                    
                    ]

#Генерируем списки с записями хороший\плохой
g1 = [getGood(x) for x in listOfGoodPatterns]
b1 = [getBad(x) for x in listOfBadPatterns]

print('Генерируем 3  BOS...')
#Генерируем один финальный список, который включает в себя 2 good наблюдения и 1 bad. 
oneBadTwoGoodList = getFinishList(g1, b1)

# Сортируем по дате
oneBadTwoGoodList.sort(key=sortLogDate)

print('Подключамся к BOS DataBase')
#conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\arubanik\Documents\Database1.accdb;') # WIN
#conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=\\pmintl.net\deptdata\PMI-RU-SPB-ORG\EHSS\Common\2_BEHAVIORAL AUDITS\Database tables\BOS\bos_be.mdb;') # WIN 
#conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=\\pmintl.net\deptdata\PMI-RU-SPB-ORG\EHSS\Common\2_BEHAVIORAL AUDITS\Database tables\BOS\Bos_be.accdb;') # WIN
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=M:\EHSS\Support\Clients\BOS.accdb;') # WIN
cursor = conn.cursor()
print('Выполняем запрос...')
cursor.executemany("INSERT INTO tblAudit(AuditDate, AuditTime, ObserverID, ObsDepartmentID, ObsOpenCellID, PerfDepartmentID, PerfJobID, PerfTypeID, PerfopenCellID, ContractorName, AuditZone, AuditPlace, ViolIndex, ViolTypeID, ViolationID, PrimReasonID,SysReasonID, Comments, Commitment, Gratitude, AuditWeek, AuditMonth, AuditYear, LogUser, LogDate, AuditShift) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", oneBadTwoGoodList)
conn.commit()
cursor.execute('select * from tblAudit')
print('Выполнено')


