from enum import Enum
import json

ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


class Mode(Enum):
    ENCRYPT = 1
    DECRYPT = 2


def main(file_name: str, mode: Mode, res_nume: str, path_js: str, shift: int = 3) -> None:
    """ 
        The main function that calls everything you need according to the entered parameters

    Args:
        file_name (str): path document 
        mode (Mode): decryption or encryption
        res_nume (str): the resulting file name
    """
    res = read_file(file_name)
    text = encryption(res, mode, shift)
    write_file(text, res_nume)
    create_json(path_js, shift)


def read_file(name: str) -> str:
    """ 
        This function reads text from the file for further processing

    Args:
        name (str): the path and name of the file to be read

    Returns:
        str: the read document
    """
    try:
        with open(name, 'r', encoding='utf-8') as f:
            data = f.read()
            return data
    except FileNotFoundError:
        print("Невозможно открыть файл")


def write_file(document: str, name_file: str) -> None:
    """
        Writes encrypted text to a document 
    Args:
        document (str): the actual processed text
        name_file (_type_): the path of the file where it will be written
    """
    try:
        with open(name_file, "w", encoding='utf-8') as f:
            f.write(document)
            return
    except IOError:
        print("Что-то пошло не так")


def encryption(document: str, mode: Enum, shift: int) -> str:
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


def create_json(path_json: str, shift: int):
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
