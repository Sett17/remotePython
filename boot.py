import network
ssid = "WLAN M+P+L"
password =  "91788659817388541394"

station = network.WLAN(network.STA_IF)

if station.isconnected() == True:
    print("Already connected")

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print("Connection successful")
print(station.ifconfig())


#import webrepl
#
