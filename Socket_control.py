import socket 

def write_to_reg(address, data):
    if (data != '') and (address != '') :##--check for empty input data
        headline = bytes ([0x00, 0x03,
                               0x88, 0xA6,
                               0x1F, 0x01,
                               0x80, 0x00,
                               0x00, 0x00,
                               0x00, 0x00,
                               0x00, 0x00,
                               0x00])
    ##------check parity of input address and data-------        
        if (len(address)%2) != 0:
            address = '0' + address           
        if (len(data)%2) != 0:
            data = '0' + data
    ##------------------------------------------------
        try:
            address = bytes.fromhex(address)
        except ValueError:
            pass
        else:
            try:
                data = bytes.fromhex(data)
            except ValueError:
                pass
            else:
                if len(data) < 8:
                    data = (8 - len(data))*bytes([0x00]) + data
                packadge = headline + address + data
                clientSock.sendto(packadge,(DSPM_IP_ADDRESS, DSPM_PORT_NO))
                print(packadge.hex())######################
                print('IP назначения',   DSPM_IP_ADDRESS)##
                print('PORT назначения', DSPM_PORT_NO)#####
                print(clientSock)##########################

##=====================================================================================
##
##=====================================================================================

def read_from_reg(address):
    if (address != ''):
        headline = bytes ([0x00, 0x03,
                        0x88, 0xA6,
                        0x1F, 0x11,
                        0x80, 0x00,
                        0x00, 0x00,
                        0x00, 0x00,
                        0x00, 0x00,
                        0x00])    
        if (len(address)%2) != 0:
            address = '0' + address
        try:
            address = bytes.fromhex(address)
        except ValueError:
            return 'Проверьте правильность адреса'           
        else:    
            empty_data = bytes([0x00, 0x00,
                                0x00, 0x00,
                                0x00, 0x00,
                                0x00, 0x00])
            packadge = headline + address + empty_data
            clientSock.sendto(packadge,(DSPM_IP_ADDRESS, DSPM_PORT_NO))
            try:
                income_pack, addr = clientSock.recvfrom(1024)
            except:
                return 'Ответ не получен\nПроверьте соединение\nили правильность запроса'
            else:
                if ((bytes([income_pack[2]]) == bytes([0x88])) and
                    (bytes([income_pack[3]]) == bytes([0xA6])) and
                    ((bytes([income_pack[4]]) == bytes([0xF1])) or
                    (bytes([income_pack[4]]) == bytes([0x21])))and
                    (bytes([income_pack[5]]) == bytes([0xA5]))):
                    return income_pack
                else:
                    return 'Ответ не получен'
    else:
        return 'Пустое поле адреса'

##=====================================================================================
##
##=====================================================================================

def create_socket():
    global clientSock
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSock.setsockopt(socket.SOL_IP, IP_MTU_DISCOVER, IP_PMTUDISC_DONT)
    clientSock.bind((IP_ADDRESS, COMP_PORT_NO))
    clientSock.settimeout(0.3)

##=====================================================================================
##
##=====================================================================================

def close_socket():
	clientSock.close()

##=====================================================================================
##
##=====================================================================================

def refresh_socket():
	close_socket()
	create_socket()

##=====================================================================================
##====================initialise the firss values of ip and port=======================
##===================================================================================== 
##-----for test only-----
IP_ADDRESS      = "127.0.0.1"
DSPM_IP_ADDRESS = "127.0.0.1"
##--initialise socket--------------------
# IP_ADDRESS      = str(socket.gethostbyname(socket.getfqdn()))
# DSPM_IP_ADDRESS = "172.16.0.13"
COMP_PORT_NO    = 44203
DSPM_PORT_NO    = 65261
##--socket settings-------------------------
IP_MTU_DISCOVER   = 10
IP_PMTUDISC_DONT  = 0
clientSock        = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock.setsockopt(socket.SOL_IP, IP_MTU_DISCOVER, IP_PMTUDISC_DONT)
clientSock.bind((IP_ADDRESS, COMP_PORT_NO))
clientSock.settimeout(0.3)