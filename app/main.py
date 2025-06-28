from fastapi import FastAPI
from pydantic import BaseModel
import base64

app = FastAPI()

class InputText(BaseModel):
    input: str

@app.post("/endpoint1")
def endpoint1(data: InputText):
    return {"result": base64.b64encode(data.input.encode()).decode()}

@app.post("/endpoint2")
def endpoint2(data: InputText):
    return {"result": data.input[::-1] if len(data.input) % 2 == 0 else data.input.upper()}

@app.post("/endpoint3")
def endpoint3(data: InputText):
    return {"result": ''.join(c for c in data.input if c.lower() not in "aeiou")}

@app.post("/endpoint4")
def endpoint4(data: InputText):
    return {"result": ''.join(sorted(data.input))}

@app.post("/endpoint5")
def endpoint5(data: InputText):
    return {"result": ''.join('*' if not c.isalnum() else c for c in data.input)}
