
from   kivy.uix.screenmanager import Screen

import Socket_control
import global_values

class BOOTLOADER_SETTINGS(Screen):
    def __init__(self,**kw):
        super(BOOTLOADER_SETTINGS,self).__init__(**kw)
        self.ids.request.text          = ' Запросить данные из'+'\n'+'  прочитанного файла'
        self.ids.request_from_reg.text = ' Запросить данные из'+'\n'+'           регистров'

##=====================================================================================
##=========================when moving to TEMP window==================================
##=====================================================================================

    def cont_drawing(self):
        if global_values.pause == False:
            global_values.start_stop = True 

##=====================================================================================
##
##=====================================================================================

    def reconf_FPGA(self, address, data):
        Socket_control.create_socket()
        Socket_control.write_to_reg(address, data)
        if address   == '04':
        	Socket_control.write_to_reg('05', '01')
        elif address == '24':
        	Socket_control.write_to_reg('25', '01')
        elif address == '4C':
        	Socket_control.write_to_reg('4D', '01')   
        Socket_control.close_socket()

##=====================================================================================
##
##=====================================================================================

    def apply(self, data_1, data_2, data_3):
        self.reconf_FPGA('04', data_1)
        self.reconf_FPGA('24', data_2)
        self.reconf_FPGA('4C', data_3)   

##=====================================================================================
##
##=====================================================================================

    def request(self):
        self.ids.reconfiguration_04.text  = global_values.BOOTLOADER_SETTINGS_FPGA_1
        self.ids.reconfiguration_24.text  = global_values.BOOTLOADER_SETTINGS_FPGA_2
        self.ids.reconfiguration_04C.text = global_values.BOOTLOADER_SETTINGS_FPGA_3

##=====================================================================================
##
##=====================================================================================

    def request_from_reg(self):
        Socket_control.create_socket()
        packadge = Socket_control.read_from_reg('04')
        try:
            self.ids.reconfiguration_04.text = str(packadge[20:24].hex())
        except AttributeError:
            pass

        packadge = Socket_control.read_from_reg('24')
        try:
            self.ids.reconfiguration_24.text = str(packadge[20:24].hex())
        except AttributeError:
            pass

        packadge = Socket_control.read_from_reg('4C')
        try:
            self.ids.reconfiguration_04C.text = str(packadge[20:24].hex())
        except AttributeError:
            pass
        Socket_control.close_socket()

##=====================================================================================
##
##=====================================================================================

    def reset(self):
        Socket_control.create_socket()
        Socket_control.write_to_reg('00', '01')
        Socket_control.close_socket()

##=====================================================================================
##==========================when moving to another window==============================
##=====================================================================================

    def reconf_all(self):  
        global_values.BOOTLOADER_SETTINGS_FPGA_1 = self.ids.reconfiguration_04.text  
        global_values.BOOTLOADER_SETTINGS_FPGA_2 = self.ids.reconfiguration_24.text
        global_values.BOOTLOADER_SETTINGS_FPGA_3 = self.ids.reconfiguration_04C.text
        Socket_control.create_socket()


