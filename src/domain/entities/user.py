class User:
    def __init__(self, id: int | None, name: str, email: str, password: str):
        self.id = id
        self.name = name
        self.email = email
        self.password = password