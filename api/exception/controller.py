from functions.to_code_error import to_code_error


class ControllerException(Exception):
    """Base exception for controller-related errors."""

    def __init__(self, message, code=None):
        super().__init__(self)
        self.message = message
        self.code = code
        self.code_error = to_code_error(code)

    def to_dict(self):
        """Convert the exception to a dictionary for JSON serialization."""
        error_dict = {
            "code": self.code,
            "error": self.code_error,
            "message": self.message,
        }
        return error_dict

    def to_code(self):
        return self.code
