
from picamera2 import Picamera2, Preview

from time import sleep

def scan_image() :

    picam2 = Picamera2()
    picam2.configure(picam2.create_still_configuration())
    picam2.start()
    sleep(2)
    picam2.capture_file("dd.jpg")
    
    picam2.close()
           

    
scan_image()
