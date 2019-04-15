
##--global values for TEMPER, get_temper_values, log and other screens
pause         = True  ##--need for pause plotting graph when mooving from TEMPER to other screens and vise versa
start_stop    = False ##--need for stop plotting graph when press STOP button 
write_to_file = False ##--for writing log
FPGA_TEMPER_1 = []    
FPGA_TEMPER_2 = []
FPGA_TEMPER_3 = []
max_temp      = 50
min_temp      = 30 
update        = 500 ##--first value of updating graph

##=====================================================================================
##
##=====================================================================================

time_of_creation = None##--string 
time_of_start    = None##--numerical

##=====================================================================================
##===========global values for CONTROL and BOOTLOADER_SETTINGS screens=================
##=====================================================================================
   
BOOTLOADER_SETTINGS_FPGA_1 = ''  
BOOTLOADER_SETTINGS_FPGA_2 = ''
BOOTLOADER_SETTINGS_FPGA_3 = ''