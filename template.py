import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

package_name = "road_sign_detector"

list_of_files = [

    ".gitignore",
    "README.md",

    "backend/main.py",
    "backend/data/.gitkeep",
    "backend/models/.gitkeep",
    f"backend/src/{package_name}/__init__.py",
    f"backend/src/{package_name}/api/__init__.py",
    f"backend/src/{package_name}/api/routes.py",
    f"backend/src/{package_name}/core/__init__.py",
    f"backend/src/{package_name}/core/detection.py",
    f"backend/src/{package_name}/core/recognition.py",
    f"backend/src/{package_name}/processing/__init__.py",
    f"backend/src/{package_name}/processing/pipeline.py",
    f"backend/src/{package_name}/utils/__init__.py",
    f"backend/src/{package_name}/utils/visualizer.py",
    
    "frontend/package.json", 
    "frontend/public/index.html",
    "frontend/public/favicon.ico",
    "frontend/src/index.js", 
    "frontend/src/App.js", 
    "frontend/src/App.css",
    "frontend/src/components/VideoFeed.js", 
    "frontend/src/components/ControlPanel.js", 
    "frontend/src/components/StatusDisplay.js",
    "frontend/src/services/socketService.js",
    "frontend/src/hooks/useSignDetector.js", 
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: '{filedir}' for the file: '{filename}'")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"'{filename}' already exists.")