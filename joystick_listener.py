import pygame

class joystick_listener:
    def __init__(self, input_converter):
        self.AXIS = 1
        self.BUTTON = 2
        self.HAT = 3
        self.axis_values = []
        self.converter = input_converter
        pygame.init()
        pygame.display.set_mode((1, 1))


#this should be refactored eventually. this class should work for any type of joystick... hmmm
    def get_xbox_controller(self) -> pygame.joystick.Joystick:
        xbox_controller = ''
        self.converter.controller_type = 0
        joystickCount = pygame.joystick.get_count()
        for index in range(0, joystickCount):
            temp_stick = pygame.joystick.Joystick(index)
            if (temp_stick.get_name() == "Controller (Xbox 360 Pro Ex)"):
                xbox_controller = temp_stick
                break

        if xbox_controller == '': raise Exception
        xbox_controller.init()
        self.get_initial_axis_values(xbox_controller)
        return xbox_controller


    def get_control_inputs(self, controller):
        while (True):
            self.check_axis(controller)
            self.check_buttons(controller)
            self.check_hat(controller)
            pygame.event.pump()

    def get_initial_axis_values(self, controller):
        axis_array = []
        number_of_axis = controller.get_numaxes()

        for axis_index in range(0, number_of_axis):
            axis_array.append(controller.get_axis(axis_index))

        self.axis_values = axis_array

    def check_axis(self, controller):
        number_of_axis = controller.get_numaxes()

        for axis_index in range(0, number_of_axis):
            axes_value = controller.get_axis(axis_index)
            if (abs(axes_value - self.axis_values[axis_index]) > .01):
                self.axis_values[axis_index] = axes_value
                self.converter.convert((self.AXIS, axis_index), axes_value)

    def check_buttons(self, controller):
        num_buttons = controller.get_numbuttons()

        for button_index in range(0, num_buttons):
            if (controller.get_button(button_index)):
                self.converter.convert((self.BUTTON, button_index), True)

    def check_hat(self, controller):
        number_of_hats = controller.get_numhats()
        for hat_index in range(0, number_of_hats):
            hat_value = controller.get_hat(hat_index)
            if (hat_value != (0, 0)):
                self.converter.convert((self.HAT, hat_index), hat_value)

