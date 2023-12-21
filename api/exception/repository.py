from functions.to_code_error import to_code_error


class RepositoryException(Exception):
    """Base exception for Repository-related errors."""

    def __init__(self, code):
        super().__init__(self)
        self.code = code
        self.code_error = to_code_error[code][0]
        self.description = to_code_error[code][1]
