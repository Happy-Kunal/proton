class IntFloatError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return (self.value + " is not valid.\n Only integers and floats are allowed.")