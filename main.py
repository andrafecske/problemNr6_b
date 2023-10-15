def primnr(no):
    if no == 1 or no == 0:
        return False
    else:
        if no % 2 == 0 and no != 2:
            return False
        else:
            for i in range(3, no // 2 + 1, 2):
                if no % i == 0:
                    return False
    return True


def sumprim(l):
    lnew = []
    lmax = []
    leng = 0
    lengmx = 0
    for i in range(1, len(l)):
        if primnr(l[i - 1] + l[i]):
            lnew.append(l[i - 1])
            leng += 1
            ok = True
        else:
            if ok:
                lnew.append(l[i - 1])
                leng += 1
            if leng > lengmx:
                lengmx = leng
                lmax = lnew[:]
            leng = 0
            lnew.clear()


    print(lmax)

list = [3, 2, 1, 8, 10, 12]
sumprim(list)
