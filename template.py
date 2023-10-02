import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "mlProject"

list_of_files = [
    # ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

def create_directories(filedir):
    os.makedirs(filedir, exist_ok=True)
    logging.info(f"Created directory: {filedir}")

def create_empty_file(filepath):
    with open(filepath, "w") as f:
        pass
    logging.info(f"Created empty file: {filepath}")

def create_list_of_files():
    for filepath in list_of_files:
        path = Path(filepath)
        filedir, filename = path.parent, path.name
        
        if filedir:
            create_directories(filedir)

        if not path.exists() or os.path.getsize(path) == 0:
            create_empty_file(path)

        else:
            logging.info(f"{filename} already exists!")

if __name__ == "__main__":
    create_list_of_files()