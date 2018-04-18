import random


def genEven():
    """
    Returns a random even number x, where 0 <= x < 100
    """
    while True:
        num = random.randint(0, 99)
        if num % 2 == 0:
            return num


def deterministicNumber():
    """
    Deterministically generates and returns an even number between 9 and 21
    """
    return 10


def stochasticNumber():
    """
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    """
    while True:
        num = random.randint(9, 21)
        if num % 2 == 0:
            return num



print(genEven())