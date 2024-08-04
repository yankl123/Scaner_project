import proSetup 
import nfc 
import led
import camera
from time import sleep

while True :
    print("Waitig for nfc trigger :")
    tagUid = nfc.scanNfc() 
    if tagUid :
        print(tagUid)
        image = camera.scan_image('/home/kamateck/Desktop/imges',tagUid) 
        if image :
            print(image) 
            led.ledFlash(17,0.5,10) 
    sleep(0.2)
