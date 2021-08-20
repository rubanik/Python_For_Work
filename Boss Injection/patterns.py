#GOOD PATTERNS:
# Приветствие в офисе - 45,0,21,186
good_0 = [makeItPast(currDate,getDelta()).date(),  # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          45,                                       # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА                    
          0,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          21,                                       # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          186,                                      # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]
# Ношение каскетки на группе 206 - 310,0,11,94
good_1 = [makeItPast(currDate,getDelta()).date(),   # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          310,                                      # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА                    
          0,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          11,                                       # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          94,                                       # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]
# Ношение каскетки на группе 207 - 311,0,11,94
good_2 = [makeItPast(currDate,getDelta()).date(),   # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          311,                                      # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА 
          0,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          11,                                       # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          94,                                       # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]
# Ношение каскетки на группе 205 - 93,0,11,94
good_3 = [makeItPast(currDate,getDelta()).date(),   # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          93,                                      # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА 
          0,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          11,                                       # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          94,                                       # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]
          
# Ношение берушей на группе 206 - 310,0,11,87
good_4 = [makeItPast(currDate,getDelta()).date(),   # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          310,                                      # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА                    
          0,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          11,                                       # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          87,                                       # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]

# Ношение берушей на группе 207 - 311,0,11,87
good_5 = [makeItPast(currDate,getDelta()).date(),   # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          311,                                      # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА                    
          0,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          11,                                       # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          87,                                       # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]
          
# Ношение берушей на группе 205 - 93,0,11,87
good_6 = [makeItPast(currDate,getDelta()).date(),   # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          93,                                       # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА                    
          0,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          11,                                       # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          87,                                       # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]
          
# Ношение перчаток на группе 206 - 310,0,11,89
good_7 = [makeItPast(currDate,getDelta()).date(),   # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          310,                                      # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА                    
          0,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          11,                                       # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          89,                                       # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]
               
# Ношение перчаток на группе 207 - 311,0,11,89
good_8 = [makeItPast(currDate,getDelta()).date(),   # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          311,                                      # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА                    
          0,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          11,                                       # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          89,                                       # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]

# Ношение перчаток на группе 205 - 93,0,11,89
good_9 = [makeItPast(currDate,getDelta()).date(),   # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          93,                                       # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА                    
          0,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          11,                                       # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          89,                                       # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]

# Чихание в столовой 22,0,21,185
good_10 = [makeItPast(currDate,getDelta()).date(),  # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          22,                                       # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА                    
          0,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          21,                                       # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          185,                                      # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]

#BAD PATTERNS
# Приветствие в офисе 45,1,21,186
bad_0 = [makeItPast(currDate,getDelta()).date(),  # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          45,                                       # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА                    
          1,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          21,                                       # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          186,                                      # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]
# Ношение каскетки на группе 206 310,1,11,94
bad_1 = [makeItPast(currDate,getDelta()).date(),    # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          310,                                      # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА                    
          1,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          11,                                       # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          94,                                       # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]

# Ношение каскетки на группе 207 311,1,11,94
bad_2 = [makeItPast(currDate,getDelta()).date(),   # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          311,                                      # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА 
          1,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          11,                                       # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          94,                                       # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]

# Ношение каскетки на группе 205 93,1,11,94
bad_3 = [makeItPast(currDate,getDelta()).date(),   # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          93,                                       # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА 
          1,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          11,                                       # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          94,                                       # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]
          
# Ношение берушей на группе 206 310,1,11,87
bad_4 = [makeItPast(currDate,getDelta()).date(),   # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          310,                                      # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА                    
          1,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          11,                                       # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          87,                                       # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]

# Ношение берушей на группе 207 311,1,11,87
bad_5 = [makeItPast(currDate,getDelta()).date(),   # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          311,                                      # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА                    
          1,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          11,                                       # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          87,                                       # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]
          
# Ношение берушей на группе 205 93,1,11,87
bad_6 = [makeItPast(currDate,getDelta()).date(),   # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          93,                                       # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА                    
          1,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          11,                                       # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          87,                                       # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]
          
# Ношение перчаток на группе 206 310,1,11,89
bad_7 = [makeItPast(currDate,getDelta()).date(),   # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          310,                                      # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА                    
          1,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          11,                                       # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          89,                                       # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]
               
# Ношение перчаток на группе 207 311,1,11,89
bad_8 = [makeItPast(currDate,getDelta()).date(),   # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          311,                                      # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА                    
          1,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          11,                                       # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          89,                                       # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]

# Ношение перчаток на группе 205 93,1,11,89
bad_9 = [makeItPast(currDate,getDelta()).date(),   # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          93,                                       # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА                    
          1,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          11,                                       # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          89,                                       # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]

# Чихание в столовой 22,0,21,185
bad_10 = [makeItPast(currDate,getDelta()).date(),   # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          22,                                       # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА                    
          1,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          21,                                       # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          185,                                      # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]

# Телефон на пешеходной дорожке 39,1,1,2
bad_11 = [makeItPast(currDate,getDelta()).date(),   # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          39,                                       # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА                    
          1,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          1,                                        # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          2,                                        # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]

# Вне пешеходной дорожка\бег 39,1,1,3
bad_12 = [makeItPast(currDate,getDelta()).date(),  # AuditDate ДАТА АУДИТА
          makeItPast(currDate,getDelta()).time(),   # AuditTime ВРЕМЯ АУДИТА
          50510636,                                 # ObserverID ТАБЕЛЬНЫЙ НОМЕР - ВСЕГДА 50510636
          28,                                       # ObsDepartmentID ДЕПАРТАМЕНТ - ВСЕГДА 28
          0,                                        # ObsOpenCellID ЯЧЕЙКА - ВСЕГДА 27
          2,                                        # PerfDepartmentID ГДЕ ПРОВОДИЛСЯ АУДИТ - ВСЕГДА 2 
          98,                                       # PerfJobID ДОЛЖНОСТЬ - ВСЕГДА 0
          1,                                        # PerfTypeID ТИП РАБОТНИКА - ВСЕГДА 1
          None,                                     # PerfopenCellID ВСЕГДА NONE
          '',                                       # ContractorName ИМЯ - ВСЕГДА ""
          4,                                        # AuditZone ЗОНА ПРОВЕДЕНИЯ АУДИТА 
          39,                                       # AuditPlace МЕСТО ПРОВЕДЕНИЯ АУДИТА                    
          1,                                        # ViolIndex БЕЗОПАНЫЙ(0) ИЛИ НЕ БЕЗОПАСНЫЙ(1)
          1,                                       # ViolTypeID ГРУППА К КОТОРОЙ ОТНОСИТСЯ НАРУШЕНИЕ
          3,                                      # ViolationID ТИП НАРУШЕНИЯ
          0,                                        # PrimReasonID ВИД НАРУШЕНИЯ
          0,                                        # SysReasonID ПРИЧИНА ВОЗНИКНОВЕНИЯ НАРУШЕНИЯ
          '',                                       # Comments КОМЕНТАРИЙ
          '',                                       # Commitment ДОГОВОРЁННОСТЬ
          '',                                       # Gratitude БЛАГОДАРНОСТЬ
          7,                                        # AuditWeek НЕДЕЛЯ АУДИТА
          2,                                        # AuditMonth МЕСЯЦ АУДИТА
          2021,                                     # AuditYear ГОД АУДИТА
          'arubanik',                               # LogUser КТО ЗАЛОГИНЕН
          currDate,                                 # LogDate КОГДА ЗАЛОГИНЕН
          'Day'                                     # AuditShift СМЕНА - ВСЕГДА 'Day'
          ]


# #GOOD PATTERN:
# good_1 = [makeItPast(currDate,getDelta()).date(),makeItPast(currDate,getDelta()).time(),50510636,28,0,2,98,1,None,'',4,332,0,1,3,0,0,'Безопасно','','',7,2,2020,'arubanik',currDate,'Day']
# good_2 = [makeItPast(currDate,getDelta()).date(),makeItPast(currDate,getDelta()).time(),50510636,28,0,2,98,1,None,'',4,93,0,3,22,0,0,'','','',10,3,2020,'arubanik',currDate,'Day']

