from functions.to_code_error import to_code_error


class RepositoryException(Exception):
    """Base exception for Repository-related errors."""

    def __init__(self, message, code=None):
        super().__init__(self)
        self.message = message
        self.code = code
        self.code_error = to_code_error(code)
