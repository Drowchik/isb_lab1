from math import erfc, sqrt
from constans import PATH
from auxiliary_function import read_file, read_json_dict, write_file


def frequency_bitwise_test(mas: str) -> float:
    """ frequency_bitwise_test. If the value tends to 1, then it is said that the generator tends to
        be ideal. If the P-value tends to 0, the generator is completely predictable.

    Args:
        mas (str): a randomly generated string consisting of 0 and 1

    Returns:
        float: the result of calculations
    """
    res = 0
    for i in mas:
        if i == "1":
            res += 1
        else:
            res -= 1
    res = abs(res/(sqrt(len(mas))))
    return erfc(res/(sqrt(2)))


def consecutive_bits(mas: str) -> float:
    """ Test for the same consecutive bits. If the value tends to 1, then it is said that the generator tends to
        be ideal. If the P-value tends to 0, the generator is completely predictable.

    Args:
        mas (str): a randomly generated string consisting of 0 and 1

    Returns:
        float: the result of calculations
    """
    fraction = mas.count("1")/len(mas)
    if abs(fraction-0.5) < 2/sqrt(len(mas)):
        v = 0
        for i in range(len(mas)-1):
            if not (mas[i] == mas[i+1]):
                v += 1
        return erfc(abs(v-2*len(mas)*fraction*(1-fraction))/(2*sqrt(2*len(mas))*fraction*(1-fraction)))
    return 0


def longest_sequence(mas: str) -> float:
    """ A test for the longest sequence of units in a block. If the value tends to 1, then it is said that the generator tends to
        be ideal. If the P-value tends to 0, the generator is completely predictable.

    Args:
        mas (str): a randomly generated string consisting of 0 and 1

    Returns:
        float: the result of calculations
    """
    pass


if __name__ == "__main__":
    paths = read_json_dict(PATH)
    gen_c = read_file(paths["rand_c++"])
    print(gen_c, gen_c.count("0"))
    gen_java = read_file(paths["rand_java"])
    print(frequency_bitwise_test(gen_c),
          frequency_bitwise_test(gen_java), sep="\n")
    print(consecutive_bits(gen_c),
          consecutive_bits(gen_java), sep="\n")
