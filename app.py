# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Inicializa a API
app = FastAPI(title="Sankofa AI API")

# Carrega tokenizer e modelo
tokenizer = AutoTokenizer.from_pretrained("sankofa/sankofa-ai")
model = AutoModelForSequenceClassification.from_pretrained("sankofa/sankofa-ai")

# Define o formato do request
class RequestBody(BaseModel):
    text: str

# Endpoint principal
@app.post("/classify")
def classify_text(body: RequestBody):
    inputs = tokenizer(body.text, return_tensors="pt")
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1)
    label_idx = torch.argmax(probs).item()
    label = "Não racista" if label_idx == 0 else "Racista"
    return {"label": label, "score": float(probs[0, label_idx])}
