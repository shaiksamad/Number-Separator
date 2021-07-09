IND_SYS = 1  # Indian System
INT_SYS = 0  # International System

def separator(num: int, sys=INT_SYS, sep=","):
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
