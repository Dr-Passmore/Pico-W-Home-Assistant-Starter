import time
from machine import Pin
import network

# python file containing wifi creds
import wifi_creds

# creds from wifi_creds.py
ssid = wifi_creds.wifi_ssid
password = wifi_creds.wifi_password

wireless = network.WLAN(network.STA_IF)
wireless.active(True)
wireless.connect(ssid, password)

timeout = 10
while timeout > 0:
    if wireless.status() <0 or wireless.status()>=3:
        break
    timeout -=1
    print("Connecting")
    time.sleep(1)
    
if wireless.status() != 3:
    raise RuntimeError("Failed to connect to network")

else:
    print("Succesfully Connected")
    status = wireless.ifconfig()
    print(f'Device IP Address is {status[0]}')