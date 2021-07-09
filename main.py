IND_SYS = 1  # Indian System
INT_SYS = 0  # International System


def separator(num: int, sys=INT_SYS, sep=","):
    """

    :param num: number to be comma-separated (eg: 123456789)

    :param sys:
    Default is "INT_SYS"
        INT_SYS (123456789 --> 123,456,789)
        IND_SYS (123456789 --> 12,34,56,789)

    :param sep: Default is ","

    :return: separated number (123,456,789)
    """
    final = sep + f"000{num % 1000}"[-3:]
    num //= 1000
    if sys:
        while num:
            final = sep + f"00{num % 100}"[-2:] + final
            num //= 100
    else:
        while num:
            final = sep + f"000{num % 1000}"[-3:] + final
            num //= 1000

    final = final[1:]
    while final[0] == "0": final = final[1:]
    return final


if __name__ == "__main__":
    print(separator(int(input()), IND_SYS))
