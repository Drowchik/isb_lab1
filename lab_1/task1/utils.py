import json
import os
import sys

from enum import Enum

project_directory = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_directory)

from constants import ALPHABET, path_js
from general_function import read_file, read_json_dict, write_file

class Mode(Enum):
    ENCRYPT = 1
    DECRYPT = 2


def encryption(document: str, mode: Enum, shift: int = 3) -> str:
    """
        Encrypts or decrypts the received document
    Args:
        document (str): the file that the actions will be performed on
        mode (Enum): decryption or encryption
        shift (int, optional): Caesar's shift. Defaults to 3.

    Returns:
        str: processed text
    """
    try:
        text = ""
        for char in document:
            if char in ALPHABET:
                pos = ALPHABET.index(char)
                if mode == Mode.ENCRYPT:
                    index = (pos + shift) % 33
                else:
                    index = (pos-shift) % 33
                text += (ALPHABET[index])
            else:
                text += (char)

        return text
    except Exception:
        print("All bad")


def create_json(path_json: str, shift: int = 3):
    """
        create json file (dict, key) for text
    Args:
        path_json (_type_): path file
        shift (int): shift for text
    """
    my_dict = {}
    for i in range(len(ALPHABET)):
        my_dict[ALPHABET[i]] = ALPHABET[(i+shift) % len(ALPHABET)]
    try:
        with open(path_json, "w", encoding="utf-8") as f:
            json.dump(my_dict, f, ensure_ascii=False, indent=1)
    except FileNotFoundError:
        print("Что-то пошло не так, невозможно открыть данный файл")


if __name__ == "__main__":
    dict_path = read_json_dict(path_js)
    res = read_file(dict_path["source_text1"])
    text = encryption(res, Mode.ENCRYPT)
    write_file(text, dict_path["text1_decrypt"])
    create_json(dict_path["json_file1"])

