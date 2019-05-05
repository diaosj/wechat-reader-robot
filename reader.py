from pymouse import PyMouse
from pykeyboard import PyKeyboard
import random
import time

m = PyMouse()
k = PyKeyboard()

x_dim, y_dim = m.screen_size()
m.click(x_dim/4*3, y_dim/2, 1)
while True:
    k.tap_key(k.page_down_key)
    m.click(x_dim-500, y_dim-50, 1)
    interval = random.randint(25, 35)
    time.sleep(interval)
