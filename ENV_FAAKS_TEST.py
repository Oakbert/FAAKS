# An addition that would like to be made is a coordinate system setup to tell the motors where to go instead of how long to run for
# This would remove the issue of friction causing the wheel to slide, throwing the robot off and allowing it fix itself rather than being offset for the rest of the 
# collection. However, I am not sure how to do this and have not been able to find any documentation on this yet. I know that it is possible but I have not figured
# it out yet 

# Motor RPM adjustments will need to be added in addition to sleep time, these changes should not be difficult but it is just a matter of getting the RPI setup 
# and running some tests to determine what sleep time and RPM speed is the best

from gpiozero import Device, Button, Motor
from gpiozero.pins.mock import MockFactory, MockPWMPin
from time import sleep

# MockFactory is required to simulate RPI pins, this will be removed and adjusted accordingly once the RPI is setup and actual pins are defined on the RPI
Device.pin_factory = MockFactory(pin_class=MockPWMPin)

motor1 = Motor(6,16)
motor2 = Motor(17,27)

button = Button(2)

# vials is the # of vials that will have fractions in them
# vial is a loop counter
# sleep(x) is to tell the code to wait for x seconds until continuing. Used to adjust run times and stop times
# this script is currently setup to run 100 fractions, however this can be adjusted depending on how many fractions will be collected by changing the vial parameter
def Run_Column(vial,vials,time):
    if vial != 100:
        for i in range (vials):
            motor1.forward()
            sleep(0.67)
            motor1.stop()
            sleep(time)
            vial = vial + 1
            print('vial', vial, 'has finished!')
        motor2.forward()
        sleep(0.67)
        motor2.stop()
    if vial == 100:
        return
    else:
        Run_Column_Reverse(vial,vials,time)

def Run_Column_Reverse(vial,vials,time):
    if vial != 100:
        for i in range (vials):
            motor1.reverse()
            sleep(0.67)
            motor1.stop()
            sleep(time)
            vial = vial + 1
            print('vial', vial, 'has finished!')
        motor2.forward()
        sleep(0.67)
        motor2.stop()
    if vial == 100:
        return
    else: 
        Run_Column(vial,vials,time)

btn_idx = 0

def call():
    global btn_idx
    time_list = [0, 1.67, 3.33, 5]
    list(map(int,time_list))
    Run_Column(0, 10, time_list[btn_idx])
    print('Column has Finished')

button.hold_time = 3
was_held = False

def held():
    global was_held
    was_held = True
    print('button was held not pressed')
    call()

def released():
    global was_held
    if not was_held:
        pressed()

def pressed():
    print("button was pressed not held")
    global btn_idx
    if btn_idx == 4:
        btn_idx = 0
    btn_idx += 1

button.when_held = held
button.when_released = released


# for loop used to choose which size column will be ran by simulating button presses. This loop will be removed after setting up the RPI because we will be able to 
# physically press the button, removing the need for simulation
for i in range (0):
    print('pushing the button')
    button.pin.drive_low()
    sleep(0.1)
    button.pin.drive_high()
    sleep(0.2)

# for loop used to run the fraction collector after selecting the size of the column by simulating button hold. This loop will be removed after setting up the RPI
# because we will be able to physically hold the button, removing the need for simulation
for i in range (1):
    print('holding the button')
    button.pin.drive_low()
    sleep(5)
    button.pin.drive_high()
    sleep(0.2)
