from joystick_listener import joystick_listener
from input_converter import input_converter
import xbox_control_mapper
import input_transmitter

input_converter = input_converter(xbox_control_mapper, input_transmitter)

j__controller = joystick_listener(input_converter)
controller = j__controller.get_xbox_controller()

j__controller.get_control_inputs(controller)