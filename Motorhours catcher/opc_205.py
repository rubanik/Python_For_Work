from opcua import Client

SS = "Basic256,SignAndEncrypt,mycert1.der,key.pem"
OPC_SERVER_ADR_LU206_GD = "opc.tcp://10.143.242.102:49320"
OPC_SERVER_ADR_LU206_GIMA = "opc.tcp://10.143.242.103:49320"
OPC_SERVER_ADR_LU206_SENZANI = "opc.tcp://10.143.242.104:49320"

tagnames_dict = {
    '206_GD_Combiner':['Line.BridgePC.CMB06.mc1.RunningTimeCounter',0],
    '206_GD_CTU':['Line.BridgePC.CMB06.ctu.RunningTimeCounter',0],
    '206_FlexA5':['Line.BridgePC.TH1.RunningTimeCounter',0],
    '206_FlexWF':['Line.BridgePC.TSW1.RunningTimeCounter',0],
    '206_FlexCO':['Line.BridgePC.TC1.RunningTimeCounter',0],
    '206_SenzaniCP':['Senzani SBNE.CPU 315 2DP PN.Statistic_Time_Hours_RUN',0]
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
    client_206_GD = setup_connection(OPC_SERVER_ADR_LU206_GD)

    print('Link Up #206 Combiner Line')
    tagnames_dict['206_GD_Combiner'][1] = client_206_GD.get_node('ns=2; s = %s'% (tagnames_dict['206_GD_Combiner'][0])).get_value()
    tagnames_dict['206_GD_CTU'][1] = client_206_GD.get_node('ns=2; s = %s'% (tagnames_dict['206_GD_CTU'][0])).get_value()

except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    client_206_GD.disconnect()
    print('Discinnected from Comb Line!')

#******************************************************************#
# Set connection with the Packer Line and get values of counters.  #
#******************************************************************#

# try:
#     client_206_gima = setup_connection(OPC_SERVER_ADR_LU206_GIMA)
#
#     print('Link Up #206 Packer Line\n')
#
#     tagnames_dict['206_FlexA5'][1] = client_206_gima.get_node('ns=2; s = %s'% (tagnames_dict['206_FlexA5'][0])).get_value()
#     tagnames_dict['206_FlexWF'][1]= client_206_gima.get_node('ns=2; s = %s'% (tagnames_dict['206_FlexWF'][0])).get_value()
#     tagnames_dict['206_FlexCO'][1] = client_206_gima.get_node('ns=2; s = %s'% (tagnames_dict['206_FlexCO'][0])).get_value()
#
# except Exception as e :
#     print('An Error Ocurred!'+ str(e))
# finally:
#     client_206_gima.disconnect()
#     print('\nDiscinnected from Pack Line!')


#*******************************************************************************#
# Set connection with the Senzani Case Packer Line and get values of counters.  #
#*******************************************************************************#

try:
    client_206_senzani = setup_connection(OPC_SERVER_ADR_LU206_SENZANI)

    print('Link Up #206 Packer Line')

    tagnames_dict['206_SenzaniCP'][1] = client_206_senzani.get_node('ns=2; s = %s'% (tagnames_dict['206_SenzaniCP'][0])).get_value()

except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    client_206_senzani.disconnect()
    print('Discinnected from Case Packer Line!')

k = list(tagnames_dict.keys())
print('\nData:')
for val in k:
       print(val,tagnames_dict[val][1])


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
