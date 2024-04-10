from collections import Counter


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


def auxiliary_function(text: str):
    """
        This auxiliary function for encryption text
    Args:
        text (str): document for encryption
    """
    info_words = Counter(text)
    print("Информация по частоте встречи символов:", info_words)
    words_in_text = a.split(info_words[0])
    words_in_text = sorted(words_in_text, key=lambda x: len(x))
    print("Список слов разделённых пробелами: ", words_in_text)


if __name__ == "__main__":

    a = read_file("task2\cod1.txt")
    dict_counter = Counter(a)
    c = a.split("2")
    c = sorted(c, key=lambda x: len(x))
    print(dict_counter)
    print("----")
    print(c)
