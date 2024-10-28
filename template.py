import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")

file_list = [
    ".gitignore",
    "Dockerfile",
    ".dockerignore",
    "src/__init__.py",
    "src/agent.py",
    "configuration/config.yml",
    "configuration/.gitkeep", 
    "app.py",
    "logs/agent.log",
    "utils/__init__.py",
    "README.md"
]

for file in file_list:
    file_path = Path(file)
    foldername = file_path.parent
    
    if not foldername.exists() and foldername != Path('.'):
        foldername.mkdir(parents=True)  
        logging.info(f"Folder created: {foldername}")
    
    if not file_path.exists():
        file_path.touch() 
        logging.info(f"File created: {file_path}")
