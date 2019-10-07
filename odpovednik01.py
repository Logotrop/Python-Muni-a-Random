def series(n):
    if n<3:
        return 0
    serie = []
    for I in range(3, n + 1):
        isok = True
        for J in str(I):
            if int(J) >= 6:
                isok = False
        if isok:
            serie.append(I)
        result = sum(serie)
    return result


def cifs(n):
    num = 0
    for I in range(len(str(n)), 0, -1):
        num += (I * int(str(n)[len(str(n)) - I]))
    return num

print(series(3))