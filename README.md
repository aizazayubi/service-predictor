# Garage Service Predictor

A simple web application to predict the next service type for a vehicle using machine learning. Built with **FastAPI**, **scikit-learn**, and a simple HTML interface.

---

## Features

- Predict the next service type based on:
  - Vehicle Make & Model
  - Year
  - Mileage
- User-friendly HTML form with dropdowns for Make and Model
- Trained on sample vehicle service dataset
- FastAPI backend with RESTful endpoints

---

## Folder Structure

```

service-predictor/
├─ app/
│  ├─ **init**.py
│  ├─ main.py           # FastAPI application
│  ├─ model.py          # ML model and prediction logic
│  └─ templates/
│     └─ index.html     # HTML form interface
├─ venv/                # Virtual environment (ignored in git)
├─ data.csv             # Sample dataset
└─ requirements.txt

````

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/aizazayubi/service-predictor.git
cd service-predictor
````

2. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Make sure you have `python-multipart` installed for form handling:

```bash
pip install python-multipart
```

---

## Usage

Run the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open your browser and visit:

```
http://127.0.0.1:8000
```

* Select Vehicle Make & Model from the dropdowns
* Enter Year and Mileage
* Click **Predict Service** to see the predicted next service

---

## Dependencies

* fastapi
* uvicorn
* pandas
* scikit-learn
* jinja2
* python-multipart

---

## License

This project is open-source and free to use.

```
