from pyOpenBCI import OpenBCIGanglion
import filterlib as flt
import time
from datetime import datetime


mac_adress = 'd2:b4:11:81:48:ad'

def print_raw(sample):
	
	smp = sample.channels_data[0]
	smp_flted = frt.filterIIR(smp, 0)
	with open(file_name, "a") as myfile:
		myfile.write(f'{str(smp_flted)},{time.time()}\n')

board = OpenBCIGanglion(mac=mac_adress)

if __name__ == '__main__':
	# filtering in real time object creation
	frt = flt.FltRealTime()
	file_name = 'dane_'+datetime.now().strftime("%d-%m_%H:%M")+'.txt'
	print('DANE SĄ ZBIERANE')
	board.start_stream(print_raw)
