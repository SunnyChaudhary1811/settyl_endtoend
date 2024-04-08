# test_model.py

import pandas as pd
import joblib

# Load the trained model
model = joblib.load("models/trained_model.pkl")

# Load sample data for testing
sample_data = pd.DataFrame({
    "numeric_column1": [1.0, 2.0, 3.0],
    "numeric_column2": [4.0, 5.0, 6.0],
    "categorical_column": ["A", "B", "C"],
    "externalStatus": ["example_status_1", "example_status_2", "example_status_3"]
})

# Perform inference
predictions = model.predict(sample_data)

# Print predictions
print("Predictions:")
for prediction in predictions:
    print(prediction)
