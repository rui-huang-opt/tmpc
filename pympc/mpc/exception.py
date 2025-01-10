class MPCTypeException(Exception):
    def __init__(self, name: str, tp: str):
        message = "The type of " + name + " must be " + tp + "!"
        super().__init__(message)


class MPCDimensionException(Exception):
    def __init__(self, *obj: str):
        message = "The dimensions of " + ", ".join(obj) + " do not match!"
        super().__init__(message)


class MPCTerminalSetTypeException(Exception):
    def __init__(self):
        super().__init__("The terminal set type must be 'zero', 'ellipsoid' or 'polyhedron'")


class MPCNotImplementedException(Exception):
    def __init__(self, function: str):
        message = "The function " + function + " has not been implemented yet!"
        super().__init__(message)
