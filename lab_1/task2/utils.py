import os
import sys
import json

from collections import Counter
from typing import Dict


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


def decryption(path_res: str, key: str, text: str) -> str:
    """
        decrypts the text by the key
    Args:
        path_res (str): _description_
        key (str): the key for decryption
        text (str): text ecryption

    Returns:
        str: result_text
    """
    try:
        res_text = ""
        for i in text:
            res_text += key.get(i, '*')
        return res_text
    except FileNotFoundError:
        print("Что-то пошло не так")
        
