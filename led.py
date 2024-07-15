from gpiozero import LED
from time import sleep


def ledOn(led_num, seconds) :
	led = LED(led_num)
	led.on()
	sleep(seconds)
	led.off()

def ledFlash(led_num, seconds) :  
	led = LED(led_num)
	
	while(True) :
		led.on()
		sleep(seconds)
		led.off()
		sleep(seconds)



def main() :
	ledOn(17,10)
	ledFlash(17,1)
main()


















