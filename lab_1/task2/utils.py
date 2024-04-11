import os
import sys
import json

from collections import Counter
from typing import Dict

project_directory = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_directory)

from general_function import read_file, read_json_dict, write_file
from constants import path_js


def auxiliary_function(text: str) -> None:
    """
        This auxiliary function for encryption text
    Args:
        text (str): document for encryption
    """
    info_words = Counter(text)
    count_char = len(text)
    dict_words = dict()
    for char, count in info_words.items():
        dict_words[char] = count / count_char
    dict_words = {key: count for key, count in sorted(
        dict_words.items(), key=lambda item: item[1], reverse=True)}
    print(f"-Информация по частоте встречи символов: {dict_words}")
    words_in_text = text.split(info_words.most_common(1)[0][0])
    print(f"-Список слов разделённых пробелами: {words_in_text}")
    words_in_text = sorted(words_in_text, key=lambda x: len(x))
    print(
        f"-Список отсортированных по длине слов разделённых пробелами: {words_in_text}")


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
    try:
        key = read_json_dict(path)
        res_text = ""
        for i in text:
            res_text += key.get(i, '*')
        return res_text
    except FileNotFoundError:
        print("Что-то пошло не так")


if __name__ == "__main__":
    path = read_json_dict(path_js)
    text = read_file(path["cod2"])
    auxiliary_function(text)
    # text = decryption(path["res_text2"], path["key_for_code"], text)
    # write_file(text, path["res_text2"])
