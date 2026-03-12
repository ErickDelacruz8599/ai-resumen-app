from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

# crear aplicación
app = FastAPI()

# permitir conexión con frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# cargar modelo de resumen en español
modelo = "mrm8488/bert2bert_shared-spanish-finetuned-summarization"

tokenizer = AutoTokenizer.from_pretrained(modelo)
model = AutoModelForSeq2SeqLM.from_pretrained(modelo)

summarizer = pipeline(
    "summarization",
    model=model,
    tokenizer=tokenizer
)

# estructura de datos que recibimos del frontend
class TextRequest(BaseModel):
    text: str
    tipo: str

# endpoint del backend
@app.post("/resumir")
def resumir_texto(request: TextRequest):

    texto = request.text[:1500]

    if request.tipo == "corto":
        max_len = 150
        min_len = 50

    elif request.tipo == "detallado":
        max_len = 700
        min_len = 100


    resumen = summarizer(
        texto,
        max_length=max_len,
        min_length=min_len,
        do_sample=False
    )

    return {"resumen": resumen[0]["summary_text"]}