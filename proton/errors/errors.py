class IntFloatError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return (self.value + " is not valid.\n Only integers and floats are allowed.")

class OnlyMatrixAllowed(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return (self.value + " is not valid.\n Only matrix are allowed.")

class OrderMismatch(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return (self.value + " order mismatch.\n Cannot compute this operation.")