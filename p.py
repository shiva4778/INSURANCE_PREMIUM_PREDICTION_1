from insurance.entity.artifact_entity import DataTransformationArtifact, DataIngestionArtifact
from insurance.config import configuration
import numpy as np
import pandas as pd
from insurance.util.util import load_object

preprocessor_file_path = r'E:\Insurance_premium_prediction\insurance\artifact\data_transformation\2023-07-16-22-13-24\preprocessed\preprocessed.pkl'
model_file_path = r'E:\Insurance_premium_prediction\saved_models\20230707211336\model.pkl'

def model(features):
    preprocessor = load_object(file_path=preprocessor_file_path)
    model = load_object(file_path=model_file_path)

    # Convert the input features to a pandas DataFrame with a single sample
    features_df = pd.DataFrame([features], columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])

   
    preds = model.predict((features_df))
    return preds

# Example usage:
print(model([18.0, "male", 18.0, 2.0, "yes", "northeast"]))

if __name__ == "__main__":
    pass
