from opcua import Client

SS = "Basic256,SignAndEncrypt,mycert1.der,key.pem"
OPC_SERVER_ADR_LU204_GIMA = "opc.tcp://10.143.242.92:49320"

tagnames_dict = {
    'CT_Transp':'OPC DA.CTU_810036.sNonResettableCounters.i32RunningTimeCTTransp',
    'CT_Left':'OPC DA.CTU_810036.sNonResettableCounters.i32RunningTimeCTLeft',
    'CT_Right':'OPC DA.CTU_810036.sNonResettableCounters.i32RunningTimeCTRight',
    'ITM_Sol':'SOLARIS_720084.MachineData.RunningTime',
    'ITM_Capricorn':'TCP/IP-TwinCAT.Capricorn_21839353.DATACONNECTIVITY.DC_LIVE.NCOUNTERSAREA.RUNNINGTIMECOUNTER',
    'ITM_Saturn':'TCP/IP-TwinCAT.Saturn_21879108.DATACONNECTIVITY.DC_LIVE.NCOUNTERSAREA.RUNNINGTIMECOUNTER',
    'FlexA5':'Line.BridgePC.TH1.RunningTimeCounter',
    'FlexWF':'Line.BridgePC.TSW1.RunningTimeCounter',
    'FlexCO':'Line.BridgePC.TC1.RunningTimeCounter',
    }

def setup_connection(adr):
    client = Client(adr,timeout=60) # Make a Client
    client.set_security_string(SS) # Set Security Settings and choose ssl certificate, pub key
    client.application_uri = ('urn:opcua:python:server') #Change the client URN as the cirtificate's URN
    client.connect()
    return client

try:
    client_gima = setup_connection(OPC_SERVER_ADR_LU204_GIMA)
    
    print('Link Up #204 Packer Line\n')

    flexA5_time = client_gima.get_node('ns=2; s = %s'% (tagnames_dict['FlexA5'])).get_value()
    flexWF_time = client_gima.get_node('ns=2; s = %s'% (tagnames_dict['FlexWF'])).get_value()
    flexCO_time = client_gima.get_node('ns=2; s = %s'% (tagnames_dict['FlexCO'])).get_value()
    
    print('GIMA FlexA5 Hours-counter is:',flexA5_time,'Min.')
    print('GIMA FlexWF Hours-counter is:',flexWF_time,'Min.')
    print('GIMA FlexCO Hours-counter is:',flexCO_time,'Min.')
    
except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    client_gima.disconnect()
    print('\nDiscinnected from Pack Line!')
