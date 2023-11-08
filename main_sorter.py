import os
from pathlib import Path
import concurrent.futures
import shutil

import logging

from format_dictionary import dic

ignored_folders = ["archives", "video", "audio", "documents", "images"]


def find_files(path):
    files_found = set()
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            files_found.add(Path(file_path))
    return files_found


def file_move(file):
    file_format = file.suffix.lower()
    if file_format in dic:
        """known format move to respective folder"""
        directory_path = Path(dic[file_format])
        directory_path.mkdir(exist_ok=True)
        shutil.move(file, directory_path / file.name)

    else:
        """unknown format move to other folder"""
        directory_path = Path("other")
        directory_path.mkdir(exist_ok=True)
        shutil.move(file, directory_path / file.name)


if __name__ == "__main__":
    path_raw = input("Please enter a path to the folder to be organized: ")
    path = Path(path_raw)
    os.chdir(path)

    files_found = find_files(path)

    with concurrent.futures.ThreadPoolExecutor(2) as executor:
        for _ in executor.map(file_move, files_found):
            pass

    print("operation done")
