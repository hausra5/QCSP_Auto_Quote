class Customer:
    running_quotes = {}

    def __init__(self, name, email, phone = None, address = None):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    @classmethod
    def add_quote(cls, name, quote):
        cls.running_quotes[name] = quote