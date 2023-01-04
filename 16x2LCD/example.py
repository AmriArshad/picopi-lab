import machine
import utime
from wslcd1602rgb import WSLCD1602RGB

sda = machine.Pin(0)
scl = machine.Pin(1)
i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)

lcd = WSLCD1602RGB(i2c)
lcd.set_rgb(255, 0, 10)

while True:
    #utime.sleep_ms(2000)
    #lcd.display_on()    
    lcd.print_lines("Mel0n", "")
    #utime.sleep_ms(2000)
    #lcd.display_off()