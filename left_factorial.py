import timeit
from functools import lru_cache


@lru_cache(maxsize=None)
def factorial(num):
    if num == 0:
        return 1
    fac = num
    while num >= 3:
        fac *= num - 1
        num -= 1
    return fac


def lfactorial(num):
    lfac = 0
    for i in range(0, num):
        lfac += factorial(i)
    return lfac


def digits(num):
    num = str(lfactorial(num))
    num = len(num)
    return num


def first():
    print("!n for n = 0(1)10")
    for i in range(0, 11):
        print(f"!{i} = {lfactorial(i)}")


def second():
    print("!n for n = 20(10)110")
    for i in range(20, 111, 10):
        print(f"!{i} = {lfactorial(i)}")


def third():
    print("digit counts of !n for n = 1000(1000)10 000")
    for i in range(1_000, 10_001, 1_000):
        print(f"!{i} digits = {digits(i)}")


print(timeit.timeit(first, number=1))
print(timeit.timeit(second, number=1))
print(timeit.timeit(third, number=1))
