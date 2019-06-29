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

1. Next are going to draw two more branches.  First we want to rotate the turtles heading, then we will call our draw branch function again.  Update the draw branch code as follows:

    ```python
    def draw_branch(len):
        color("brown")
        forward(len)
        right(25)
        draw_branch(len)
    ```
1. When you run the code you end up with a circle and a turtle that never stops.  Lets fix that.  Each time we draw a branch, lets make it shorter that the one before.  Update the code as follows:

    ```python
    def draw_branch(len):
        color("brown")
        forward(len)
        right(25)
        draw_branch(len - 5)
    ```

1. Looking a little better, but we need to tell the turtle to stop drawing branches when they get too small.  We can do that with an if statement:

    ```python
    def draw_branch(len):
        if (len > 5):
            color("brown")
            forward(len)
            right(25)
            draw_branch(len - 5)
    ```

1.  Lot better now, lets update the code to draw the other branch.  So after we have draw a branch we want the turtle to go back to the start of the branch before drawing the next:

    ```python
    def draw_branch(len):
        if (len > 5):
            color("brown")
            forward(len)
            right(25)
            draw_branch(len - 5)
            left(50)
            draw_branch(len - 5)
            right(25)
            backward(len)
    ```

1. You should see a tree something like this:

    ![Trees](/simple_tree.png)

1.  You can make thicker branches by using the following:

    ```python
    pensize(5)
    ```

1. You can speed up the drawing by adding the following to the top of the script:

    ```python
    speed(0)
    ```
1. Challenge:  Try changing the shape of the by altering the length of the branches with a random number:

    Add the following to import the the random function

    ```python
    from random import randint

    ```

    Then update the draw_branch function to change how much we shorten each branch.

    ```python
    def draw_branch(len):
        if (len > 5):
            color("brown")
            forward(len)
            right(25)
            draw_branch(len - randint(1,10))
            left(50)
            draw_branch(len - randint(1,10))
            right(25)
            backward(len)
    ```


1. Challenge:  Try changing the shape of the by altering the angle between the branches.  Remember to make sure you rotate back the same amount each time.

1. Challenge: Try adding leaves to the end of the branch.  You can draw a filled circle using the following:

    ```python
        color("green", "green")
        begin_fill()
        circle(10)
        end_fill()
    ```



