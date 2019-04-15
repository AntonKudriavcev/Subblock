
from kivy.uix.screenmanager import Screen

import socket 

import Socket_control
import global_values

class SETTING(Screen):
    def __init__(self, **kw):
        super(SETTING, self).__init__(**kw)
        self.ids.reconf.text  = 'Применить новый IP-адрес и порт'
        ip_list = []
        for i in socket.gethostbyname_ex(socket.getfqdn())[2]:
        	ip_list.append(' ' + i)
        self.ids.COMP_IP.values = ip_list
        self.ids.COMP_IP.text   = ip_list[0]
    def reconfig(self):
        Socket_control.close_socket()
        Socket_control.IP_ADDRESS = str(self.ids.COMP_IP.text)[1:]
        Socket_control.create_socket()

        DSPM_IP_ADDRESS = self.ids.IP_DSPM.text
        DSPM_PORT_NO    = self.ids.PORT_DSPM.text
        ##------check correct DSPM_IP_ADDRESS and DSPM_PORT_NO-----
        try:
            Socket_control.clientSock.sendto(bytes("", 'utf-8'),(str(DSPM_IP_ADDRESS), int(DSPM_PORT_NO)))
        except:
            print('alarm')
        else:
            Socket_control.DSPM_IP_ADDRESS = str(DSPM_IP_ADDRESS)
            Socket_control.DSPM_PORT_NO    = int(DSPM_PORT_NO)

##=====================================================================================
##==========================when moving to TEMP window=================================
##=====================================================================================

    def cont_drawing(self):
        if global_values.pause == False:
            global_values.start_stop = True

##=====================================================================================
##
##=====================================================================================

    def socket_close(self):
        Socket_control.close_socket()
       