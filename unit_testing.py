import random

import excercise1
from excercise1 import Bus

Bus = Bus("ROOI DAKKIE", 142,["Black", "Yellow", "Orange", "White", "Blue"])

print(Bus.driver)
print(Bus.seats)
print(Bus.color[random.randint(0, 4)])
