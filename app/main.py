import joblib
import numpy as np
import pandas as pd
from fastapi import FastAPI, status
import uvicorn
from pydantic import BaseModel
from pathlib import Path

## Create a instance 
app = FastAPI(
    title = "Telco Custumer Churn Detection API",
    description = "An API that utilizes a Machine Learning model(XGBoost) to detect whether the customers from a Telco company will churns or not the company based on several features.",
    version = "0.1.0",
    debug = True
    )

## path model
version = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent
# Load Model
with open(f"{BASE_DIR}/customer_churn_xgb_model-{version}.pkl", "rb") as f:
    model = joblib.load(f)


## Schema validation
class Features(BaseModel):
    Gender: int
    Parther: int
    Dependents: int
    Tenure_Months: int
    Mutiple_lines: int
    Internet_services: int
    Online_Security: int
    Online_Backup: int
    Device_Protection: int
    Tech_support: int
    Streaming_tv: int
    Streaming_movies: int
    Contract: int
    Paperless_billing: int
    Payment_method: int
    Monthly_charges: float
    cltv: float

# get path
@app.get("/")
def home():
    return {"health_check": "OK", "model_version": "0.1.0"}

# Post path
@app.post("/predict", status_code= status.HTTP_201_CREATED)
def predict(data: Features):
    
    # Features
    features = data.dict()
    # Dataframe from features
    data_f = pd.DataFrame(features, index = [0])
    # predictions
    predictions = model.predict(data_f)

    proba = model.predict_proba(data_f)
    proba_nochurn = np.round((proba[0][0])*100, 2)
    proba_churn = np.round((proba[0][1])*100, 2)

    if predictions == 1:
        return {f"The probability that the customer leaves the company is {proba_churn} percent"}
    elif predictions == 0:
        return {f"The probability that the customer stays in the company is {proba_nochurn} percent"}
    
