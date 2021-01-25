import RPi.GPIO as GPIO             #import Raspberry Pi GPIO library
from time import sleep              #import the sleep method from time module

GPIO.setmode(GPIO.BOARD)            #setup BOARD numbering
GPIO.setup(11, GPIO.OUT)            #set pin 11 as output 

try:
    while True:                     #run forever untill you press Ctrl+C
        GPIO.output(11, 1)          #turn on the LED
        sleep(1)                    #sleep for 1 second
        GPIO.output(11, 0)          #turn off the LED
        sleep(0.5)                  #sleep for 0.5 second
except KeyboardInterrupt:
    GPIO.cleanup()                  #clean up all the ports used
