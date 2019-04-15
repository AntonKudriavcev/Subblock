import time
import global_values

##=====================================================================================
##
##=====================================================================================

def txt_creator(): 
    with open(str(global_values.time_of_creation + '.txt'),'w', encoding = 'utf-8') as txt_file:
        txt_file.write(global_values.time_of_creation + '\n' + '\n')
        txt_file.write('TIME\tFPGA_1\tFPGA_2\tFPGA_3\n')

##=====================================================================================
##
##=====================================================================================

def write_to_log(temper_1, temper_2, temper_3):
    with open(str(global_values.time_of_creation + '.txt'),'a', encoding = 'utf-8') as txt_file:
        txt_file.write('{0}\t{1}\t{2}\t{3}\n'
                .format(round((time.perf_counter() - global_values.time_of_start),3),temper_1,temper_2,temper_3))

