import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path,exist_ok=True)

#basically this file consist of cobination of logging and file handling
log_file=os.path.join(log_path,LOG_FILE)


#This  is the function which will define the format like how w9ill bw the logging message displayed
logging.basicConfig(
    filename=log_file,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)