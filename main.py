import math

def addition(*args):
    x = sum(args)
    return x


def subtraction(*args):
    args = list(args)
    result = args.pop(0)
    while args != []:
        result -= args.pop(0)
    return result


def multiplication(*args):
    
    return
print(subtraction(1, 2, 3, 4, 5))