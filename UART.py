
import time
from machine import UART, Pin
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1), bits=8, parity=None, stop=1)
uart.write('start')
# Initialisierung: UART
# UART 0, TX=GPIO0 (Pin 1), RX=GPIO1 (Pin 2)
# UART 1, TX=GPIO4 (Pin 6), RX=GPIO5 (Pin 7)
#print(uart)

print('Warten auf Daten der Gegenstelle')

while 1:
    time.sleep(2)
    char = uart.read()
    if char is not None:
        try: print(char.decode())
        except: print(char)

    
    
    
    