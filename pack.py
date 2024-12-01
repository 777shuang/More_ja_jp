import zipfile
import shutil
import os

VERSION="1.2"
FILENAME=f'more_ja_jp-{VERSION}'

shutil.make_archive(FILENAME, 'zip', os.path.dirname(__file__), 'assets')

with zipfile.ZipFile(FILENAME+'.zip', 'a') as zf:
    zf.write("pack.mcmeta")
    zf.write("pack.png")