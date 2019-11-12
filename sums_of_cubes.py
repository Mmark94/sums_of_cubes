#x^3 + y^3 + z^3 = 42
# x^2 - x*y + y^2 = (42 - z^3) / d
# x + y = d

import random
import matplotlib.pyplot as plt
import math

x = 0
y = 0
z = 0
d = 0
t = 0
n = 0
randoms  = 5000
randoms2 = -5000
simulations = 1000000
while t < simulations:
    x = random.randint(0, randoms)
    y = random.randint(randoms2, 0)
    z = random.randint(randoms2, randoms)
    d = random.randint(randoms2, randoms)
    SUM = x**3+y**3+z**3
    if abs(SUM) < 1000:
        print("SUM =", SUM)
        #print("x =", x)
        #print("y =", y)
        #print("z =", z)
        print(str(x) + "^3 + " + str(y) + "^3 + " + str(z) + "^3 = " + str(SUM))

        cube_work = open("cube_work.txt", "a")
        cube_work.write("\n")
        cube_work.write("\n" + str(x) + "^3 + " + str(y) + "^3 + " + str(z) + "^3 = " + str(SUM))
        cube_work.close()
        n = n + 1
    t = t + 1

if n == 0:
    print("YOU LOST!!!")
