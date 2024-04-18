from math import erfc, sqrt

from scipy.special import gammainc

from constans import PATH, PI, M
from auxiliary_function import read_file, read_json_dict, write_file, write_json_dict


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
    count_blocks = len(mas)//M
    blocks = []
    for i in range(count_blocks):
        blocks.append(mas[i*8:(i+1)*8])
    count_max_one = []
    v = []
    for block in blocks:
        max_one = 0
        one_now = 0
        for i in block:
            if i == "1":
                one_now += 1
            else:
                max_one = max(one_now, max_one)
                one_now = 0
        count_max_one.append(max(one_now, max_one))
    v = []
    v.append(count_max_one.count(0) + count_max_one.count(1))
    v.append(count_max_one.count(2))
    v.append(count_max_one.count(3))
    v.append(len(count_max_one) - v[0] - v[1] - v[2])
    x = sum([(v[i]-16*PI[i])**2/(16*PI[i]) for i in range(len(v))])
    return gammainc(3/2, x/2)


if __name__ == "__main__":
    paths = read_json_dict(PATH)
    gen_c = read_file(paths["rand_c++"])
    gen_java = read_file(paths["rand_java"])
    dict_result = {}
    dict_result["frequency_bitwise_test C++"] = frequency_bitwise_test(gen_c)
    dict_result["frequency_bitwise_test java"] = frequency_bitwise_test(
        gen_java)
    dict_result["consecutive_bits C++"] = consecutive_bits(gen_c)
    dict_result["consecutive_bits java"] = consecutive_bits(gen_java)
    dict_result["longest_sequence C++"] = longest_sequence(gen_c)
    dict_result["longest_sequence java"] = longest_sequence(gen_java)
    write_json_dict(paths["result_file"], dict_result)
