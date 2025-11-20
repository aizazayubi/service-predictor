# app/main.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .model import predict_service  # <- Relative import

import os

app = FastAPI()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
templates = Jinja2Templates(directory=TEMPLATE_DIR)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
def predict(request: Request,
            make: str = Form(...),
            model: str = Form(...),
            year: int = Form(...),
            mileage: int = Form(...)):
    data = {"Make": make, "Model": model, "Year": year, "Mileage": mileage}
    service = predict_service(data)
    return templates.TemplateResponse("index.html", {"request": request, "prediction": service})
