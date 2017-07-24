#input_id: (type, index) 1 = axes, 2 = button, 3 = hat
#input value: axes = 0 - 1, button is true, hat is tuple

#Control ID
CAMERA_PAN = 3
CAMERA_TILT = 4

#INPUT ID
RIGHT_STICK_VERTICAL = 3
RIGHT_STICK_HORIZONTAL = 4

def map(input_id, input_value):
    if(input_id[0] == 1): return map_axes(input_id[1], input_value)
    elif(input_id[0] == 2): return map_button(input_id[1])
    elif(input_id[0] == 3): return map_hat(input_id[1], input_value)
    return None

def map_axes(axes_index, axis_value):
    if(axes_index == RIGHT_STICK_HORIZONTAL): return (CAMERA_PAN, axis_value)
    if(axes_index == RIGHT_STICK_VERTICAL): return(CAMERA_TILT, axis_value)
    return None

def map_button(button_index):
    return None

def map_hat(hat_index, hat_tuple):
    return None




# axis 0 - left stick horizontal
# axis 1 - left stick vertical
# axis 2 - triggers left positive right negative
# axis 3 - right stick vertical
# axis 4 - right stick horizontal

# button 0 - A
# button 1 - B
# button 2 - X
# button 3 - Y
# button 4 - Left Bumper
# button 5 - Right Bumper
# button 6 - Back Button
# button 7 - Start Button
# button 8 - Left Trigger
# button 9 - Right Trigger

#        1
# hat -1 -|- 1
#       -1

#  (L/R, UP/DOWN)

#right stick is camera
