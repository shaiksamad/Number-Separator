function separator(num, sep=",") {
    num = num.toString().replace(",", "")
    if (num.length <= 3) return num
    final = sep+num.slice(-3)
    num = num.slice(0, -3)
    while (num.length > 2) {
        final = sep+num.slice(-2) + final
        num = num.slice(0, -2)
    }
    final = num + final
    return final
}