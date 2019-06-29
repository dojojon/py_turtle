from turtle import *

speed(0)
def square(len):
    
    for s in range(4):
        forward(len)
        right(90)

step = 10
for n in range(int(360/step)):    
    square(140)
    right(step)
