class input_converter:
    def __init__(self, input_mapper, input_transmitter):
        self.input_mapper = input_mapper
        self.input_transmitter = input_transmitter
        self.controller_type = None

    def convert(self, input_id, input_value ):
        if self.controller_type is None: print ('error, no input type')
        if self.controller_type is 0: # this is used to decide which mapper to use. should probably go somewhere else
            control_information = self.input_mapper.map(input_id, input_value)
            if control_information is not None:
                self.input_transmitter.transmit(control_information)
