from kivy.uix.screenmanager import Screen

import Socket_control
import global_values

class READ_AND_WRITE(Screen):
    def __init__(self, **kw):
        super(READ_AND_WRITE, self).__init__(**kw) 

##=====================================================================================
##
##===================================================================================== 

    def read(self):      
        address = self.ids.address.text
        inf = Socket_control.read_from_reg(address)
        try:
            self.ids.income_data.text = str(inf.hex())
        except AttributeError:
            self.ids.income_data.text = inf

##=====================================================================================
##
##=====================================================================================

    def write(self):     
        address = self.ids.address.text
        data    = self.ids.data.text
        Socket_control.write_to_reg(address,data)

##=====================================================================================
##=============================when moving to TEMP window==============================
##=====================================================================================

    def cont_drawing(self):
        if global_values.pause == False:
            global_values.start_stop = True

##=====================================================================================
##
##=====================================================================================

    def socket_close(self):
        Socket_control.close_socket()
