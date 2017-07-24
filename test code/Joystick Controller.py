import pygame
import serial, time

arduino = serial.Serial('COM3', 115200, timeout=.1)

def main():
    pygame.init()
    WIDTH = 600
    HEIGHT = 600
    pygame.display.set_mode((WIDTH, HEIGHT))
    XboxController = getXboxController()

    if XboxController is None:
        print("problem")
    else:
        print("yay working")
        XboxController.init()

    watch_all_axes(XboxController)
    #watch_buttons(XboxController)
    #watch_hats(XboxController)

def watch_hats(XboxController):
    while(1):
        print(XboxController.get_hat(0))
        pygame.event.pump()

def watch_buttons(XboxController):
    numButtons = XboxController.get_numbuttons()
    print(numButtons)
    while(1):
        for i in range(0,numButtons):
            if(XboxController.get_button(i)):
                print(i)

        pygame.event.pump()

def watch_all_axes(XboxController):
    values = {0 : 0.0,
              1 : 0.0,
              2 : 0.0,
              3 : 0.0,
              4 : 0.0}
    axisCount = XboxController.get_numaxes()
    while(1):
        get_from_arduino()
        for i in range(0,axisCount):
            axisValue = XboxController.get_axis(i)
            if (abs(axisValue - values[i]) > .01):
                values[i] = axisValue
                send_to_arduino(format_data_to_send(i, axisValue))
                #print("axis " + str(i) + " value " + str(int((axisValue)*100)))
        pygame.event.pump()

def getXboxController() -> pygame.joystick.Joystick:
    joystickCount = pygame.joystick.get_count()
    for index in range(0, joystickCount):
        tempStick = pygame.joystick.Joystick(index)
        print(tempStick.get_name())
        if (tempStick.get_name() == "Controller (Xbox 360 Pro Ex)"):
            return tempStick
    return None

def send_to_arduino(info_to_send):
    arduino.write(info_to_send)

def format_data_to_send(axis, axis_value):
    value_to_send = str(int(axis_value * 100))
    return (str(axis) + ':' + value_to_send + "x").encode()



def get_from_arduino():
    data = arduino.readline()
    if data:
        print(data.decode())

if __name__ == "__main__":
    main()


#axis 0 - left stick horizontal
#axis 1 - left stick vertical
#axis 2 - triggers left positive right negative
#axis 3 - right stick vertical
#axis 4 - right stick horizontal

#button 0 - A
#button 1 - B
#button 2 - X
#button 3 - Y
#button 4 - Left Bumper
#button 5 - Right Bumper
#button 6 - Back Button
#button 7 - Start Button
#button 8 - Left Trigger
#button 9 - Right Trigger

#        1
#hat -1 -|- 1
#       -1

#  (L/R, UP/DOWN)