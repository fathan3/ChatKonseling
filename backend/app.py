from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from backend.chat_mediator import ChatMediator
from backend.student import Student
from backend.teacher import Teacher

import os

app = FastAPI()

# === Izinkan frontend mengakses backend ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Absolute path untuk folder frontend ===
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

# === Serving Frontend ===
app.mount("/frontend", StaticFiles(directory=FRONTEND_DIR), name="frontend")

# === Homepage → index.html ===
@app.get("/")
def read_root():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

@app.get("/chat.html")
def get_chat_html():
    return FileResponse(os.path.join(FRONTEND_DIR, "chat.html"))

# === Inisialisasi mediator dan user ===
mediator = ChatMediator()
student = Student("Siswa")
teacher = Teacher("Guru BK")

mediator.register_student(student)
mediator.register_teacher(teacher)

# === Endpoint kirim pesan ===
@app.post("/send")
def send_message(sender: str, message: str):
    if sender == "student":
        result = student.send(message)
    else:
        result = teacher.send(message)
    return {"status": "ok", "response": result}

# === Endpoint ambil pesan ===
@app.get("/messages")
def get_messages():
    return mediator.get_messages()