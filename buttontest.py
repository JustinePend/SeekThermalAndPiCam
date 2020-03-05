import RPi.GPIO as GPIO
from picamera import PiCamera
import subprocess
import cv2
import time
import threading
import datetime

def this_is_sketchy():
    name = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("Taking Picture")
    camera.capture('/home/pi/Desktop/Photos/realColor/' + name + '.jpg')
    print("beans beans")
    subprocess.call(["sudo", "./libseek-thermal/examples/seek_viewer","--camtype=seekpro","--colormap=11", "--output=/home/pi/Desktop/Photos/seek.avi"])# "&& sleep 5s", "&& ^C"])
    
    print("end me")
    _,image = cv2.VideoCapture('/home/pi/Desktop/Photos/seek.avi').read()
    status = cv2.imwrite("/home/pi/Desktop/Photos/Thermal/" + name + ".jpg", image)
    print(status)
   
def button_callback(channel):
    thread = threading.Thread(target=this_is_sketchy)
    thread.start()
    print("starting sleep")
    time.sleep(4)
    raise KeyboardInterrupt()


camera = PiCamera()



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(10, GPIO.RISING, callback=button_callback)

message = input("Press enter to quit\n\n")
GPIO.cleanup()