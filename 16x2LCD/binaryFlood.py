import RGB1602
import time
import math
import random

lcd = RGB1602.RGB1602(16,2)

def rand_bin(n):
    s = ""
    for i in range(n):
        s += str(random.randint(0, 1))
    return s

while True:
    lcd.setRGB(255, 0, 10)
    
    for i in range(15):
        lcd.clear()
        lcd.setCursor(0, 0)
        lcd.printout(rand_bin(16))
        
        lcd.setCursor(0, 1)
        lcd.printout(rand_bin(16))
        
        time.sleep(.1)
        
    lcd.clear()
    lcd.setCursor(0,0)
    lcd.printout("Beep Boop")
    time.sleep(1)