from enum import Enum

ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


class Mode(Enum):
    ENCRYPT = 1
    DECRYPT = 2


def main(file_name: str, mode: Mode, res_nume: str) -> None:
    """ 
        The main function that calls everything you need according to the entered parameters

    Args:
        file_name (str): path document 
        mode (Mode): decryption or encryption
        res_nume (str): the resulting file name
    """
    res = read_file(file_name)
    text = encryption(res, mode)
    write_file(text, res_nume)


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


def encryption(document: str, mode: Enum, shift=3) -> str:
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
