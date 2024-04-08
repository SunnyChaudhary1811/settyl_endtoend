from pydantic import BaseModel

class PredictionRequest(BaseModel):
    externalStatus: str

class PredictionResponse(BaseModel):
    predicted_internalStatus: str
