import sys
from src.housepricepredictor.exception import CustomException
from src.housepricepredictor.logger import logging
from src.housepricepredictor.components.data_ingestion import DataIngestion


if __name__ == "__main__":
    logging.info("the execution has started")

    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion = DataIngestion() 
        data_ingestion .initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)
