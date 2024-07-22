
from picamera2 import Picamera2, Preview
from PIL import Image 
from time import sleep
from datetime import date


def scan_image(dest, tagUid) :

    picam2 = Picamera2()
    picam2.configure(picam2.create_still_configuration())
    picam2.start()

    time_out = 50 

    while time_out :

        image_name = ""
        image_arr = picam2.capture_array()

        imageCorrect = True 

        """
        #TODO 

        """
        if imageCorrect :
            today = date.today() 
            image_name = "{}/{}-{}.jpg".format(dest,tagUid,today)
            image = Image.fromarray(image_arr)
            image.save(image_name)
            picam2.close()
            break

        sleep(0.2)
        time_out = time_out-1 
    picam2.stop()
    return image_name 
