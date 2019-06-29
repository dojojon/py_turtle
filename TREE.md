# Trees

## Introduction

Use loops and recursion to create fractal trees.

## What you will make

![Trees](/fractal_tree.png)

##

1. Open the blank Python template Trinket: [jumpto.cc/python-new](jumpto.cc/python-new).

1. Add the following:

```python
from turtle import *

```

1. Add the following code to point our turtle up the canvas.

```python
 setheading(90)
 ```

 
1. We are going to define a function that gets calls its self to draw the branches.  It will set the branch color and draw the first branch.  Add the following to define a function we can call.  

```python
def draw_branch():
    color("brown")
    forward(40)
```

1.  Below our new function add the following to call the function:

```python
draw_branch()
```

1.  Our tree is made up of branches that get smaller and smaller, lets add an parameter to this function for the length.  Update the function so it looks like this:

```python
def draw_branch(len):
    color("brown")
    forward(len)
```

1. And update where we call the function:

```python
draw_branch(40)
```

1. Try change the we are passing in to see how it changes the length of the branch we draw.

1.

```python
```
```python
```


def draw_branch(len):
    
    if(len > 5):
        color("brown")
        forward(len)
        right(25 )
        draw_branch(len - randint(4,10))
        left(50)
        draw_branch(len - randint(4,10))
        right(25)
        color("brown")
        backward(len)
    else:
        color("green", "green")
        begin_fill()
        circle(10+ randint(0,5))
        end_fill()
        
def draw_tree(start_len):
    pendown()
    setheading(90)
    color("brown")
    pensize(5)
    draw_branch(start_len)
 

penup()
goto(-100, -200)
draw_tree(randint(40, 60))
penup()
goto(100, -180)
draw_tree(randint(30, 40))


