import sys
import pandas as pd
from insurance.exception import InsuranceException
from insurance.util import load_object
import os
import sys

age,sex,bmi,children,smoker,region,expenses

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessed.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise InsuranceException(e,sys) from e



class CustomData:
    def __init__(  self,
        age: int,
        sex: str,
        bmi:int,
        children: int,
        smoker: str,
        region: str):

        self.age = age

        self.sex = sex

        self.bmi =bmi

        self.children = children

        self.smoker = smoker

        self.region = region

        

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "age": [self.age],
                "sex": [self.sex],
                "bmi": [self.bmi],
                "children": [self.children],
                "smoker": [self.smoker],
                "region": [self.region]
               
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise InsuranceException(e, sys) from e