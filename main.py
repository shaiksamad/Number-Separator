def separator(num: float, sep=",")-> str:
    # removing zeros before unit's place and converting to string
    num = str(float(num))  
    # if not num.isfloat():
        # raise ValueError("Enter a valid number.")
    if len(num) <= 3:
        return num
    final = sep + num[-3:]
    num = num[:-3]
    while len(num) > 2:
        final = sep + num[-2:] + final
        num = num[:-2]
    
    final = num + final
    return final
    # if sys:
    #     while num:
    #         final = sep + f"00{num % 100}"[-2:] + final
    #         num //= 100
    # else:
    #     while num:
    #         final = sep + f"000{num % 1000}"[-3:] + final
    #         num //= 1000

    # final = final[1:]
    # while final[0] == "0": final = final[1:]
    # return final


if __name__ == "__main__":
    while 1:
        inp = input("number : ")
        # if not inp.isnumeric():
            # continue
        print(separator(inp))