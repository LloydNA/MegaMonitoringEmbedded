from machine import Pin
from time import sleep
import dht
import network
import urequests

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("IZZI-7FB4","9CC8FC877FB4")

sensor = dht.DHT11(Pin(13))

while True:
    sleep(10)     # measure 6 times per minute
    sensor.measure()
    print("Temperature: "+str(round(sensor.temperature(), 1))+" °C")
    print("Humidity: "+str(round(sensor.humidity(), 1))+"%")
    
    temp_req = "http://192.168.0.2:8080/api/devices/users/toribio/temperature/" + str(round(sensor.temperature(), 1))
    hum_req = "http://192.168.0.2:8080/api/devices/users/toribio/humidity/" + str(round(sensor.humidity(), 1))
    
    urequests.post(temp_req)
    urequests.post(hum_req)
