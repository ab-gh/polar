#!/usr/bin/env python
import time
from bh1745 import BH1745
import dot3k.lcd as lcd
import dot3k.backlight as backlight


print("""
This example shows a basic "Hello World" on the LCD.
You should see "Hello World" displayed on your LCD!
Press CTRL+C to exit.
""")

bh1745 = BH1745()

bh1745.setup()
bh1745.set_leds(0)
backlight.rgb(200,200,200)
time.sleep(1.0)  # Skip the reading that happened before the LEDs were enabled

try:
    while True:
        r, g, b, c = bh1745.get_rgbc_raw()
        print('RGBC: {:10.1f} {:10.1f} {:10.1f} {:10.1f}'.format(r, g, b, c))
        # Clear the LCD and display Hello World
        lcd.clear()
        lcd.write('{:10.1f}'.format(c))
        time.sleep(0.1)

except KeyboardInterrupt:
    bh1745.set_leds(0)
