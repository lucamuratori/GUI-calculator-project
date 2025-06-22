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
    result = math.prod(args)
    return result


print(subtraction(1, 2, 3, 4, 5))
print(multiplication(1, 2, 3, 4, 5))