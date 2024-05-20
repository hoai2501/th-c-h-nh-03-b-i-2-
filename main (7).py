from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Operands(BaseModel):
    a: float
    b: float

@app.post("/add")
def add(operands: Operands):
    return {"result": operands.a + operands.b}

@app.post("/subtract")
def subtract(operands: Operands):
    return {"result": operands.a - operands.b}

@app.post("/multiply")
def multiply(operands: Operands):
    return {"result": operands.a * operands.b}

@app.post("/divide")
def divide(operands: Operands):
    return {"result": operands.a / operands.b if operands.b != 0 else "Error: Division by zero"}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Cho phép CORS cho tất cả các nguồn và phương thức
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Định nghĩa các API của bạn ở đây
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Hoặc chỉ định các origin cụ thể
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Operands(BaseModel):
    a: float
    b: float

@app.post("/add")
def add(operands: Operands):
    return {"result": operands.a + operands.b}

@app.post("/subtract")
def subtract(operands: Operands):
    return {"result": operands.a - operands.b}

@app.post("/multiply")
def multiply(operands: Operands):
    return {"result": operands.a * operands.b}

@app.post("/divide")
def divide(operands: Operands):
    return {"result": operands.a / operands.b if operands.b != 0 else "Error: Division by zero"}
