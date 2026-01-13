class User:
    def __init__(self, name, mediator=None):
        self.name = name
        self.mediator = mediator

    def send(self, message):
        return self.mediator.send_message(self, message)

    def receive(self, message):
        return f"{self.name} menerima: {message}"
