from fastapi import FastAPI
from pydantic import BaseModel
import base64

app = FastAPI()

class InputText(BaseModel):
    input: str

@app.post("/endpoint1")
def encode_base64(data: InputText):
    encoded = base64.b64encode(data.input.encode()).decode()
    return {"result": encoded}

@app.post("/endpoint2")
def reverse_or_upper(data: InputText):
    text = data.input
    if len(text) % 2 == 0:
        return {"result": text[::-1]}
    return {"result": text.upper()}

@app.post("/endpoint3")
def remove_vowels(data: InputText):
    vowels = "aeiouAEIOU"
    return {"result": ''.join(c for c in data.input if c not in vowels)}

@app.post("/endpoint4")
def sort_characters(data: InputText):
    return {"result": ''.join(sorted(data.input))}

@app.post("/endpoint5")
def redact_special(data: InputText):
    return {"result": ''.join(['*' if not c.isalnum() else c for c in data.input])}
