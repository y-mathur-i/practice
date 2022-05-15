import os
import shutil


code_path = os.path.join(os.curdir , "code")

for path in os.walk(os.curdir):
    if path[0].endswith("22") and not path[0].startswith(".\.git"):
        file_path = os.path.join(os.curdir , path[0])
        for file in os.listdir(file_path):
            shutil.copy(os.path.join(file_path, file), code_path)