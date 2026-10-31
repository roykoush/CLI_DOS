import random
from turtle import *

L = [0, 90, 180, 270]
L2 = ['red', 'blue', 'green', 'purple']
reset()
mode('logo')
for i in range(20):    
    color(random.choice(L2))    
    rt(random.choice(L))    
    fd(30)

done()