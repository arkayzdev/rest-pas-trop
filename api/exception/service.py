from functions.to_code_error import to_code_error


class ServiceException(Exception):
    """Base exception for Service-related errors."""

    def __init__(self, code):
        super().__init__(self)
        self.code = code
        self.code_error = to_code_error[code][0]
        self.description = to_code_error[code][1]
