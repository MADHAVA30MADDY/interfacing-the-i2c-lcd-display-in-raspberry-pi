from RPi_GPIO_i2c_LCD import lcd
from time import sleep

i2c_address = 0x27

lcdDisplay = lcd.HD44780(i2c_address)

    
lcdDisplay.set("     MADHAVAN   ",1)
lcdDisplay.set("   MADDY     ",2)
sleep(1)
while(True):
    
    
    lcdDisplay.backlight("off")
    sleep(1)
    lcdDisplay.backlight("on")
    sleep(1)
