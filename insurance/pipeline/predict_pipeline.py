import sys
import pandas as pd
import numpy as np
from insurance.constant import *
from insurance.exception import InsuranceException
from insurance.util.util import load_object
from insurance.logger import logging
from insurance.entity.artifact_entity import ModelEvaluationArtifact,DataTransformationArtifact

import os,sys



class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            
            print("Before Loading")
            preprocessor_file_path=r'E:\Insurance_premium_prediction\insurance\artifact\data_transformation\2023-07-16-22-13-24\preprocessed\preprocessed.pkl'
            model_file_path=r'E:\Insurance_premium_prediction\saved_models\20230707211336\model.pkl'
            logging.info(features)
            preprocessor=load_object(file_path=preprocessor_file_path)
            model=load_object(file_path=model_file_path)
            logging.info('after loading')
            # Convert the input features to a pandas DataFrame with a single sample
            

   
            preds = model.predict((features))
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
        logging.info('get_data_as_data_frame')
        try:
            custom_data_input_dict = {
                "age": [self.age],
                "sex": [self.sex],
                "bmi": [self.bmi],
                "children": [self.children],
                "smoker": [self.smoker],
                "region": [self.region]
               
            }
            s=pd.DataFrame(custom_data_input_dict)
            logging.info(pd.DataFrame(custom_data_input_dict))
            print(s.head())

            return pd.DataFrame(custom_data_input_dict,columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])

        except Exception as e:
            raise InsuranceException(e, sys) from e