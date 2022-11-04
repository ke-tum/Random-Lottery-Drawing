# Random-Lottery-Drawing
# This program is inspired by Powerball

import random


reg_drawing = []
power_drawing = []


for i in range(5):
    if i not in reg_drawing:
        reg_drawing.append(random.randint(1, 69))


for i in range(1):
    power_drawing.append(random.randint(1, 26))

print(f'Your drawing is {reg_drawing}. Your Power Draw is {power_drawing[0]}.')
print('Thanks for playing!')