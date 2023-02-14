error = 0


def clear_error():
    global error
    error = 0


def rat_add(a, b):
    global error
    try:
        k = a + b
    except:
        error = 1
    return k if error == 0 else (None, None)


def rat_mull(a, b):
    global error
    try:
        k = a * b
    except:
        error = 1
    return k if error == 0 else (None, None)


def rat_sub(a, b):
    global error
    try:
        k = a - b
    except:
        error = 1
    return k if error == 0 else (None, None)


def rat_div(a, b):
    global error
    try:
        k = a / b
    except:
        error = 1
    return k if error == 0 else (None, None)


def rat_create(m: int, n: int):
    global error
    try:
        if n > 0:
            k = m / n
        else:
            error = 1
    except:
        error = 1
    return k if error == 0 else (None, None)


def rat_inp():
    global error
    try:
        k = float(input())
    except:
        error = 1
    return k if error == 0 else (None, None)


def rat_prt(a):
    print(a)


def rat_eq(a, b):
    global error
    try:
        k = a == b
    except:
        error = 1
    return k if error == 0 else (None, None)


def rat_lt(a, b):
    global error
    try:
        k = a < b
    except:
        error = 1
    return k if error == 0 else (None, None)


def rat_reduce(m: int, n: int):
    global error
    try:
        if n > 0:
            dilnyk = 1
            count = 1
            while count < min(m, n) // 2:
                if m % count == 0 and n % count == 0 and count > dilnyk:
                    dilnyk = count
                count += 1
            k = (m // dilnyk) / (n // dilnyk)
        else:
            error = 1
    except:
        error = 1
    return k if error == 0 else (None, None)
