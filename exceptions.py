

class ArgumentNotSetError(Exception):
    def __init__(self, argument, message):
        self.argument = argument
        self.message = message
        # super().__init__(self.message)