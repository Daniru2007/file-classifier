import os
import shutil

src = "src"
dst = "dst"

for root, dirs, files in os.walk("src"):
    print(f"root {root}")
    for dir in dirs:
        try:
            path = root
            if len(root) > len(src):
                path = root[len(src):]
            else:
                path = ""
            os.makedirs(f"{dst}/{path}/{dir}")
            print(f"[FOLDER] creating folder {path}\\{dir}...")
        except FileExistsError:
            pass

    for file in files:
        pass


