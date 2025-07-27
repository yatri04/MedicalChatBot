import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
list_of_files=[
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials/ipynb"
]
for file in list_of_files:
    file_path = Path(file)
    if not file_path.exists():
        logging.info(f"Creating file: {file}")
        file_path.parent.mkdir(parents=True, exist_ok=True)  # Create parent directories if they don't exist
        file_path.touch()  # Create the file
    else:
        logging.info(f"File already exists: {file}")    