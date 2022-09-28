def division(a, b):
    return a / b

def calcular_saldo_final(saldo_inicial, operaciones):
    if saldo_inicial < 0:
        return None
    saldo = saldo_inicial
    for operacion in operaciones:
        saldo += operacion
        if saldo < 0:
            return -1

    return saldo


def es_mayor_a(a, b):
    """
    if a > b:    if fun1(a, b, c) > fun2(d, e)
        return True
    else:
        return False
    """


    """
    if a > b:
        return True
    return False
    """
    return a > b    # return fun1(a, b, c) > fun2(d, e)



