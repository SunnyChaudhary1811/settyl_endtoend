from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("C:/settyl_endtoend/models/trained_model.pkl")

# Define FastAPI app
app = FastAPI()


# Define request and response models
class PredictionRequest(BaseModel):
    externalStatus: str


class PredictionResponse(BaseModel):
    predicted_internalStatus: str


# Define API endpoint
@app.post("/predict", response_model=PredictionResponse)
def predict_status(request: PredictionRequest):
    # Preprocess input data
    input_data = pd.DataFrame([vars(request)])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Return prediction
    return {"predicted_internalStatus": prediction}
