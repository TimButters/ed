class EdDbAlreadyExists(Exception):
    pass


class EdDbNotConnected(Exception):
    def __init__(self):
        message = """Not currently connected to an Excel database.
        Run `db.connect(dbname)` to connect to an existing Ed."""
        super().__init__(message)


class EdTableNotFound(Exception):
    pass


class EdTableAlreadyExists(Exception):
    pass
