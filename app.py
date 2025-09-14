from src.pythonE2EProject.logger import logging
from src.pythonE2EProject.exception import CustomException
import sys


if __name__ == "__main__":
    logging.info("Starting the application...")

    try:
        
        # Simulating an exception
        a=1 / 0
    except Exception as e:
        logging.info("custom exception called")
        raise CustomException(e, sys) from e
    