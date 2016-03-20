"""
Sample student code that drives the robot based off of joystick values.

Copyright 2016. Pioneers in Engineering.
"""
from api import Gamepads, Robot
import time

while True:
    # For now, get_joysticks actually takes in a string index, not integer
    # This will be fixed in a later update
    gamepad_axis = Gamepads.get_joysticks('0')
    joystick_1_value = gamepad_axis[1]
    #This directly gets the joystick
    joystick_2_value = gamepad_axis[3]
    print[joystick_1_value, joystick_2_value]
    
    #metal_value = Robot.get_metal_detector('802975074932338635676961')
    
   # if metal_value < 35876:
#        Robot.set_led(0, True)
 #       Robot.set_led(1, True)
 #       Robot.set_led(2, True)
 #       Robot.set_led(3, True)
 #   else:
 ###       Robot.set_led(0, False)
#        Robot.set_led(1, False)
#        Robot.set_led(2, False)
#        Robot.set_led(3, False)
#        

    #Drives the robot at 75% of its power, based off of the joystick values.
    Robot.set_motor('motor0', -1 * joystick_1_value)
    Robot.set_motor('motor1', 1 * joystick_2_value)

    time.sleep(.05)