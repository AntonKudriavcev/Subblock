from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.garden.graph      import LinePlot
from kivy.clock             import Clock

import time

from   log import txt_creator
import global_values

import Socket_control
import get_temperature_level

class TEMPERATURE(Screen):
    def __init__(self, **kw):
        super(TEMPERATURE, self).__init__(**kw)       
        self.graph_1 = LinePlot(line_width = 1.2, color = [.62,.93,.25,1])
        self.graph_2 = LinePlot(line_width = 1.2, color = [.31,.42,.96,1])
        self.graph_3 = LinePlot(line_width = 1.2, color = [.96,.46,.21,1])           
        self.ids.graph.add_plot(self.graph_1)
        self.ids.graph.add_plot(self.graph_2)
        self.ids.graph.add_plot(self.graph_3)

##=====================================================================================
##
##=====================================================================================

    def start_stop(self,start_control):
        if start_control.state == 'down': 
            global_values.pause = False##------message for other screens
            global_values.start_stop = True##--message for thread                
            self.ids.switch.touch_control = False
            if self.ids.switch.active == True:
                global_values.write_to_file = True
                global_values.time_of_creation = str(time.strftime('%d.%m.%Y_h%Hm%Ms%S'))
                global_values.time_of_start    = time.perf_counter()               
                txt_creator()                
            else:
                global_values.write_to_file = False
            self.ids.start_control.text = 'СТОП'
            Clock.schedule_interval(self.get_value_1, 0.001)
            Clock.schedule_interval(self.get_value_2, 0.001)
            Clock.schedule_interval(self.get_value_3, 0.001)       
        else:
            global_values.pause      = True
            global_values.start_stop = False 
            global_values.FPGA_TEMPER_1.clear()
            global_values.FPGA_TEMPER_2.clear()
            global_values.FPGA_TEMPER_3.clear()
            self.ids.start_control.text   = 'СТАРТ'
            self.ids.switch.touch_control = None
            Clock.unschedule(self.get_value_1)
            Clock.unschedule(self.get_value_2)
            Clock.unschedule(self.get_value_3)

##=====================================================================================
##
##===================================================================================== 

    def get_value_1(self, dt):
        self.graph_1.points = [(i,j) for i, j in enumerate(global_values.FPGA_TEMPER_1)] 
    def get_value_2(self, dt):
        self.graph_2.points = [(i,j) for i, j in enumerate(global_values.FPGA_TEMPER_2)]
    def get_value_3(self, dt):
        self.graph_3.points = [(i,j) for i, j in enumerate(global_values.FPGA_TEMPER_3)]
        ##------autoscale---------------------
        self.ids.graph.ymax = round(float(global_values.max_temp + 5),0)
        self.ids.graph.ymin = round(float(global_values.min_temp - 5),0)  

##=====================================================================================
##======================for control speed of updating graph============================
##=====================================================================================  

    def move(self):
        update         = int(self.ids.updating_time.text)
        global_values.update  = update
        number_of_dots = self.ids.display_time.value
        self.ids.time_of_display.text = str(int(number_of_dots*update/1000))

##=====================================================================================
##==============================updating values of label===============================
##=====================================================================================        

    def display_time_changes(self):
        number_of_dots = self.ids.display_time.value
        self.ids.time_of_display.text = str(int(number_of_dots*global_values.update/1000))

##=====================================================================================
##==========================when moving to another window==============================
##=====================================================================================
   
    def stop_drawing(self):
        global_values.start_stop = False

##=====================================================================================
##=================clear buffer when moving to another window==========================
##=====================================================================================

    def refresh_socket(self):
        Socket_control.refresh_socket()

##=====================================================================================
##
##=====================================================================================

    def socket_close(self):
        Socket_control.close_socket()
       
