from src.pythonE2EProject.logger import logging
from src.pythonE2EProject.exception import CustomException
import sys
from src.pythonE2EProject.components.data_injection import DataIngestion    


if __name__ == "__main__":
    logging.info("Starting the application...")

    try:
        #data_injection_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed successfully.")
        
        # Simulating an exception
        #just for testing the custom exception
        a=1 / 0

    except Exception as e:
        logging.info("custom exception called")
        raise CustomException(e, sys) from e
    