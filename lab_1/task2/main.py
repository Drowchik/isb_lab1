import os
import sys
import json

project_directory = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_directory)

from task2.utils import auxiliary_function, decryption
from constants import PATH
from general_function import read_file, read_json_dict, write_file


if __name__ == "__main__":
    path = read_json_dict(PATH)
    text = read_file(path["cod2"])
    auxiliary_function(text)
    key = read_json_dict(path["key_for_code"])
    text = decryption(path["res_text2"], key, text)
    write_file(text, path["res_text2"])
    