import os
import sys
import json
from collections import Counter
from typing import Dict


project_directory = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_directory)

from general_function import read_file, write_file


def auxiliary_function(text: str) -> None:
    """
        This auxiliary function for encryption text
    Args:
        text (str): document for encryption
    """
    info_words = Counter(text)
    print(f"Информация по частоте встречи символов: {info_words}")
    words_in_text = text.split(info_words.most_common(1)[0][0])
    print(f"Список слов разделённых пробелами: {words_in_text}")
    words_in_text = sorted(words_in_text, key=lambda x: len(x))
    print(
        f"Список отсортированных по длине слов разделённых пробелами: {words_in_text}")


def read_json_dict(path: str) -> Dict:
    """ 
        read json file
    Args:
        path (str): the path for the json file

    Returns:
        Dict: keys
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Невозможно открыть файл.")


def decryption(path_res: str, path: str, text: str) -> str:
    """
        decrypts the text by the key
    Args:
        path_res (str): _description_
        path (str): the path for the key
        text (str): text ecryption

    Returns:
        str: result_text
    """
    key = read_json_dict(path)
    res_text = ""
    for i in text:
        res_text += key.get(i, '*')
    return res_text
    
def main(path_res: str, path: str, path_key: str) -> None:
    """
        The main function for calling the required task.

    Args:
        path_res (str): the path for the result text
        path (str): the path for the text
        path_key (str): the path for the key
    """
    text = read_file(path)
    text = decryption(path_res, path_key, text)
    write_file(text, path_res)