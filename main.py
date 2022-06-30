import os
import shutil

src = "src"
dst = "dst"

file_types = {
    # images
    "tiff": "img", "tif": "img", "png": "img", "jpg": "img", "jpeg": "img", "bmp": "img", "svg": "img", "gif": "img", "eps": "img", "raw": "img",

    # code
    "c": "code", "cpp": "code", "cs":"code", "py": "code", "js": "code", "java": "code", "html": "code", "css": "code", "go": "code", "rs": "code", "r": "code", "ktl": "code", "bf": "code", "b": "code", "asm": "code", "xml": "code", "json": "code", "xaml": "code",

    # documents
    "doc": "docs", "docx": "docs", "xls": "docs", "xlsx": "docs", "ppt": "docs", "pptx": "docs",
}

out_dirs = ["img", "code", "doc", "other"]

for ftype in out_dirs:
    try:
        os.makedirs(f"{dst}/{ftype}")
    except FileExistsError:
        pass

for root, dirs, files in os.walk("src"):
    if len(root) > len(src):
        path = root[len(src):]
    else:
        path = ""

    for file in files:
        file_type = file.split(".")[-1]
        print(f"[FILE] {dst}/{file_types.get(file_type, 'other')}/{file}")
        shutil.copy(f"{root}/{file}", f"{dst}/{file_types.get(file_type, 'other')}/{file}")


