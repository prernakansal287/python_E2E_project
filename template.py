import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

project_name = "pythonE2EProject"
#for deployment
list_of_files = [
    #".github/workflows/.gitkeep",
    f"src/{project_name}/init.py",
    f"src/{project_name}/components/init.py",
    f"src/{project_name}/components/datainjection.py",
    f"src/{project_name}/components/data_transformation.py/init.py",
    f"src/{project_name}/components/model_trainer.py/init.py",
    f"src/{project_name}/components/model_monitoring.py/init.py",
    f"src/{project_name}/pipelines/init.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",


    f"tests/{project_name}/test_main.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logger.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as p:
            pass
        logger.info(f"Creating empty file: {filepath}")
    else:
        logger.info(f"File already exists: {filepath}, skipping creation.")
