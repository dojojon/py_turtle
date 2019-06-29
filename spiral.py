from turtle import *

speed(0)
def draw_section(len):

    forward(len)
    right(50)
    if(len > 5):
        draw_section(len - 2)
        
        
draw_section(100)