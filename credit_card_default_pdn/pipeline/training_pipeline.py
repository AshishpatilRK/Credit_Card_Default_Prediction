import os
import sys
from credit_card_default_pdn.logging.logger import logging
from credit_card_default_pdn.exceptions.exception import CustomException
import pandas as pd

from credit_card_default_pdn.components.data_ingestion import DataIngestion
from credit_card_default_pdn.components.data_transformation import DataTransformation
from credit_card_default_pdn.components.model_trainer import ModelTrainer


if __name__=='__main__':
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr,test_arr,_=data_transformation.initaite_data_transformation(train_data_path,test_data_path)
    model_trainer=ModelTrainer()
    model_trainer.initate_model_training(train_arr,test_arr)



