class SetTypeException(Exception):
    def __init__(self, name: str, set_type: str, tp: str):
        message = "The type of the " + name + " of " + set_type + " must be " + tp + "!"
        super().__init__(message)


class SetDimensionException(Exception):
    def __init__(self, *args: str):
        message = "The dimensions of " + ", ".join(args) + "do not match!"
        super().__init__(message)


class SetCalculationException(Exception):
    def __init__(self, set_type: str, operation: str, other: str):
        message = "A " + set_type + " can only be " + operation + " by a " + other + "!"
        super().__init__(message)


class SetNotImplementedException(Exception):
    def __init__(self, function: str, set_type: str):
        message = "The function " + function + " of " + set_type + " has not been implemented yet!"
        super().__init__(message)


class SetPlotException(Exception):
    def __init__(self):
        super().__init__("Only 2D set can be plotted!")
