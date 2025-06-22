import math

def addition(a: float, b: float):
    result = a + b
    return result


def subtraction(a: float, b: float):
    result = a - b
    return result


def multiplication(a: float, b: float):
    result = a * b
    return result


def division(a: float, b: float):
    result = a / b
    return result


def squareRoot(a: float):
    return math.sqrt(a)


def power(a: float, b: float):
    return math.pow(a, b)


def fact(a: int):
    return math.factorial(a)


def sine(a: float):
    return math.sin(a)


def cosine(a: float):
    return math.cos(a)


def tangent(a: float):
    return math.tan(a)


def logarithm(a: float, b = math.e):
    return math.log(a, b)


def roots(exp: float, base: float):
    return base ** (1 / exp)
