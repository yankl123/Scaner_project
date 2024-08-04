
from picamera2 import Picamera2, Preview
from PIL import Image 
from time import sleep
from datetime import date
import cv2
import image_validation


def camera_setup() :
    picam2 = Picamera2()
    picam2.resolution = (1920, 1080)
    picam2.awb_mode = 'auto'
    picam2.exposure_mode = 'auto'
    picam2.iso = 100
    picam2.led = True
    picam2.configure(picam2.create_still_configuration())
    picam2.start()

    return picam2 

def capture_images(camera, num_images=5):
    images = []
    for i in range(num_images):
        camera.capture(f'/tmp/image_{i}.jpg')
        img = cv2.imread(f'/tmp/image_{i}.jpg')
        images.append(img)
        sleep(0.1)  # Short delay between captures
    return images

def scan_image(dest, tagUid) :

    time_out = 1

    picam2 = camera_setup() 
    print("scanning..")

    while time_out :

        image_name = ""

        images = capture_images(picam2)
        
        image = image_validation.select_best_image(images)
        h = image.shape[0]
        w = image.shape[1]
        ratio = 0.75
        min_area = int(h*ratio) * int(w*ratio) 
        is_frame_complete = image_validation.detect_complete_frame(image,min_area) 
        
        if image is not None and is_frame_complete == True :
            today = date.today() 
            image_name = f"{dest}/{tagUid}-{today}"
            cv2.imwrite(image_name, image) 
            break

        time_out = time_out-1 
    print("finish scanning")
    print(f"image_is " + ("valid" if is_frame_complete == True else "not valid") )
    picam2.close()
    return image_name 

def capture_images(camera, num_images=5):
    images = []
    for i in range(num_images):
        camera.capture_file(f'/home/kamateck/Desktop/scan_project/tmp/image_{i}.jpg')
        img = cv2.imread(f'/home/kamateck/Desktop/scan_project/tmp/image_{i}.jpg')
        images.append(img)
        sleep(0.1)  # Short delay between captures
    return images