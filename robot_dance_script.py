from Myro import *
init("sim")
def forwardback (x):
    for i in range(0,x):
        forward(3, 0.5)
        backward(3, 0.5)
        stop
forwardback(14)
turnRight(10, 4.5)
turnLeft(10, 4.5)

def cross (x):
    for i in range(0,x):
        forward(5, 0.25)
        backward(5, 0.25)
        turnLeft(9, .2)
        wait(0.5)
        stop
cross (6)

def jazzsquare (x):
    for i in range (0,x):
        forward(4,.5)
        turnRight(5, 0.5)
        stop
jazzsquare (3)
turnRight(10, 4.5)
turnLeft(10,4.5)
cross(8)
jazzsquare(2)
turnRight(10, 2)
turnLeft(10,2)

def crazy (x):
    for i in range (0,x):
        forward(10, .1)
        backward(10, .1)
        turnRight(10, 2)
        turnLeft(10, 2)
        stop
crazy(4)
cross(4)

def tensecondcircle (x):
    for i in range (0,x):
        move(3,3)
        wait(10)
        stop
        
tensecondcircle(1)
cross(4)
jazzsquare(4)

def sevensecondcircle (x):
    for i in range (0,x):
        move(3,3)
        wait(7)
        stop

sevensecondcircle(1)
cross(3)
jazzsquare(4)



        
        