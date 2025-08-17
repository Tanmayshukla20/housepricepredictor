import os
import sys
from src.housepricepredictor.exception import CustomException
from src.housepricepredictor.logger import logging
import pandas as pd
from src.housepricepredictor.utils import read_sql_data

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info("Starting data ingestion...")

            # ✅ Step 1: Read data from MySQL (via helper)
            df = read_sql_data()   # <-- make sure your utils.py has this function

            logging.info("Reading from MySQL completed successfully")

            # ✅ Step 2: Create artifacts directory
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # ✅ Step 3: Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # ✅ Step 4: Split train/test
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # ✅ Step 5: Save train/test
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data Ingestion is completed successfully")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)
