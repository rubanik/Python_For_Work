from opcua import Client

SS = "Basic256,SignAndEncrypt,mycert1.der,key.pem"
OPC_SERVER_ADR_LU204_SENZANI = "opc.tcp://10.143.242.93:49320"

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
    'SenzaniCP':'Senzani SBNE.CPU 315 2DP PN.Statistic_Time_Hours_RUN'
    }

def setup_connection(adr):
    client = Client(adr,timeout=60) # Make a Client
    client.set_security_string(SS) # Set Security Settings and choose ssl certificate, pub key
    client.application_uri = ('urn:opcua:python:server') #Change the client URN as the cirtificate's URN
    client.connect()
    return client


try:
    client_senzani = setup_connection(OPC_SERVER_ADR_LU204_SENZANI)
    
    print('Link Up #204 Packer Line\n')

    case_packer_time = client_senzani.get_node('ns=2; s = %s'% (tagnames_dict['SenzaniCP'])).get_value()
    print('SENZANI Case Packer Hours-counter is:',case_packer_time,'Hrs.')
    
except Exception as e :
    print('An Error Ocurred!'+ str(e))
finally:
    client_senzani.disconnect()
    print('\nDiscinnected from Pack Line!')
