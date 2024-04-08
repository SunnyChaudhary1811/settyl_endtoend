import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
import joblib

# Configure logging
logging.basicConfig(filename='training.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    # Load data
    data_url = "C:/settyl_endtoend/data/dataset.csv"
    data = pd.read_csv(data_url)

    # Check for missing values
    logging.info("Checking for missing values...")
    logging.info(data.isnull().sum())

    # Split data into features and target
    X = data.drop(columns=["internalStatus"])
    y = data["internalStatus"]

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Check if X_train and y_train contain NaN values
    logging.info("Checking for missing values in train set...")
    logging.info(X_train.isnull().sum())
    logging.info(y_train.isnull().sum())

    # Define preprocessing steps
    categorical_features = ["externalStatus"]
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', categorical_transformer, categorical_features)
        ])

    # Append classifier to preprocessing pipeline
    clf = Pipeline(steps=[('preprocessor', preprocessor),
                          ('classifier', RandomForestClassifier())])

    # Fit the model
    logging.info("Training the model...")
    clf.fit(X_train, y_train)

    # Save the model
    logging.info("Saving the model...")
    joblib.dump(clf, r"C:\settyl_endtoend\models\trained_model.pkl")

    logging.info("Training completed successfully.")

except Exception as e:
    # Log any exceptions
    logging.error(f"An error occurred: {str(e)}")





