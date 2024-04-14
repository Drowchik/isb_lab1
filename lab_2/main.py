from math import erfc, sqrt
from constans import PATH
from auxiliary_function import read_file, read_json_dict, write_file


def frequency_bitwise_test(mas: str):
    res = 0
    for i in mas:
        if i == "1":
            res += 1
        else:
            res -= 1
    res = abs(res/(sqrt(len(mas))))
    return erfc(res/(sqrt(2)))


if __name__ == "__main__":
    paths = read_json_dict(PATH)
    gen_c = read_file(paths["rand_c++"])
    print(gen_c, gen_c.count("0"))
    gen_java = read_file(paths["rand_java"])
    print(gen_java,  gen_java.count("0"))
    print(frequency_bitwise_test(gen_c),
          frequency_bitwise_test(gen_java), sep="\n")
