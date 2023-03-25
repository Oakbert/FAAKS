from gpiozero import Device, Button, Motor
from gpiozero.pins.mock import MockFactory, MockPWMPin
from time import sleep

Device.pin_factory = MockFactory(pin_class=MockPWMPin)

motor1 = Motor(6,16)
motor2 = Motor(17,27)

button = Button(2)

# vials is the # of vials that will have fractions in them
# vial is a loop counter
# sleep(x) is to tell the code to wait for x seconds until continuing. Used to adjust run times and stop times
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

for i in range (0):
    print('pushing the button')
    button.pin.drive_low()
    sleep(0.1)
    button.pin.drive_high()
    sleep(0.2)

for i in range (1):
    print('holding the button')
    button.pin.drive_low()
    sleep(5)
    button.pin.drive_high()
    sleep(0.2)