from functions.to_code_error import to_code_error


class ServiceException(Exception):
    """Base exception for Service-related errors."""

    def __init__(self, message, code=None):
        super().__init__(self)
        self.message = message
        self.code = code
        self.code_error = to_code_error(code)
