from backend.student import Student
from backend.teacher import Teacher

class ChatMediator:
    def __init__(self):
        self.student = None
        self.teacher = None
        self.messages = []   # Semua pesan disimpan di memori

    def register_student(self, student):
        self.student = student
        student.mediator = self

    def register_teacher(self, teacher):
        self.teacher = teacher
        teacher.mediator = self

    def send_message(self, sender, message):
        if sender == self.student:
            formatted = f"Siswa: {message}"
            self.messages.append(formatted)
            return self.teacher.receive(message)

        elif sender == self.teacher:
            formatted = f"Guru BK: {message}"
            self.messages.append(formatted)
            return self.student.receive(message)

    def get_messages(self):
        return self.messages
