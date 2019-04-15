from kivy.uix.screenmanager import Screen
from kivy.uix.popup         import Popup

from kivy.properties        import ObjectProperty
from kivy.uix.boxlayout     import BoxLayout
import struct
import os

import Socket_control

import global_values

class CONTROL(Screen):
    def __init__(self, **kw):
        super(CONTROL, self).__init__(**kw)

        ##===when moving to TEMP window======
    def cont_drawing(self):
        if global_values.pause == False:
            global_values.start_stop = True

##=====================================================================================
##
##=====================================================================================

    def socket_close(self):
        Socket_control.close_socket()

##=====================================================================================
##
##=====================================================================================

    def dismiss_popup(self):
        self._popup.dismiss()

##=====================================================================================
##
##=====================================================================================

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

##=====================================================================================
##
##===================================================================================== 

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

##=====================================================================================
##
##=====================================================================================

    def load(self, path, filename):
        try:
            with open(os.path.join(path, filename[0]),'r') as stream:
                file = stream.read().split('\n')
        except:
            pass
        else:

##=============================RADIO BUTTONS===============================

            try:
                if (file[3] == '0'):
                    self.ids.duplication_off_01.active = True
                    self.ids.duplication_on_01.active  = False
                elif (file[3] == '1'):
                    self.ids.duplication_on_01.active  = True
                    self.ids.duplication_off_01.active = False 
                else:##----switch off if input data incorrect------
                    self.ids.duplication_on_01.active  = False
                    self.ids.duplication_off_01.active = False

                if (file[15] == '0'):
                    self.ids.prohibition_of_adaptation_off_44.active = True
                    self.ids.prohibition_of_adaptation_on_44.active  = False
                elif(file[15] == '1'):
                    self.ids.prohibition_of_adaptation_on_44.active  = True
                    self.ids.prohibition_of_adaptation_off_44.active = False
                else:##----switch off if input data incorrect------
                    self.ids.prohibition_of_adaptation_on_44.active  = False
                    self.ids.prohibition_of_adaptation_off_44.active = False

                if (file[23] == '0'):
                    self.ids.MDF_control_register_off_48.active = True
                    self.ids.MDF_control_register_on_48.active  = False 
                elif (file[23] == '1'):
                    self.ids.MDF_control_register_on_48.active  = True
                    self.ids.MDF_control_register_off_48.active = False
                else:##----switch off if input data incorrect------
                    self.ids.MDF_control_register_on_48.active  = False
                    self.ids.MDF_control_register_off_48.active = False

                if (file[37] == '0'):
                    self.ids.amplitude_unstability_on_50.active  = True
                    self.ids.amplitude_unstability_off_50.active = False
                elif (file[37] == '1'):
                    self.ids.amplitude_unstability_off_50.active = True
                    self.ids.amplitude_unstability_on_50.active  = False
                else:##----switch off if input data incorrect------
                    self.ids.amplitude_unstability_off_50.active = False
                    self.ids.amplitude_unstability_on_50.active  = False

                if (file[39] == '0'):
                    self.ids.phase_unstability_on_51.active  = True
                    self.ids.phase_unstability_off_51.active = False 
                elif(file[39] == '1'):
                    self.ids.phase_unstability_off_51.active = True
                    self.ids.phase_unstability_on_51.active  = False
                else:##----switch off if input data incorrect------
                    self.ids.phase_unstability_off_51.active = False
                    self.ids.phase_unstability_on_51.active  = False

                if (file[45] == '0'):
                    self.ids.phase_threshold_on_54.active  = True
                    self.ids.phase_threshold_off_54.active = False 
                elif(file[45] == '1'):
                    self.ids.phase_threshold_off_54.active = True
                    self.ids.phase_threshold_on_54.active  = False
                else:##----switch off if input data incorrect------
                    self.ids.phase_threshold_off_54.active = False
                    self.ids.phase_threshold_on_54.active  = False

                if (file[55] == '0'):
                    self.ids.BNP_resolution_off_59.active = True
                    self.ids.BNP_resolution_on_59.active  = False
                elif(file[55] == '1'):
                    self.ids.BNP_resolution_on_59.active  = True
                    self.ids.BNP_resolution_off_59.active = False
                else:##----switch off if input data incorrect------
                    self.ids.BNP_resolution_on_59.active  = False
                    self.ids.BNP_resolution_off_59.active = False
            except IndexError:
                pass

##=================================BOOTLOADER==================================

            try:
                global_values.BOOTLOADER_SETTINGS_FPGA_1 = file[5]
                global_values.BOOTLOADER_SETTINGS_FPGA_2 = file[13]
                global_values.BOOTLOADER_SETTINGS_FPGA_3 = file[11]
            except IndexError:
                pass   

##=================================TEXT INPUT===================================

            try:
                self.ids.correction_register_04A.text       = file[7]
            except IndexError:
                pass
            try:
                self.ids.correction_register_04B.text       = file[9]
            except IndexError:
                pass
            try:
                self.ids.averaging_window_45.text           = file[17]
            except IndexError:
                pass
            try:
                self.ids.suppression_band_46.text           = file[19]
            except IndexError:
                pass
            try:
                self.ids.threshold_control_register_47.text = file[21]
            except IndexError:
                pass
            try:
                self.ids.period_threshold_49.text           = file[25]
            except IndexError:
                pass
            try:
                self.ids.noise_level_52.text                = file[41]
            except IndexError:
                pass
            try:
                self.ids.noise_level_excess_53.text         = file[43]
            except IndexError:
                pass
            try:
                self.ids.phase_threshold_register_55.text   = file[47]
            except IndexError:
                pass
            try:
                self.ids.phase_threshold_register_56.text   = file[49]
            except IndexError:
                pass
            try:
                self.ids.sum_delta_threshold_57.text        = file[51]
            except IndexError:
                pass
            try:
                self.ids.velocity_evaluation_58.text        = file[53]
            except IndexError:
                pass

            self.dismiss_popup()

##=====================================================================================
##
##=====================================================================================

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write('REGISTERS\n')
            stream.write('\n')
            stream.write('Register 0x01:\n')
            if (self.ids.duplication_off_01.active   == True  and self.ids.duplication_on_01.active == False):
                stream.write('0\n')
            elif (self.ids.duplication_off_01.active == False and self.ids.duplication_on_01.active == True):
                stream.write('1\n')
            else:##-----if both radio buttons switch off-------
                stream.write('\n')
            stream.write('Register 0x4:\n')
            stream.write(str(global_values.BOOTLOADER_SETTINGS_FPGA_1) + '\n')
            stream.write('Register 0x4A:\n')
            stream.write(str(self.ids.correction_register_04A.text) + '\n')
            stream.write('Register 0x4B:\n')
            stream.write(str(self.ids.correction_register_04B.text) + '\n')
            stream.write('Register 0x4C:\n')
            stream.write(str(global_values.BOOTLOADER_SETTINGS_FPGA_3) + '\n')
            stream.write('Register 0x24:\n')
            stream.write(str(global_values.BOOTLOADER_SETTINGS_FPGA_2) + '\n')
            stream.write('Register 0x44:\n')
            if (self.ids.prohibition_of_adaptation_off_44.active   == True  and self.ids.prohibition_of_adaptation_on_44.active == False):
                stream.write('0\n')
            elif (self.ids.prohibition_of_adaptation_off_44.active == False and self.ids.prohibition_of_adaptation_on_44.active == True):
                stream.write('1\n')
            else:##-----if both radio buttons switch off-------
                stream.write('\n')
            stream.write('Register 0x45:\n')
            stream.write(str(self.ids.averaging_window_45.text) + '\n')
            stream.write('Register 0x46:\n')
            stream.write(str(self.ids.suppression_band_46.text) + '\n')
            stream.write('Register 0x47:\n')
            stream.write(str(self.ids.threshold_control_register_47.text) + '\n')
            stream.write('Register 0x48:\n')
            if (self.ids.MDF_control_register_off_48.active  == True  and self.ids.MDF_control_register_on_48.active == False):
                stream.write('0\n')
            elif(self.ids.MDF_control_register_off_48.active == False and self.ids.MDF_control_register_on_48.active == True):
                stream.write('1\n')
            else:
                stream.write('\n')##-----if both radio buttons switch off-------
            stream.write('Register 0x49:\n')
            stream.write(str(self.ids.period_threshold_49.text) + '\n')
            
            stream.write('Temperature 1:\n')
            tempr_1 = Socket_control.read_from_reg('03')
            try: 
                tempr_1 = int.from_bytes(bytes([tempr_1[23]]), byteorder = 'big', signed=True)
            except TypeError:  
                stream.write('\n')            
            else:
                stream.write(str(tempr_1) + '\n')
                
            stream.write('Temperature 2:\n')
            tempr_2 = Socket_control.read_from_reg('23')
            try: 
                tempr_2 = int.from_bytes(bytes([tempr_2[23]]), byteorder = 'big', signed=True)
            except TypeError:  
                stream.write('\n')            
            else:
                stream.write(str(tempr_2) + '\n')
                
            stream.write('Temperature 3:\n')
            tempr_3 = Socket_control.read_from_reg('43')
            try: 
                tempr_3 = int.from_bytes(bytes([tempr_3[23]]), byteorder = 'big', signed=True)
            except TypeError:  
                stream.write('\n')            
            else:
                stream.write(str(tempr_3) + '\n')
                
            stream.write('IP:\n')
            stream.write(str(Socket_control.DSPM_IP_ADDRESS) + '\n')
            stream.write('PORT:\n')
            stream.write(str(Socket_control.DSPM_PORT_NO) + '\n')

            stream.write('Register 0x50:\n') 
            if (self.ids.amplitude_unstability_off_50.active  == True  and self.ids.amplitude_unstability_on_50.active == False):
                stream.write('1\n')
            elif(self.ids.amplitude_unstability_off_50.active == False and self.ids.amplitude_unstability_on_50.active == True):
                stream.write('0\n')
            else:##-----if both radio buttons switch off-------
                stream.write('\n')
            stream.write('Register 0x51:\n')
            if (self.ids.phase_unstability_off_51.active  == True  and self.ids.phase_unstability_on_51.active == False):
                stream.write('1\n')
            elif(self.ids.phase_unstability_off_51.active == False and self.ids.phase_unstability_on_51.active == True):
                stream.write('0\n')
            else:##-----if both radio buttons switch off-------
                stream.write('\n')
            stream.write('Register 0x52:\n')
            stream.write(str(self.ids.noise_level_52.text) + '\n')
            stream.write('Register 0x53:\n')
            stream.write(str(self.ids.noise_level_excess_53.text) + '\n')
            stream.write('Register 0x54:\n')
            if (self.ids.phase_threshold_off_54.active  == True  and self.ids.phase_threshold_on_54.active == False):
                stream.write('1\n')
            elif(self.ids.phase_threshold_off_54.active == False and self.ids.phase_threshold_on_54.active == True):
                stream.write('0\n')
            else:##-----if both radio buttons switch off-------
                stream.write('\n')
            stream.write('Register 0x55:\n')
            stream.write(str(self.ids.phase_threshold_register_55.text) + '\n')
            stream.write('Register 0x56:\n')
            stream.write(str(self.ids.phase_threshold_register_56.text) + '\n')
            stream.write('Register 0x57:\n')
            stream.write(str(self.ids.sum_delta_threshold_57.text) + '\n')
            stream.write('Register 0x58:\n')
            stream.write(str(self.ids.velocity_evaluation_58.text) + '\n')
            stream.write('Register 0x59:\n')
            if (self.ids.BNP_resolution_off_59.active  == True  and self.ids.BNP_resolution_on_59.active == False):
                stream.write('0\n')
            elif(self.ids.BNP_resolution_off_59.active == False and self.ids.BNP_resolution_on_59.active == True):
                stream.write('1\n') 
            else:##-----if both radio buttons switch off-------
                stream.write('\n')               
        self.dismiss_popup()

##=====================================================================================
##
##=====================================================================================

    def apply(self):

##=============================RADIO BUTTONS===============================

        if (self.ids.duplication_off_01.active == True) and (self.ids.duplication_on_01.active == False):
             Socket_control.write_to_reg('01', 'AC10002C00')
        elif (self.ids.duplication_off_01.active == False) and (self.ids.duplication_on_01.active == False):
            Socket_control.write_to_reg('01', '')
        else:
            Socket_control.write_to_reg('01', 'AC10002C01')

        if (self.ids.prohibition_of_adaptation_off_44.active == True) and (self.ids.prohibition_of_adaptation_on_44.active == False):
             Socket_control.write_to_reg('44', '00')
        elif (self.ids.prohibition_of_adaptation_off_44.active == False) and (self.ids.prohibition_of_adaptation_on_44.active == False):
            Socket_control.write_to_reg('44', '')
        else:
            Socket_control.write_to_reg('44', '01')

        if (self.ids.MDF_control_register_off_48.active == True) and (self.ids.MDF_control_register_on_48.active == False):
             Socket_control.write_to_reg('48', '00')
        elif (self.ids.MDF_control_register_off_48.active == False) and (self.ids.MDF_control_register_on_48.active == False):
            Socket_control.write_to_reg('48', '')
        else:
            Socket_control.write_to_reg('48', '01')

        if (self.ids.amplitude_unstability_on_50.active == True) and (self.ids.amplitude_unstability_off_50.active == False):
             Socket_control.write_to_reg('50', '00')
        elif (self.ids.amplitude_unstability_on_50.active == False) and (self.ids.amplitude_unstability_off_50.active == False):
            Socket_control.write_to_reg('50', '')
        else:
            Socket_control.write_to_reg('50', '01')

        if (self.ids.phase_unstability_on_51.active == True) and (self.ids.phase_unstability_off_51.active == False):
             Socket_control.write_to_reg('51', '00')
        elif (self.ids.phase_unstability_on_51.active == False) and (self.ids.phase_unstability_off_51.active == False):
            Socket_control.write_to_reg('51', '')
        else:
            Socket_control.write_to_reg('51', '01')

        if (self.ids.phase_threshold_on_54.active == True) and (self.ids.phase_threshold_off_54.active == False):
             Socket_control.write_to_reg('54', '00')
        elif (self.ids.phase_threshold_on_54.active == False) and (self.ids.phase_threshold_off_54.active == False):
            Socket_control.write_to_reg('54', '')
        else:
            Socket_control.write_to_reg('54', '01')

        if (self.ids.BNP_resolution_off_59.active  == True) and (self.ids.BNP_resolution_on_59.active  == False):
             Socket_control.write_to_reg('59', '00')
        elif (self.ids.BNP_resolution_off_59.active  == False) and (self.ids.BNP_resolution_on_59.active  == False):
            Socket_control.write_to_reg('59', '')
        else:
            Socket_control.write_to_reg('59', '01')

##=================================TEXT INPUT=======================================

        try:
        	packadge = hex(int(self.ids.averaging_window_45.text))
        except ValueError:
        	pass
        else:
        	Socket_control.write_to_reg('45', packadge[2:])

        try:
        	packadge = hex(int(self.ids.suppression_band_46.text))
        except ValueError:
        	pass
        else:
        	Socket_control.write_to_reg('46', packadge[2:])

        try:
        	packadge = hex(int(self.ids.threshold_control_register_47.text))
        except ValueError:
        	pass
        else:
        	Socket_control.write_to_reg('47', packadge[2:])

        try:
        	packadge = hex(int(self.ids.period_threshold_49.text))
        except ValueError:
        	pass
        else:
        	Socket_control.write_to_reg('49', packadge[2:])

        try:
        	packadge = hex(int(self.ids.correction_register_04A.text))
        except ValueError:
        	pass
        else:
        	Socket_control.write_to_reg('4A', packadge[2:])

        try:
        	packadge = hex(int(self.ids.correction_register_04B.text))
        except ValueError:
        	pass
        else:
        	Socket_control.write_to_reg('4B', packadge[2:])

        try:
        	packadge = hex(int(self.ids.sum_delta_threshold_57.text))
        except ValueError:
        	pass
        else:
        	Socket_control.write_to_reg('57', packadge[2:])

        try:
        	packadge = hex(int(self.ids.velocity_evaluation_58.text))
        except ValueError:
        	pass
        else:
        	Socket_control.write_to_reg('58', packadge[2:])

##==================================SINGLE FLOAT=======================================

        try:
        	packadge = float(self.ids.noise_level_52.text.replace(',','.'))
        except ValueError:
        	pass
        else:
        	packadge = hex(struct.unpack('<I', struct.pack('<f', packadge))[0])
        	Socket_control.write_to_reg('52', packadge[2:])

        try:
        	packadge = float(self.ids.noise_level_excess_53.text.replace(',','.'))
        except ValueError:
        	pass
        else:
        	packadge = hex(struct.unpack('<I', struct.pack('<f', packadge))[0])
        	Socket_control.write_to_reg('53', packadge[2:])

        try:
        	packadge = float(self.ids.phase_threshold_register_55.text.replace(',','.'))
        except ValueError:
        	pass
        else:
        	packadge = hex(struct.unpack('<I', struct.pack('<f', packadge))[0])
        	Socket_control.write_to_reg('55', packadge[2:])

        try:
        	packadge = float(self.ids.phase_threshold_register_56.text.replace(',','.'))
        except ValueError:
        	pass
        else:
        	packadge = hex(struct.unpack('<I', struct.pack('<f', packadge))[0])
        	Socket_control.write_to_reg('56', packadge[2:])

##=====================================================================================
##
##=====================================================================================

    def request(self):
##=============================RADIO BUTTONS===============================

        packadge = Socket_control.read_from_reg('01')
        if type(packadge) == str:
            self.ids.duplication_on_01.active  = False
            self.ids.duplication_off_01.active = False
        else:
            if (packadge[23] == 0):
                self.ids.duplication_off_01.active = True
                self.ids.duplication_on_01.active  = False
            elif (packadge[23] == 1):
                self.ids.duplication_on_01.active  = True
                self.ids.duplication_off_01.active = False

        packadge = Socket_control.read_from_reg('44')
        if type(packadge) == str:
            self.ids.prohibition_of_adaptation_on_44.active  = False
            self.ids.prohibition_of_adaptation_off_44.active = False
        else:
            if (packadge[23] == 0):
                self.ids.prohibition_of_adaptation_off_44.active = True
                self.ids.prohibition_of_adaptation_on_44.active  = False
            elif (packadge[23] == 1):
                self.ids.prohibition_of_adaptation_on_44.active  = True
                self.ids.prohibition_of_adaptation_off_44.active = False
                
        packadge = Socket_control.read_from_reg('48')
        if type(packadge) == str:
            self.ids.MDF_control_register_on_48.active  = False
            self.ids.MDF_control_register_off_48.active = False
        else:
            if (packadge[23] == 0):
                self.ids.MDF_control_register_off_48.active = True
                self.ids.MDF_control_register_on_48.active  = False
            elif (packadge[23] == 1):
                self.ids.MDF_control_register_on_48.active  = True
                self.ids.MDF_control_register_off_48.active = False
                
        packadge = Socket_control.read_from_reg('50')
        if type(packadge) == str:
            self.ids.amplitude_unstability_on_50.active  = False
            self.ids.amplitude_unstability_off_50.active = False
        else:
            if (packadge[23] == 0):
                self.ids.amplitude_unstability_on_50.active   = True
                self.ids.amplitude_unstability_off_50.active  = False
            elif (packadge[23] == 1):
                self.ids.amplitude_unstability_off_50.active  = True
                self.ids.amplitude_unstability_on_50.active   = False
                
        packadge = Socket_control.read_from_reg('51')
        if type(packadge) == str:           
            self.ids.phase_unstability_on_51.active  = False
            self.ids.phase_unstability_off_51.active = False
        else:
            if (packadge[23] == 0):
                self.ids.phase_unstability_on_51.active   = True
                self.ids.phase_unstability_off_51.active  = False
            elif (packadge[23] == 1):
                self.ids.phase_unstability_off_51.active  = True
                self.ids.phase_unstability_on_51.active   = False
                
        packadge = Socket_control.read_from_reg('54')
        if type(packadge) == str:
            self.ids.phase_threshold_on_54.active  = False
            self.ids.phase_threshold_off_54.active = False
        else:
            if (packadge[23] == 0):
                self.ids.phase_threshold_on_54.active   = True
                self.ids.phase_threshold_off_54.active  = False
            elif (packadge[23] == 1):
                self.ids.phase_threshold_off_54.active  = True
                self.ids.phase_threshold_on_54.active   = False
                
        packadge = Socket_control.read_from_reg('59')
        if type(packadge) == str:
            self.ids.duplication_on_01.active     = False
            self.ids.BNP_resolution_off_59.active = False
        else:
            if (packadge[23] == 0):
                self.ids.BNP_resolution_off_59.active = True
                self.ids.BNP_resolution_on_59.active  = False
            elif (packadge[23] == 1):
                self.ids.BNP_resolution_on_59.active  = True
                self.ids.BNP_resolution_off_59.active = False

##=================================TEXT INPUT=======================================

        packadge = Socket_control.read_from_reg('45')
        try:
            self.ids.averaging_window_45.text = str(int.from_bytes(packadge[23:24], byteorder='big'))
        except TypeError:
            pass
        packadge = Socket_control.read_from_reg('46')
        try:
            self.ids.suppression_band_46.text = str(int.from_bytes(packadge[23:24], byteorder='big'))
        except TypeError:
            pass
        packadge = Socket_control.read_from_reg('47')
        try:
            self.ids.threshold_control_register_47.text = str(int.from_bytes(packadge[22:24], byteorder='big'))
        except TypeError:
            pass
        packadge = Socket_control.read_from_reg('49')
        try:
            self.ids.period_threshold_49.text = str(int.from_bytes(packadge[23:24], byteorder='big') )
        except TypeError:
            pass
        packadge = Socket_control.read_from_reg('4A')
        try:
            self.ids.correction_register_04A.text = str(int.from_bytes(packadge[22:24], byteorder='big'))
        except TypeError:
            pass
        packadge = Socket_control.read_from_reg('4B')
        try:
            self.ids.correction_register_04B.text = str(int.from_bytes(packadge[22:24], byteorder='big'))
        except TypeError:
            pass
        packadge = Socket_control.read_from_reg('57')
        try:
            self.ids.sum_delta_threshold_57.text = str(int.from_bytes(packadge[23:24], byteorder='big'))
        except TypeError:
            pass
        packadge = Socket_control.read_from_reg('58')
        try:
            self.ids.velocity_evaluation_58.text = str(int.from_bytes(packadge[23:24], byteorder='big'))
        except TypeError:
            pass

##==================================SINGLE FLOAT=======================================

        packadge = Socket_control.read_from_reg('52')
        try:
        	self.ids.noise_level_52.text = str(round((struct.unpack(">f", bytes.fromhex((packadge[20:24]).hex()))[0]), 3))
        except AttributeError:
        	pass
        packadge = Socket_control.read_from_reg('53')
        try:
        	self.ids.noise_level_excess_53.text = str(round((struct.unpack(">f", bytes.fromhex((packadge[20:24]).hex()))[0]), 3))
        except AttributeError:
        	pass
        packadge = Socket_control.read_from_reg('55')
        try:
        	self.ids.phase_threshold_register_55.text = str(round((struct.unpack(">f", bytes.fromhex((packadge[20:24]).hex()))[0]), 3))
        except AttributeError:
        	pass
        packadge = Socket_control.read_from_reg('56')
        try:
        	self.ids.phase_threshold_register_56.text = str(round((struct.unpack(">f", bytes.fromhex((packadge[20:24]).hex()))[0]), 3))
        except AttributeError:
        	pass
 
##=====================================================================================
##
##=====================================================================================  

class LoadDialog(BoxLayout):
    load       = ObjectProperty(None)
    cancel     = ObjectProperty(None)
class SaveDialog(BoxLayout):
    save       = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel     = ObjectProperty(None)
##-----------------------------
