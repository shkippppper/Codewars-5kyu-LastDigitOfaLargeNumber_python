def last_digit(n1, n2):
    if n2 == 0:
        return 1
    last = str(n1)[-1]
    result = 0 
    if last == "0" or last == "1" or last == "5" or last == "6":
        result = last
    if last == "4" or last == "9":
        if n2%2 == 1: result = last
        else: result = str(int(last)+2)[-1]
    if last == "2" or last == "3" or last == "7" or last == "8":
        if n2%4 == 0:
            result = str(int(last)**4)[-1] 
        elif n2%4 == 1:
            result = str(int(last)**5)[-1]
        elif n2%4 == 2:
            result = str(int(last)**6)[-1]
        elif n2%4 == 3:
            result = str(int(last)**7)[-1]
    return int(result)