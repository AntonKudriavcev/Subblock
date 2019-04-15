import time
from   threading    import Thread 

import Socket_control
from   log          import write_to_log
import global_values

def get_temperature():
    while True:
        if global_values.start_stop == True:##-----when press START------
            income_pack = Socket_control.read_from_reg('03')
            try:
                temper_1 = int.from_bytes(bytes([income_pack[23]]),byteorder = 'big', signed=True)
                global_values.FPGA_TEMPER_1.append(temper_1)
            except TypeError:
                pass
            income_pack = Socket_control.read_from_reg('23')
            try:
                temper_2 = int.from_bytes(bytes([income_pack[23]]),byteorder = 'big', signed=True)
                try:
                    if temper_2 == global_values.FPGA_TEMPER_1[len(global_values.FPGA_TEMPER_1)-1]:
                        global_values.FPGA_TEMPER_2.append(temper_2 + 0.1)
                    else:
                        global_values.FPGA_TEMPER_2.append(temper_2)
                except IndexError:
                    pass
            except TypeError:
                pass
            income_pack = Socket_control.read_from_reg('43')
            try:
                temper_3 = int.from_bytes(bytes([income_pack[23]]),byteorder = 'big',signed=True)
                try:
                    if ((temper_3 == global_values.FPGA_TEMPER_1[len(global_values.FPGA_TEMPER_1)-1]) or
                        (temper_3 == global_values.FPGA_TEMPER_2[len(global_values.FPGA_TEMPER_2)-1])):
                        global_values.FPGA_TEMPER_3.append(temper_3 - 0.1)
                    else:
                        global_values.FPGA_TEMPER_3.append(temper_3)
                except IndexError:
                    pass                                     
            except TypeError:
                pass

            if (len(global_values.FPGA_TEMPER_1) or 
                len(global_values.FPGA_TEMPER_2) or 
                len(global_values.FPGA_TEMPER_3)) >= 302:
                del global_values.FPGA_TEMPER_1[0]
                del global_values.FPGA_TEMPER_2[0]
                del global_values.FPGA_TEMPER_3[0] 
            try:    
                global_values.max_temp = max(max(global_values.FPGA_TEMPER_1),
                    max(global_values.FPGA_TEMPER_2),
                    max(global_values.FPGA_TEMPER_3))
                global_values.min_temp = min(min(global_values.FPGA_TEMPER_1),
                    min(global_values.FPGA_TEMPER_2),
                    min(global_values.FPGA_TEMPER_3))                                    
            except ValueError:
                pass
            if global_values.write_to_file == True:
                try:  
                    write_to_log(temper_1, temper_2, temper_3) 
                except UnboundLocalError:
                    pass
            time.sleep(global_values.update/1000.0000-0.0018)            
        else:##----when press STOP moving to another window----------------
            time.sleep(.01)

##=====================================================================================
##===================================module init=======================================
##=====================================================================================

get_level_thread = Thread(target = get_temperature)
get_level_thread.daemon = True
get_level_thread.start()