# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass

class AlphaError(Error):
    """Raised when the input value is not a letter"""
    pass

class OffGridError(Error):
    """Raised when the rover will fall off the grid"""
    pass

class CrashError(Error):
    """Raised when the rover will crash into another rover"""
    pass