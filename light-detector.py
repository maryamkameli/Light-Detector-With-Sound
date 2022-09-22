import math
import sys
import time
from grove.adc import ADC
import RPi.GPIO as GPIO
#This creates the light sensor class (just helps contain the ADC call)
class GroveLightSensor:
 
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC(0x08)
 
    @property
    def light(self):
        value = self.adc.read(self.channel)
        return value


Grove = GroveLightSensor
def sos(pin):
        #dot dot dot
        GPIO. OUTPUT (pin, GPIO. HIGH)
        time. sleep(0.1)
        GPIO. OUTPUT (pin, GPIO. LOW)
        time.sleep(0.5)
        GPIO. OUTPUT (pin, GPIO. HIGH)
        time. sleep(0.1)
        GPIO. OUTPUT (pin, GPIO. LOW)
        time.sleep(0.5)
        GPIO. OUTPUT (pin, GPIO. HIGH)
        time. sleep(0.1)
        GPIO. OUTPUT (pin, GPIO. LOW)
        time.sleep(0.5)
    
    #dash dash dash
        GPIO. OUTPUT (pin, GPIO. HIGH)
        time. sleep(1)
        GPIO. OUTPUT (pin, GPIO. LOW)
        time.sleep(0.05)
        GPIO. OUTPUT (pin, GPIO. HIGH)
        time. sleep(1)
        GPIO. OUTPUT (pin, GPIO. LOW)
        time.sleep(0.05)
        GPIO. OUTPUT (pin, GPIO. HIGH)
        time. sleep(1)
        GPIO. OUTPUT (pin, GPIO. LOW)
        time.sleep(0.05)
        
        GPIO. OUTPUT (pin, GPIO. HIGH)
        time. sleep(0.5)
        GPIO. OUTPUT (pin, GPIO. LOW)
        time.sleep(0.05)
        GPIO. OUTPUT (pin, GPIO. HIGH)
        time. sleep(0.5)
        GPIO. OUTPUT (pin, GPIO. LOW)
        time.sleep(0.05)
        GPIO. OUTPUT (pin, GPIO. HIGH)
        time. sleep(0.5)
        GPIO. OUTPUT (pin, GPIO. LOW)
        time.sleep(0.05)  
    

def main():
    #set the pin value for the buzzer
    pin = 5
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    #set the analog value for the light sensor
    sensor = GroveLightSensor(0)
    

 
    while True:
        #the light sensor is sensitive, so a minimum threshold of 300 is best to determine if there is an ample amount of light
        if sensor.light > 300:
            #make the buzzer beep
            sos(pin)
            print(sensor.light)
        #else: up to you whether you want it to be a quick beep or a consistant sound
         time.sleep(1)
    
        
 
if __name__ == '__main__':
    main()
