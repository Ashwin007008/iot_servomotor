from pyfirmata import Arduino , SERVO , util
from time import sleep
port = 'COM5'
pin = 10
board = Arduino (port)
board.digital [pin] .mode = SERVO
def rotateservo (pin,angle) :
    board.digital [pin].write(angle)
    sleep (0.015)
while True :
    x = input(" input : ")
    print(x)
    if x == "1" :
        print("if")
        for i in range ( 0,180 ) :
            rotateservo ( pin , i )
    
    if x == "2" :
        for i in range ( 0,90 ) :
            rotateservo ( pin , i )

    if x == "3" :
        for i in range ( 0,270 ) :
            rotateservo ( pin , i )