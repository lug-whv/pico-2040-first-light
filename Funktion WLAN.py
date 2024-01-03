# Bibliotheken laden
import machine
import network
import time

# WLAN-Konfiguration
wlanSSID = 'nordwest.freifunk.net'
wlanPW = ''
network.country('DE')

# Status-LED
led_onboard = machine.Pin('LED', machine.Pin.OUT, value=0)

# Funktion: WLAN-Verbindung
def wlanConnect():
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print('WLAN-Verbindung herstellen')
        wlan.active(True)
        wlan.connect(wlanSSID, wlanPW)
        for i in range(10):
            if wlan.status() < 0 or wlan.status() >= 3:
                break
            led_onboard.toggle()
            print('.', wlan.status())
            time.sleep(1)
    if wlan.isconnected():
        print('WLAN-Verbindung hergestellt')
        led_onboard.on()
        print('WLAN-Status:', wlan.status())
        netConfig = wlan.ifconfig()
        print('IPv4-Adresse:', netConfig[0], '/', netConfig[1])
        print('Standard-Gateway:', netConfig[2])
        print('DNS-Server:', netConfig[3])
    else:
        print('Keine WLAN-Verbindung')
        led_onboard.off()
        print('WLAN-Status:', wlan.status())

# WLAN-Verbindung herstellen
wlanConnect()

# Stromsparmodus abschalten
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
# Stromsparmodus off
wlan.config(pm = 0xa11140)