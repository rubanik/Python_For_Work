from opcua import Client
import exceltest as et
import time

SS = "Basic256,SignAndEncrypt,mycert1.der,key.pem"
OPC_SERVER_ADR_LU201_ITM = "opc.tcp://10.143.242.16:49320"
OPC_SERVER_ADR_LU201_GIMA = "opc.tcp://10.143.242.17:49320"
OPC_SERVER_ADR_LU201_SENZANI = "opc.tcp://10.143.242.20:49320"
OPC_SERVER_ADR_LU202_ITM = "opc.tcp://10.143.242.18:49320"
OPC_SERVER_ADR_LU202_GIMA = "opc.tcp://10.143.242.19:49320"
OPC_SERVER_ADR_LU202_SENZANI = "opc.tcp://10.143.242.21:49320"
OPC_SERVER_ADR_LU203_ITM = "opc.tcp://10.143.242.87:49320"
OPC_SERVER_ADR_LU203_MONTRADE = "opc.tcp://10.143.242.86:49320"
OPC_SERVER_ADR_LU203_GIMA = "opc.tcp://10.143.242.88:49320"
OPC_SERVER_ADR_LU203_SENZANI = "opc.tcp://10.143.242.89:49320"
OPC_SERVER_ADR_LU204_ITM = "opc.tcp://10.143.242.91:49320"
OPC_SERVER_ADR_LU204_MONTRADE = "opc.tcp://10.143.242.90:49320"
OPC_SERVER_ADR_LU204_GIMA = "opc.tcp://10.143.242.92:49320"
OPC_SERVER_ADR_LU204_SENZANI = "opc.tcp://10.143.242.93:49320"
OPC_SERVER_ADR_LU205_GD = "opc.tcp://10.143.242.98:49320"
OPC_SERVER_ADR_LU205_GIMA = "opc.tcp://10.143.242.99:49320"
OPC_SERVER_ADR_LU205_SENZANI = "opc.tcp://10.143.242.100:49320"
OPC_SERVER_ADR_LU206_GD = "opc.tcp://10.143.242.102:49320"
OPC_SERVER_ADR_LU206_GIMA = "opc.tcp://10.143.242.103:49320"
OPC_SERVER_ADR_LU206_SENZANI = "opc.tcp://10.143.242.104:49320"
OPC_SERVER_ADR_LU207_GD = "opc.tcp://10.143.242.106:49320"
OPC_SERVER_ADR_LU207_GIMA = "opc.tcp://10.143.242.107:49320"
OPC_SERVER_ADR_LU207_SENZANI = "opc.tcp://10.143.242.108:49320"
OPC_SERVER_ADR_PLA3_MONTRADE = "opc.tcp://10.143.242.96:49320"

tagnames_dict = {
    'LU201 - Cut & Turn - Transporter':['OPC DA.CTU_810032.uPMIDataConnectivity.sNonResettableCounters.i32RunningTimeCTTransp', 0 ],
    'LU201 - Cut & Turn - Right':['OPC DA.CTU_810032.uPMIDataConnectivity.sNonResettableCounters.i32RunningTimeCTLeft', 0 ],#!!!!!!!!!!!
    'LU201 - Cut & Turn - Left':['OPC DA.CTU_810032.uPMIDataConnectivity.sNonResettableCounters.i32RunningTimeCTRight', 0 ],#!!!!!!!!!!!change left
    'LU201 - Solaris':['SOLARIS_720075.MachineData.RunningTime', 0 ],
    'LU201 - Capricorn':['TCP/IP-TwinCAT.Capricorn_21839346.DATACONNECTIVITY.DC_LIVE.NCOUNTERSAREA.RUNNINGTIMECOUNTER', 0 ],
    'LU201 - Saturn':['TCP/IP-TwinCAT.Saturn_21879099.DATACONNECTIVITY.DC_LIVE.NCOUNTERSAREA.RUNNINGTIMECOUNTER', 0 ],
    'LU201 - Gima - FlexA5':['Line.BridgePC.TH1.RunningTimeCounter', 0 ],
    'LU201 - Gima - FlexWF':['Line.BridgePC.TSW1.RunningTimeCounter', 0 ],
    'LU201 - Gima - FlexCO':['Line.BridgePC.TC1.RunningTimeCounter', 0 ],
    'LU201 - Senzani':['Senzani SBNE.CPU 315 2DP PN.Statistic_Time_Hours_RUN', 0 ],
    'LU202 - Cut & Turn - Transporter':['OPC DA.CTU_810033.uPMIDataConnectivity.sNonResettableCounters.i32RunningTimeCTTransp', 0 ],
    'LU202 - Cut & Turn - Left':['OPC DA.CTU_810033.uPMIDataConnectivity.sNonResettableCounters.i32RunningTimeCTLeft', 0 ],
    'LU202 - Cut & Turn - Right':['OPC DA.CTU_810033.uPMIDataConnectivity.sNonResettableCounters.i32RunningTimeCTRight', 0 ],
    'LU202 - Solaris':['SOLARIS_720082.MachineData.RunningTime', 0 ],
    'LU202 - Capricorn':['TCP/IP-TwinCAT.Capricorn_21839351.DATACONNECTIVITY.DC_LIVE.NCOUNTERSAREA.RUNNINGTIMECOUNTER', 0 ],
    'LU202 - Saturn':['TCP/IP-TwinCAT.Saturn_21879100.DATACONNECTIVITY.DC_LIVE.NCOUNTERSAREA.RUNNINGTIMECOUNTER', 0 ],
    'LU202 - Gima - FlexA5':['Line.BridgePC.TH1.RunningTimeCounter', 0 ],
    'LU202 - Gima - FlexWF':['Line.BridgePC.TSW1.RunningTimeCounter', 0 ],
    'LU202 - Gima - FlexCO':['Line.BridgePC.TC1.RunningTimeCounter', 0 ],
    'LU202 - Senzani':['Senzani SBNE.CPU 315 2DP PN.Statistic_Time_Hours_RUN', 0 ],
    'LU203 - Cut & Turn - Transporter':['OPC DA.CTU_810035.0SYM:.CT_810035.CTU_810035.uPMIDataConnectivity.sNonResettableCounters.i32RunningTimeCTTransp', 0 ],
    'LU203 - Cut & Turn - Left':['OPC DA.CTU_810035.0SYM:.CT_810035.CTU_810035.uPMIDataConnectivity.sNonResettableCounters.i32RunningTimeCTLeft', 0 ],
    'LU203 - Cut & Turn - Right':['OPC DA.CTU_810035.0SYM:.CT_810035.CTU_810035.uPMIDataConnectivity.sNonResettableCounters.i32RunningTimeCTRight', 0 ],
    'LU203 - Solaris':['SOLARIS_720083.MachineData.RunningTime', 0 ],
    'LU203 - Capricorn':['TCP/IP-TwinCAT.Capricorn_21839352.DATACONNECTIVITY.DC_LIVE.NCOUNTERSAREA.RUNNINGTIMECOUNTER', 0 ],
    'LU203 - Saturn':['TCP/IP-TwinCAT.Saturn_21879107.DATACONNECTIVITY.DC_LIVE.NCOUNTERSAREA.RUNNINGTIMECOUNTER', 0 ],
    'LU203 - Montrade - Crimper':['Line.BridgePC.CRIMPER.WMSK.COUNTERABSOLUTEWORKHOURS',0],#!
    'LU203 - Gima - FlexA5':['Line.BridgePC.TH1.RunningTimeCounter', 0 ],
    'LU203 - Gima - FlexWF':['Line.BridgePC.TSW1.RunningTimeCounter', 0 ],
    'LU203 - Gima - FlexCO':['Line.BridgePC.TC1.RunningTimeCounter', 0 ],
    'LU203 - Senzani':['Senzani SBNE.CPU 315 2DP PN.Statistic_Time_Hours_RUN', 0 ],
    'LU204 - Cut & Turn - Transporter':['OPC DA.CTU_810036.sNonResettableCounters.i32RunningTimeCTTransp', 0 ],
    'LU204 - Cut & Turn - Left':['OPC DA.CTU_810036.sNonResettableCounters.i32RunningTimeCTLeft', 0 ],
    'LU204 - Cut & Turn - Right':['OPC DA.CTU_810036.sNonResettableCounters.i32RunningTimeCTRight', 0 ],
    'LU204 - Solaris':['SOLARIS_720084.MachineData.RunningTime', 0 ],
    'LU204 - Capricorn':['TCP/IP-TwinCAT.Capricorn_21839353.DATACONNECTIVITY.DC_LIVE.NCOUNTERSAREA.RUNNINGTIMECOUNTER', 0 ],
    'LU204 - Saturn':['TCP/IP-TwinCAT.Saturn_21879108.DATACONNECTIVITY.DC_LIVE.NCOUNTERSAREA.RUNNINGTIMECOUNTER', 0 ],
    'LU204 - Montrade - Crimper':['Line.BridgePC.CRIMPER.WMSK.COUNTERABSOLUTEWORKHOURS',0],#!
    'LU204 - Gima - FlexA5':['Line.BridgePC.TH1.RunningTimeCounter', 0 ],
    'LU204 - Gima - FlexWF':['Line.BridgePC.TSW1.RunningTimeCounter', 0 ],
    'LU204 - Gima - FlexCO':['Line.BridgePC.TC1.RunningTimeCounter', 0 ],
    'LU204 - Senzani':['Senzani SBNE.CPU 315 2DP PN.Statistic_Time_Hours_RUN', 0 ],
    'LU205 - GD - Combiner':['GD.1.CMB05.mc1.RunningTimeCounter',0],
    'LU205 - GD - CTU':['GD.1.CMB05.ctu.RunningTimeCounter',0],
    'LU205 - Gima - FlexA5':['Line.BridgePC.TH1.RunningTimeCounter',0],
    'LU205 - Gima - FlexWF':['Line.BridgePC.TSW1.RunningTimeCounter',0],
    'LU205 - Gima - FlexCO':['Line.BridgePC.TC1.RunningTimeCounter',0],
    'LU205 - Senzani':['Senzani SBNE.CPU 315 2DP PN.Statistic_Time_Hours_RUN',0],
    'LU206 - GD - Combiner':['Line.BridgePC.CMB06.mc1.RunningTimeCounter',0],
    'LU206 - GD - CTU':['Line.BridgePC.CMB06.ctu.RunningTimeCounter',0],
    'LU206 - Gima - FlexA5':['Line.BridgePC.TH1.RunningTimeCounter',0],
    'LU206 - Gima - FlexWF':['Line.BridgePC.TSW1.RunningTimeCounter',0],
    'LU206 - Gima - FlexCO':['Line.BridgePC.TC1.RunningTimeCounter',0],
    'LU206 - Senzani':['Senzani SBNE.CPU 315 2DP PN.Statistic_Time_Hours_RUN',0],
    'LU207 - GD - Combiner':['Line.BridgePC.CMB07.mc1.RunningTimeCounter',0],
    'LU207 - GD - CTU':['Line.BridgePC.CMB07.ctu.RunningTimeCounter',0],
    'LU207 - Gima - FlexA5':['Line.BridgePC.TH1.RunningTimeCounter',0],
    'LU207 - Gima - FlexWF':['Line.BridgePC.TSW1.RunningTimeCounter',0],
    'LU207 - Gima - FlexCO':['Line.BridgePC.TC1.RunningTimeCounter',0],
    'LU207 - Senzani':['Senzani SBNE.CPU 315 2DP PN.Statistic_Time_Hours_RUN',0],
    'PLA3 - Montrade':['Line.BridgePC.CRIMPER.WMSK.COUNTERABSOLUTEWORKHOURS',0]
    }

print('*****   Программа Сбора данных о моточасах оборудования цеха RRP   *****')
print('*****   Для корректной работы программы, на пк должен быть доступ к BridgePC   *****\n')

def setup_connection(adr):
    try:
        client = Client(adr,timeout=60) # Make a Client
        client.set_security_string(SS) # Set Security Settings and choose ssl certificate, pub key
        client.application_uri = ('urn:opcua:python:server') # Change the client URN as the cirtificate's URN
        client.connect()
        return client
    except Exception as e:
        print(e)
        return None


def disconnect(client):
    try:
        if client:
            client.disconnect()
    except Exception as e:
        print(e)

print('Сбор данных...')


##########
# LU 201 #
##########
print('Step 1: Getting data from LU201 OPC...')

#*************************************************************************#
# Set connection with the LU 201 Combiner Line and get values of counters.#
#*************************************************************************#

try:
    client_201_itm = setup_connection(OPC_SERVER_ADR_LU201_ITM)
    if client_201_itm:
        tagnames_dict['LU201 - Cut & Turn - Transporter'][1] = client_201_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU201 - Cut & Turn - Transporter'][0])).get_value()//60
        tagnames_dict['LU201 - Cut & Turn - Right'][1] = client_201_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU201 - Cut & Turn - Right'][0])).get_value()//60
        tagnames_dict['LU201 - Cut & Turn - Left'][1] = client_201_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU201 - Cut & Turn - Left'][0])).get_value()//60
        tagnames_dict['LU201 - Solaris'][1] = client_201_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU201 - Solaris'][0])).get_value()//60
        tagnames_dict['LU201 - Capricorn'][1] = client_201_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU201 - Capricorn'][0])).get_value()//60
        tagnames_dict['LU201 - Saturn'][1] = client_201_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU201 - Saturn'][0])).get_value()//60
except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    disconnect(client_201_itm)

#******************************************************************#
# Set connection with the Packer Line and get values of counters.  #
#******************************************************************#

try:
    client_201_gima = setup_connection(OPC_SERVER_ADR_LU201_GIMA)
    if client_201_gima:
        tagnames_dict['LU201 - Gima - FlexA5'][1] = client_201_gima.get_node('ns=2; s = %s'% (tagnames_dict['LU201 - Gima - FlexA5'][0])).get_value()
        tagnames_dict['LU201 - Gima - FlexWF'][1] = client_201_gima.get_node('ns=2; s = %s'% (tagnames_dict['LU201 - Gima - FlexWF'][0])).get_value()
        tagnames_dict['LU201 - Gima - FlexCO'][1] = client_201_gima.get_node('ns=2; s = %s'% (tagnames_dict['LU201 - Gima - FlexCO'][0])).get_value()
except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    disconnect(client_201_gima)

#*******************************************************************************#
# Set connection with the Senzani Case Packer Line and get values of counters.  #
#*******************************************************************************#

try:
    client_201_senzani = setup_connection(OPC_SERVER_ADR_LU201_SENZANI)
    if client_201_senzani:
        tagnames_dict['LU201 - Senzani'][1] = client_201_senzani.get_node('ns=2; s = %s'% (tagnames_dict['LU201 - Senzani'][0])).get_value()
except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    disconnect(client_201_senzani)


##########
# LU 203 #
##########
print('Step 2: Getting data from LU202 OPC...')
#*************************************************************************#
# Set connection with the LU 202 Combiner Line and get values of counters.#
#*************************************************************************#

try:
    client_202_itm = setup_connection(OPC_SERVER_ADR_LU202_ITM)

    if client_202_itm:
        tagnames_dict['LU202 - Cut & Turn - Transporter'][1]= client_202_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU202 - Cut & Turn - Transporter'][0])).get_value()//60
        tagnames_dict['LU202 - Cut & Turn - Right'][1] = client_202_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU202 - Cut & Turn - Right'][0])).get_value()//60
        tagnames_dict['LU202 - Cut & Turn - Left'][1] = client_202_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU202 - Cut & Turn - Left'][0])).get_value()//60
        tagnames_dict['LU202 - Solaris'][1] = client_202_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU202 - Solaris'][0])).get_value()//60
        tagnames_dict['LU202 - Capricorn'][1] = client_202_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU202 - Capricorn'][0])).get_value()//60
        tagnames_dict['LU202 - Saturn'][1] = client_202_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU202 - Saturn'][0])).get_value()//60

except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    disconnect(client_202_itm)

#******************************************************************#
# Set connection with the Packer Line and get values of counters.  #
#******************************************************************#

try:
    client_202_gima = setup_connection(OPC_SERVER_ADR_LU202_GIMA)
    if client_202_gima:
        tagnames_dict['LU202 - Gima - FlexA5'][1] = client_202_gima.get_node('ns=2; s = %s'% (tagnames_dict['LU202 - Gima - FlexA5'][0])).get_value()
        tagnames_dict['LU202 - Gima - FlexWF'][1] = client_202_gima.get_node('ns=2; s = %s'% (tagnames_dict['LU202 - Gima - FlexWF'][0])).get_value()
        tagnames_dict['LU202 - Gima - FlexCO'][1] = client_202_gima.get_node('ns=2; s = %s'% (tagnames_dict['LU202 - Gima - FlexCO'][0])).get_value()
    #
    # print('GIMA FlexA5 Hours-counter is:',flexA5_time,'Min.')
    # print('GIMA FlexWF Hours-counter is:',flexWF_time,'Min.')
    # print('GIMA FlexCO Hours-counter is:',flexCO_time,'Min.')

except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    disconnect(client_202_gima)

#*******************************************************************************#
# Set connection with the Senzani Case Packer Line and get values of counters.  #
#*******************************************************************************#

try:
    client_202_senzani = setup_connection(OPC_SERVER_ADR_LU202_SENZANI)
    if client_202_senzani:
        tagnames_dict['LU202 - Senzani'][1] = client_202_senzani.get_node('ns=2; s = %s'% (tagnames_dict['LU202 - Senzani'][0])).get_value()
    # print('SENZANI Case Packer Hours-counter is:',case_packer_time,'Hrs.')

except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    disconnect(client_202_senzani)

# ##########
# # LU 203 #
# ##########
# print('Step 3: Getting data from LU203 OPC...')
# #*************************************************************************#
# # Set connection with the LU 203 Combiner Line and get values of counters.#
# #*************************************************************************#

# try:
    # client_203_itm = setup_connection(OPC_SERVER_ADR_LU203_ITM)

    # if client_203_itm:
        # tagnames_dict['LU203 - Cut & Turn - Transporter'][1] = client_203_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU203 - Cut & Turn - Transporter'][0])).get_value()//60
        # tagnames_dict['LU203 - Cut & Turn - Right'][1] = client_203_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU203 - Cut & Turn - Right'][0])).get_value()//60
        # tagnames_dict['LU203 - Cut & Turn - Left'][1] = client_203_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU203 - Cut & Turn - Left'][0])).get_value()//60
        # tagnames_dict['LU203 - Solaris'][1] = client_203_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU203 - Solaris'][0])).get_value()//60
        # tagnames_dict['LU203 - Capricorn'][1] = client_203_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU203 - Capricorn'][0])).get_value()//60
        # tagnames_dict['LU203 - Saturn'][1] = client_203_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU203 - Saturn'][0])).get_value()//60

# except Exception as e :
    # print('An Error Ocurred!'+ str(e))
# finally:
    # disconnect(client_203_itm)


# #Crimper

# try:
    # client_203_montrade = setup_connection(OPC_SERVER_ADR_LU203_MONTRADE)

    # if client_203_montrade:
        # tagnames_dict['LU203 - Montrade - Crimper'][1] = client_203_montrade.get_node('ns=2; s = %s'% (tagnames_dict['LU203 - Montrade - Crimper'][0])).get_value()

# except Exception as e :
    # print('An Error Ocurred!'+ str(e))
# finally:
    # disconnect(client_203_montrade)


# # Set connection with the Packer Line and get values of counters.
# try:
    # client_203_gima = setup_connection(OPC_SERVER_ADR_LU203_GIMA)
    # if client_203_gima:
        # tagnames_dict['LU203 - Gima - FlexA5'][1] = client_203_gima.get_node('ns=2; s = %s'% (tagnames_dict['LU203 - Gima - FlexA5'][0])).get_value()
        # tagnames_dict['LU203 - Gima - FlexWF'][1] = client_203_gima.get_node('ns=2; s = %s'% (tagnames_dict['LU203 - Gima - FlexWF'][0])).get_value()
        # tagnames_dict['LU203 - Gima - FlexCO'][1] = client_203_gima.get_node('ns=2; s = %s'% (tagnames_dict['LU203 - Gima - FlexCO'][0])).get_value()
# except Exception as e :
    # print('An Error Ocurred!'+ str(e))
# finally:
    # disconnect(client_203_gima)

# #*******************************************************************************#
# # Set connection with the Senzani Case Packer Line and get values of counters.  #
# #*******************************************************************************#

# try:
    # client_203_senzani = setup_connection(OPC_SERVER_ADR_LU203_SENZANI)

    # if client_203_senzani:
        # tagnames_dict['LU203 - Senzani'][1] = client_203_senzani.get_node('ns=2; s = %s'% (tagnames_dict['LU203 - Senzani'][0])).get_value()

# except Exception as e :
    # print('An Error Ocurred!'+ str(e))
# finally:
    # disconnect(client_203_senzani)
    # #print('__________Discinnected from Case Packer Line!__________\n')


# ##########
# # LU 204 #
# ##########
# print('Step 4: Getting data from LU204 OPC...')

# #*************************************************************************#
# # Set connection with the LU 204 Combiner Line and get values of counters.#
# #*************************************************************************#

# try:
    # client_204_itm = setup_connection(OPC_SERVER_ADR_LU204_ITM)

    # if client_204_itm:
        # tagnames_dict['LU204 - Cut & Turn - Transporter'][1] = client_204_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU204 - Cut & Turn - Transporter'][0])).get_value()//60
        # tagnames_dict['LU204 - Cut & Turn - Right'][1] = client_204_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU204 - Cut & Turn - Right'][0])).get_value()//60
        # tagnames_dict['LU204 - Cut & Turn - Left'][1] = client_204_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU204 - Cut & Turn - Left'][0])).get_value()//60
        # tagnames_dict['LU204 - Solaris'][1] = client_204_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU204 - Solaris'][0])).get_value()//60
        # tagnames_dict['LU204 - Capricorn'][1] = client_204_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU204 - Capricorn'][0])).get_value()//60
        # tagnames_dict['LU204 - Saturn'][1] = client_204_itm.get_node('ns=2; s = %s'% (tagnames_dict['LU204 - Saturn'][0])).get_value()//60

# except Exception as e :
    # print('An Error Ocurred!'+ str(e))
# finally:
    # disconnect(client_204_itm)
    # #print('\nDiscinnected from Comb Line!')

# #Crimper

# try:
    # client_204_montrade = setup_connection(OPC_SERVER_ADR_LU204_MONTRADE)
    # if client_204_montrade:
        # tagnames_dict['LU204 - Montrade - Crimper'][1] = client_204_montrade.get_node('ns=2; s = %s'% (tagnames_dict['LU204 - Montrade - Crimper'][0])).get_value()
# except Exception as e :
    # print('An Error Ocurred!'+ str(e))
# finally:
    # disconnect(client_204_montrade)


# #******************************************************************#
# # Set connection with the Packer Line and get values of counters.  #
# #******************************************************************#

# try:
    # client_204_gima = setup_connection(OPC_SERVER_ADR_LU204_GIMA)

    # if client_204_gima:
        # tagnames_dict['LU204 - Gima - FlexA5'][1] = client_204_gima.get_node('ns=2; s = %s'% (tagnames_dict['LU204 - Gima - FlexA5'][0])).get_value()
        # tagnames_dict['LU204 - Gima - FlexWF'][1] = client_204_gima.get_node('ns=2; s = %s'% (tagnames_dict['LU204 - Gima - FlexWF'][0])).get_value()
        # tagnames_dict['LU204 - Gima - FlexCO'][1] = client_204_gima.get_node('ns=2; s = %s'% (tagnames_dict['LU204 - Gima - FlexCO'][0])).get_value()

# except Exception as e :
    # print('An Error Ocurred!'+ str(e))
# finally:
    # disconnect(client_204_gima)

# #*******************************************************************************#
# # Set connection with the Senzani Case Packer Line and get values of counters.  #
# #*******************************************************************************#

# try:
    # client_204_senzani = setup_connection(OPC_SERVER_ADR_LU204_SENZANI)

    # if client_204_senzani:
        # tagnames_dict['LU204 - Senzani'][1] = client_204_senzani.get_node('ns=2; s = %s'% (tagnames_dict['LU204 - Senzani'][0])).get_value()
# except Exception as e :
    # print('An Error Ocurred!'+ str(e))
# finally:
    # disconnect(client_204_senzani)
    
    
    # ЗАКОМЕНТИЛ ТК НЕ РАБОТАЮТ ЛИНИИ

##########
# LU 205 #
##########
print('Step 5: Getting data from LU205 OPC...')
#*************************************************************************#
# Set connection with the LU 201 Combiner Line and get values of counters.#
#*************************************************************************#

try:
    client_205_GD = setup_connection(OPC_SERVER_ADR_LU205_GD)

    if client_205_GD:
        tagnames_dict['LU205 - GD - Combiner'][1] = client_205_GD.get_node('ns=2; s = %s'% (tagnames_dict['LU205 - GD - Combiner'][0])).get_value()
        tagnames_dict['LU205 - GD - CTU'][1] = client_205_GD.get_node('ns=2; s = %s'% (tagnames_dict['LU205 - GD - CTU'][0])).get_value()

except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    disconnect(client_205_GD)
    #print('\nDiscinnected from Comb Line!')

#******************************************************************#
# Set connection with the Packer Line and get values of counters.  #
#******************************************************************#

try:
    client_205_gima = setup_connection(OPC_SERVER_ADR_LU205_GIMA)

    if client_205_gima:
        tagnames_dict['LU205 - Gima - FlexA5'][1] = client_205_gima.get_node('ns=2; s = %s'% (tagnames_dict['LU205 - Gima - FlexA5'][0])).get_value()
        tagnames_dict['LU205 - Gima - FlexWF'][1]= client_205_gima.get_node('ns=2; s = %s'% (tagnames_dict['LU205 - Gima - FlexWF'][0])).get_value()
        tagnames_dict['LU205 - Gima - FlexCO'][1] = client_205_gima.get_node('ns=2; s = %s'% (tagnames_dict['LU205 - Gima - FlexCO'][0])).get_value()

except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    disconnect(client_205_gima)

#*******************************************************************************#
# Set connection with the Senzani Case Packer Line and get values of counters.  #
#*******************************************************************************#

try:
    client_205_senzani = setup_connection(OPC_SERVER_ADR_LU205_SENZANI)
    if client_205_senzani:
        tagnames_dict['LU205 - Senzani'][1] = client_205_senzani.get_node('ns=2; s = %s'% (tagnames_dict['LU205 - Senzani'][0])).get_value()

except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    disconnect(client_205_senzani)
    #print('\nDiscinnected from Case Packer Line!')

##########
# LU 206 #
##########
print('Step 6: Getting data from LU206 OPC...')
#*************************************************************************#
# Set connection with the LU 201 Combiner Line and get values of counters.#
#*************************************************************************#

try:
    client_206_GD = setup_connection(OPC_SERVER_ADR_LU206_GD)

    if client_206_GD:
        tagnames_dict['LU206 - GD - Combiner'][1] = client_206_GD.get_node('ns=2; s = %s'% (tagnames_dict['LU206 - GD - Combiner'][0])).get_value()
        tagnames_dict['LU206 - GD - CTU'][1] = client_206_GD.get_node('ns=2; s = %s'% (tagnames_dict['LU206 - GD - CTU'][0])).get_value()

except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    disconnect(client_206_GD)
    #print('Discinnected from Comb Line!')

#******************************************************************#
# Set connection with the Packer Line and get values of counters.  #
#******************************************************************#

try:
    client_206_gima = setup_connection(OPC_SERVER_ADR_LU206_GIMA)

    if client_206_gima:
        tagnames_dict['LU206 - Gima - FlexA5'][1] = client_206_gima.get_node('ns=2; s = %s'% (tagnames_dict['LU206 - Gima - FlexA5'][0])).get_value()
        tagnames_dict['LU206 - Gima - FlexWF'][1]= client_206_gima.get_node('ns=2; s = %s'% (tagnames_dict['LU206 - Gima - FlexWF'][0])).get_value()
        tagnames_dict['LU206 - Gima - FlexCO'][1] = client_206_gima.get_node('ns=2; s = %s'% (tagnames_dict['LU206 - Gima - FlexCO'][0])).get_value()

except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    disconnect(client_206_gima)


#*******************************************************************************#
# Set connection with the Senzani Case Packer Line and get values of counters.  #
#*******************************************************************************#

try:
    client_206_senzani = setup_connection(OPC_SERVER_ADR_LU206_SENZANI)
    if client_206_senzani:
        tagnames_dict['LU206 - Senzani'][1] = client_206_senzani.get_node('ns=2; s = %s'% (tagnames_dict['LU206 - Senzani'][0])).get_value()

except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    disconnect(client_206_senzani)

##########
# LU 207 #
##########
print('Step 7: Getting data from LU207 OPC...')
#*************************************************************************#
# Set connection with the LU 207 Combiner Line and get values of counters.#
#*************************************************************************#

try:
    client_207_GD = setup_connection(OPC_SERVER_ADR_LU207_GD)

    if client_207_GD:
        tagnames_dict['LU207 - GD - Combiner'][1] = client_207_GD.get_node('ns=2; s = %s'% (tagnames_dict['LU207 - GD - Combiner'][0])).get_value()
        tagnames_dict['LU207 - GD - CTU'][1] = client_207_GD.get_node('ns=2; s = %s'% (tagnames_dict['LU207 - GD - CTU'][0])).get_value()

except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    disconnect(client_207_GD)
    #print('Discinnected from Comb Line!')

#******************************************************************#
# Set connection with the Packer Line and get values of counters.  #
#******************************************************************#

try:
    client_207_gima = setup_connection(OPC_SERVER_ADR_LU207_GIMA)

    if client_207_gima:
        tagnames_dict['LU207 - Gima - FlexA5'][1] = client_207_gima.get_node('ns=2; s = %s'% (tagnames_dict['LU207 - Gima - FlexA5'][0])).get_value()
        tagnames_dict['LU207 - Gima - FlexWF'][1]= client_207_gima.get_node('ns=2; s = %s'% (tagnames_dict['LU207 - Gima - FlexWF'][0])).get_value()
        tagnames_dict['LU207 - Gima - FlexCO'][1] = client_207_gima.get_node('ns=2; s = %s'% (tagnames_dict['LU207 - Gima - FlexCO'][0])).get_value()

except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    disconnect(client_207_gima)

#*******************************************************************************#
# Set connection with the Senzani Case Packer Line and get values of counters.  #
#*******************************************************************************#
try:
    client_207_senzani = setup_connection(OPC_SERVER_ADR_LU207_SENZANI)
    if client_207_senzani:
        tagnames_dict['LU207 - Senzani'][1] = client_207_senzani.get_node('ns=2; s = %s'% (tagnames_dict['LU207 - Senzani'][0])).get_value()

except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    disconnect(client_207_senzani)
    #print('Discinnected from Case Packer Line!')

#Crimper PLA3
try:
    client_pla3_montrade = setup_connection(OPC_SERVER_ADR_PLA3_MONTRADE)

    if client_pla3_montrade:
        tagnames_dict['PLA3 - Montrade'][1] = client_pla3_montrade.get_node('ns=2; s = %s'% (tagnames_dict['PLA3 - Montrade'][0])).get_value()
except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    disconnect(client_pla3_montrade)

try:

    
    print('\nData:')
    k = list(tagnames_dict.keys())
    zeroPresence = 0
    i=1
    for val in k:
        print(i,val,tagnames_dict[val][1])
        i+=1
        if tagnames_dict[val][1] == 0 and not zeroPresence:
            zeroPresence = 1

    if zeroPresence:
        print('Zero Values are in array')
        zeroPresence = 0
        
except Exception as e :
    print('An Error while Printer!'+ str(e))

    

et.saveToExcell(tagnames_dict)

time.sleep(3)
