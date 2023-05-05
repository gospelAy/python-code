from pathlib import Path


def class_work():
    my_list = []
    my_folder = Path.cwd()/"class_work_folder"
    my_folder.mkdir()
    my_folder.exists()
