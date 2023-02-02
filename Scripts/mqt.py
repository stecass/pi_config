#!/usr/bin/env python
import json
import time
import paho.mqtt.client as mqtt
import mqt_creds
from microdotphat import write_string, set_decimal, clear, show


# This is the Subscriber

def on_connect(client, userdata, flags, rc):
#  print("Connected with result code "+str(rc))
  client.subscribe("tele/tasmota_5987C6/SENSOR")
  outputMessage ("ok..")

def on_message(client, userdata, msg):
    print msg.payload.decode()
    json_string = msg.payload.decode()
    temp=json.loads(json_string)
    temp_unit=temp["TempUnit"]
    temper=temp["BME280"]
    print (temper)
    temperature=temp["BME280"]["Temperature"]
    print (temperature )
    print(temp_unit)

    print "Current temperature is %s%s" %(temperature,temp_unit)

    clear()
    outputMessage ( "%.1f" % temperature)
    
    show()

def outputMessage(msg):
    clear()
    write_string (msg, kerning=False)
    show()
    time.sleep(2)


outputMessage("Wait")
client = mqtt.Client()
client.username_pw_set(username=mqt_creds.username,password=mqt_creds.password)
client.connect("192.168.2.121",1883,60)

client.on_connect = on_connect
print ("connecting")
client.on_message = on_message
print ("awaiting message")

client.loop_forever()
