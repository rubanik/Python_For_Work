from opcua import Client

SS = "Basic256,SignAndEncrypt,mycert1.der,key.pem"
OPC_SERVER_ADR_LU201_ITM = "opc.tcp://10.143.242.16:49320"
OPC_SERVER_ADR_LU201_GIMA = "opc.tcp://10.143.242.17:49320"
OPC_SERVER_ADR_LU201_SENZANI = "opc.tcp://10.143.242.20:49320"

tagnames_dict = {
    '201_CT_Transp':'OPC DA.CTU_810032.uPMIDataConnectivity.sNonResettableCounters.i32RunningTimeCTTransp',
    '201_CT_Left':'OPC DA.CTU_810032.uPMIDataConnectivity.sNonResettableCounters.i32RunningTimeCTLeft',
    '201_CT_Right':'OPC DA.CTU_810032.uPMIDataConnectivity.sNonResettableCounters.i32RunningTimeCTRight',
    '201_ITM_Sol':'SOLARIS_720075.MachineData.RunningTime',
    '201_ITM_Capricorn':'TCP/IP-TwinCAT.Capricorn_21839346.DATACONNECTIVITY.DC_LIVE.NCOUNTERSAREA.RUNNINGTIMECOUNTER',
    '201_ITM_Saturn':'TCP/IP-TwinCAT.Saturn_21879099.DATACONNECTIVITY.DC_LIVE.NCOUNTERSAREA.RUNNINGTIMECOUNTER',
    '201_FlexA5':'Line.BridgePC.TH1.RunningTimeCounter',
    '201_FlexWF':'Line.BridgePC.TSW1.RunningTimeCounter',
    '201_FlexCO':'Line.BridgePC.TC1.RunningTimeCounter',
    '201_SenzaniCP':'Senzani SBNE.CPU 315 2DP PN.Statistic_Time_Hours_RUN'
    }

def setup_connection(adr):
    client = Client(adr,timeout=60) # Make a Client
    client.set_security_string(SS) # Set Security Settings and choose ssl certificate, pub key
    client.application_uri = ('urn:opcua:python:server') # Change the client URN as the cirtificate's URN
    client.connect()
    return client

#*************************************************************************#
# Set connection with the LU 201 Combiner Line and get values of counters.#
#*************************************************************************#

try:
    client_201_itm = setup_connection(OPC_SERVER_ADR_LU201_ITM)

    data_201 = {
    '201_CT_Transp':0,'201_CT_Left':0,'201_CT_Right':0,'201_ITM_Sol':0,'201_ITM_Capricorn':0,'201_ITM_Saturn':0,'201_FlexA5':0,'201_FlexWF':0,'201_FlexCO':0,'201_SenzaniCP':0,
    }

    print('Connected to the OPC-UA server ITM COMBINER + SATURN + CAPRICORN\n')

    print('Link Up #201 Combiner Line\n')
    ctt_time = client_201_itm.get_node('ns=2; s = %s'% (tagnames_dict['201_CT_Transp'])).get_value()
    ctr_time = client_201_itm.get_node('ns=2; s = %s'% (tagnames_dict['201_CT_Right'])).get_value()
    ctl_time = client_201_itm.get_node('ns=2; s = %s'% (tagnames_dict['201_CT_Left'])).get_value()
    itm_sol_time = client_201_itm.get_node('ns=2; s = %s'% (tagnames_dict['201_ITM_Sol'])).get_value()
    itm_cap_time = client_201_itm.get_node('ns=2; s = %s'% (tagnames_dict['201_ITM_Capricorn'])).get_value()
    itm_sat_time = client_201_itm.get_node('ns=2; s = %s'% (tagnames_dict['201_ITM_Saturn'])).get_value()

    print('Cut & Turn Trasport counter is:',ctt_time,'Min.')
    print('Cut & Turn Left Module Hours-counter is:',ctt_time,'Min.')
    print('Cut & Turn Right Module Hours-Scounter is:',ctt_time,'Min.')
    print('ITM Solaris Hours-counter is:',itm_sol_time,'Min.')
    print('ITM Capriconn Hours-counter is:',itm_cap_time,'Min.')
    print('ITM Saturn Hours-counter is:',itm_sat_time,'Min.')

except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    client_201_itm.disconnect()
    print('\nDiscinnected from Comb Line!')

#******************************************************************#
# Set connection with the Packer Line and get values of counters.  #
#******************************************************************#

try:
    client_201_gima = setup_connection(OPC_SERVER_ADR_LU201_GIMA)

    print('Link Up #201 Packer Line\n')

    flexA5_time = client_201_gima.get_node('ns=2; s = %s'% (tagnames_dict['201_FlexA5'])).get_value()
    flexWF_time = client_201_gima.get_node('ns=2; s = %s'% (tagnames_dict['201_FlexWF'])).get_value()
    flexCO_time = client_201_gima.get_node('ns=2; s = %s'% (tagnames_dict['201_FlexCO'])).get_value()

    print('GIMA FlexA5 Hours-counter is:',flexA5_time,'Min.')
    print('GIMA FlexWF Hours-counter is:',flexWF_time,'Min.')
    print('GIMA FlexCO Hours-counter is:',flexCO_time,'Min.')

except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    client_201_gima.disconnect()
    print('\nDiscinnected from Pack Line!')



#*******************************************************************************#
# Set connection with the Senzani Case Packer Line and get values of counters.  #
#*******************************************************************************#

try:
    client_201_senzani = setup_connection(OPC_SERVER_ADR_LU201_SENZANI)

    print('Link Up #203 Packer Line\n')

    case_packer_time = client_201_senzani.get_node('ns=2; s = %s'% (tagnames_dict['201_SenzaniCP'])).get_value()
    print('SENZANI Case Packer Hours-counter is:',case_packer_time,'Hrs.')

except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    client_201_senzani.disconnect()
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
