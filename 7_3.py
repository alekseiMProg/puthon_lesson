import shutil
from os import walk


for paths, dirs, files in walk("my_project"):
    if paths.endswith("templates"):
        shutil.copytree(paths, "templates", dirs_exist_ok=True)