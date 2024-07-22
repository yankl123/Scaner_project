from gpiozero import LED
from time import sleep

def ledOn(led_num, seconds) :
	led = LED(led_num)
	led.on()
	sleep(seconds)
	led.off()

def ledFlash(led_num, seconds, times) :  
	led = LED(led_num)
	
	while(times) :
		led.on()
		sleep(seconds)
		led.off()
		sleep(seconds)
		times = times-1





















