class StroryException(Exception):
    def __init__(self, status_code: int, name: str):
        self.name = name
        self.status_code = status_code