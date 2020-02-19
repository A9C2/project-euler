import math
def trial_division(n):
    if type(n) != int:
        raise TypeError
    if n < 2:
        return False
    a = 2
    while a <= math.sqrt(n):
        if n % a == 0:
            return False
        a += 1
    return True