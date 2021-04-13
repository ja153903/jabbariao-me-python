import os
from pathlib import Path
from typing import List

import uvicorn
import fire


def start(host: str = "0.0.0.0", port: int = 8000, reload: bool = True):
    uvicorn.run("jabbariao_me_python.main:app", host=host, port=port, reload=reload)


def create_app():
    """
    This command creates a new app within the project directory
    """
    HOME_DIR = Path(__file__).parent.parent

    def func(app_name: str):
        if os.path.isdir(os.path.join(HOME_DIR, app_name)):
            raise OSError(f"Directory {app_name} already exists")

        ABS_PATH = f"{HOME_DIR}/{app_name}"

        os.mkdir(ABS_PATH)

        files_to_create: List[str] = [
            "api.py", "__init__.py", "crud.py", "models.py", "schemas.py"
        ]

        for file in files_to_create:
            if not os.path.exists(filename := f"{ABS_PATH}/{file}"):
                open(filename, 'w').close()
    
    return fire.Fire(func)