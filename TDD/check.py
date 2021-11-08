def check(a, b, c):
    l = [a, b, c]
    if (checkint(a) and checkint(b) and checkint(c)):  # iii
        return max(l)
    elif (checkfloat(a) and checkfloat(b) and checkfloat(c)):  # fff
        return max(l)
    elif ((checkfloat(a) and checkfloat(b) and checkint(c))):  # ffi
        return max(l)
    elif ((checkfloat(a) and checkint(b) and checkint(c))):  # fii
        return max(l)
    elif ((checkint(a) and checkfloat(b) and checkfloat(c))):  # iff
        return max(l)
    elif ((checkint(a) and checkint(b) and checkfloat(c))):  # iif
        return max(l)
    elif ((checkint(a) and checkfloat(b) and checkint(c))):  # ifi
        return max(l)
    elif ((checkfloat(a) and checkint(b) and checkfloat(c))):  # fif
        return max(l)
    else:
        return "Error"


def checkint(x):
    if type(x) == int:
        return True
    else:
        False

def checkfloat(x):
    if type(x) == float:
        return True
    else:
        False