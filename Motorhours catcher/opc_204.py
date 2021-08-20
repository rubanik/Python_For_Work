from opcua import Client

SS = "Basic256,SignAndEncrypt,mycert1.der,key.pem"
OPC_SERVER_ADR_LU204_ITM = "opc.tcp://10.143.242.91:49320"
OPC_SERVER_ADR_LU204_GIMA = "opc.tcp://10.143.242.92:49320"
OPC_SERVER_ADR_LU204_SENZANI = "opc.tcp://10.143.242.93:49320"

tagnames_dict = {
    '204_CT_Transp':'OPC DA.CTU_810036.sNonResettableCounters.i32RunningTimeCTTransp',
    '204_CT_Left':'OPC DA.CTU_810036.sNonResettableCounters.i32RunningTimeCTLeft',
    '204_CT_Right':'OPC DA.CTU_810036.sNonResettableCounters.i32RunningTimeCTRight',
    '204_ITM_Sol':'SOLARIS_720084.MachineData.RunningTime',
    '204_ITM_Capricorn':'TCP/IP-TwinCAT.Capricorn_21839353.DATACONNECTIVITY.DC_LIVE.NCOUNTERSAREA.RUNNINGTIMECOUNTER',
    '204_ITM_Saturn':'TCP/IP-TwinCAT.Saturn_21879108.DATACONNECTIVITY.DC_LIVE.NCOUNTERSAREA.RUNNINGTIMECOUNTER',
    '204_FlexA5':'Line.BridgePC.TH1.RunningTimeCounter',
    '204_FlexWF':'Line.BridgePC.TSW1.RunningTimeCounter',
    '204_FlexCO':'Line.BridgePC.TC1.RunningTimeCounter',
    '204_SenzaniCP':'Senzani SBNE.CPU 315 2DP PN.Statistic_Time_Hours_RUN'
    }

def get_LU201_data():
    pass

def get_LU202_data():
    pass

def get_LU203_data():
    pass

def get_LU204_data():
    pass

def get_PackerData():
    pass

def setup_connection(adr):
    client = Client(adr,timeout=60) # Make a Client
    client.set_security_string(SS) # Set Security Settings and choose ssl certificate, pub key
    client.application_uri = ('urn:opcua:python:server') #Change the client URN as the cirtificate's URN
    client.connect()
    return client

#*************************************************************************#
# Set connection with the LU 204 Combiner Line and get values of counters.#
#*************************************************************************#

try:
    client_204_itm = setup_connection(OPC_SERVER_ADR_LU204_ITM)
    
    print('Connected to the OPC-UA server ITM COMBINER + SATURN + CAPRICORN\n')

    print('Link Up #204 Combiner Line\n')
    ctt_time = client_204_itm.get_node('ns=2; s = %s'% (tagnames_dict['204_CT_Transp'])).get_value()
    ctr_time = client_204_itm.get_node('ns=2; s = %s'% (tagnames_dict['204_CT_Right'])).get_value()
    ctl_time = client_204_itm.get_node('ns=2; s = %s'% (tagnames_dict['204_CT_Left'])).get_value()
    itm_sol_time = client_204_itm.get_node('ns=2; s = %s'% (tagnames_dict['204_ITM_Sol'])).get_value()
    itm_cap_time = client_204_itm.get_node('ns=2; s = %s'% (tagnames_dict['204_ITM_Capricorn'])).get_value()
    itm_sat_time = client_204_itm.get_node('ns=2; s = %s'% (tagnames_dict['204_ITM_Saturn'])).get_value()
    
    print('Cut & Turn Trasport counter is:',ctt_time,'Min.')
    print('Cut & Turn Left Module Hours-counter is:',ctt_time,'Min.')
    print('Cut & Turn Right Module Hours-Scounter is:',ctt_time,'Min.')
    print('ITM Solaris Hours-counter is:',itm_sol_time,'Min.')
    print('ITM Capriconn Hours-counter is:',itm_cap_time,'Min.')
    print('ITM Saturn Hours-counter is:',itm_sat_time,'Min.')
    
except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    client_204_itm.disconnect()
    print('\nDiscinnected from Comb Line!')

#******************************************************************#
# Set connection with the Packer Line and get values of counters.  #
#******************************************************************#

try:
    client_204_gima = setup_connection(OPC_SERVER_ADR_LU204_GIMA)
    
    print('Link Up #204 Packer Line\n')

    flexA5_time = client_204_gima.get_node('ns=2; s = %s'% (tagnames_dict['204_FlexA5'])).get_value()
    flexWF_time = client_204_gima.get_node('ns=2; s = %s'% (tagnames_dict['204_FlexWF'])).get_value()
    flexCO_time = client_204_gima.get_node('ns=2; s = %s'% (tagnames_dict['204_FlexCO'])).get_value()
    
    print('GIMA FlexA5 Hours-counter is:',flexA5_time,'Min.')
    print('GIMA FlexWF Hours-counter is:',flexWF_time,'Min.')
    print('GIMA FlexCO Hours-counter is:',flexCO_time,'Min.')
    
except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    client_204_gima.disconnect()
    print('\nDiscinnected from Pack Line!')


    
#*******************************************************************************#
# Set connection with the Senzani Case Packer Line and get values of counters.  #
#*******************************************************************************#

try:
    client_204_senzani = setup_connection(OPC_SERVER_ADR_LU204_SENZANI)
    
    print('Link Up #204 Packer Line\n')

    case_packer_time = client_204_senzani.get_node('ns=2; s = %s'% (tagnames_dict['204_SenzaniCP'])).get_value()
    print('SENZANI Case Packer Hours-counter is:',case_packer_time,'Hrs.')
    
except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    client_204_senzani.disconnect()
    print('\nDiscinnected from Case Packer Line!')




#delim = '*-----------------------------------------------------*'
#print('\nLink Up #204 Combiner Line\n',delim)
#print('Cut & Turn Trasport counter is:',ctt_time,'Min.')
#print('Cut & Turn Left Module Hours-counter is:',ctt_time,'Min.')
#print('Cut & Turn Right Module Hours-Scounter is:',ctt_time,'Min.')
#print('ITM Solaris Hours-counter is:',itm_sol_time,'Min.')
#print('ITM Capriconn Hours-counter is:',itm_cap_time,'Min.')
#print('ITM Saturn Hours-counter is:',itm_sat_time,'Min.')
#print(delim+'\n')
#print('Link Up #204 Packer Line\n',delim)
#print('GIMA FlexA5 Hours-counter is:',flexA5_time,'Min.')
#print('GIMA FlexWF Hours-counter is:',flexWF_time,'Min.')
#print('GIMA FlexCO Hours-counter is:',flexCO_time,'Min.')
#print(delim+'\n')
#print('Link Up #204 Case Packer Line\n',delim)
#print('SENZANI Case Packer Hours-counter is:',case_packer_time,'Hrs.')
#print(delim+'\n')
