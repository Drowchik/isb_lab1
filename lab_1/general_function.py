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