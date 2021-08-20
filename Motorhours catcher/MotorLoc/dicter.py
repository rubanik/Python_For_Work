import exceltest as et

dict = {'201_CT_Transp':['OPC DA.CTU_810032.uPMIDataConnectivity.sNonResettableCounters.i32RunningTimeCTTransp', 0 ],
'201_CT_Left':['OPC DA.CTU_810032.uPMIDataConnectivity.sNonResettableCounters.i32RunningTimeCTLeft', 0 ],
'201_CT_Right':['OPC DA.CTU_810032.uPMIDataConnectivity.sNonResettableCounters.i32RunningTimeCTRight', 0 ],
'201_ITM_Sol':['SOLARIS_720075.MachineData.RunningTime', 0 ]}

et.saveToExcell(dict)
