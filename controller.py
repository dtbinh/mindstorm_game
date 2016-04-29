#import the ev3dev library
import ev3dev.ev3 as ev3

#define sensor and motor variables
motorA = ev3.LargeMotor('outA')
motorB = ev3.LargeMotor('outB')

colorSensor = ev3.ColorSensor('in1')

#define a function that makes it possible for the robot to announce the winner
def winSpeak(winner):
    ev3.Sound.speak(winner + 'team wins').wait()

#if the color the sensor detects is either blue, green, yellow or red
#the respective team wins
def colorCheck(sensor):
    if sensor in [2, 3, 4, 5]:
        if sensor == 2:
            print('Blue team wins!')
            winSpeak('blue')
        elif sensor == 3:
            print('Green team wins!')
            winSpeak('green')
        elif sensor == 4:
            print('Yellow team wins!')
            winSpeak('yellow')
        elif sensor == 5:
            print('Red team wins!')
            winSpeak('red')
active = False
def motor(direction):
    # The not is just to lookm good
    if not active:
        if direction == 'right':
            active = True
            motorA.run_timed(time_sp=2000, duty_cycle_sp=50)
            # colorCheck(colorSensor.color())
            active = False
        elif direction == 'left':
            active = True
            motorB.run_timed(time_sp=2000, duty_cycle_sp=50)
            # colorCheck(colorSensor.color())
            active = False
        elif direction == 'forward':
            active = True
            motorA.run_timed(time_sp=2000, duty_cycle_sp=50)
            motorB.run_timed(time_sp=2000, duty_cycle_sp=50)
            # colorCheck(colorSensor.color())
            active = False
        elif direction == 'backward':
            active = True
            motorA.run_timed(time_sp=2000, duty_cycle_sp=-50) #check negative if this doesn't work
            motorB.run_timed(time_sp=2000, duty_cycle_sp=-50)
            # colorCheck(colorSensor.color())
            active = False
