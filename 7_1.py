from os import path, mkdir
from collections import defaultdict

dirs = defaultdict(list)
dirs["my_project"] = ["setting", "mainapp", "adminapp", "authapp"]
for key in dirs:
    if not path.exists(key):
        mkdir(key)
        for val in dirs[key]:
            mkdir(path.join(key, val))
