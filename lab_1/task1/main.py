import os
import sys
import json

project_directory = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_directory)

from task1.utils import create_json, encryption, Mode
from constants import PATH
from general_function import read_file, read_json_dict, write_file


if __name__ == "__main__":
    dict_path = read_json_dict(PATH)
    res = read_file(dict_path["source_text1"])
    text = encryption(res, Mode.ENCRYPT)
    write_file(text, dict_path["text1_decrypt"])
    create_json(dict_path["json_file1"])
    