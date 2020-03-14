# Amicable pairs are two numbers not equal to each other whos sum of proper divisors are
#   the same as the other.
from proper_divisors import pd
import timeit


def sums(num):
    sums = 0
    for divisor in num:
        sums += divisor
    return sums


def amicable_pairs():
    amicables = []
    for x in range(1, 20_000):
        for y in range(x+1, 20_000):
            pd_of_x = pd(x)[2]
            pd_of_y = pd(y)[2]
            if pd_of_x == [] or pd_of_y == []:
                continue
            pd_sum_of_x = sum(pd_of_x)
            pd_sum_of_y = sum(pd_of_y)
            if pd_sum_of_x == y and pd_sum_of_y == x:
                pair = [x, y]
                amicables.append(pair)
    print(f"Amicable pairs:")
    for pair in amicables:
        print(pair)


if __name__ == "__main__":
    print(timeit.timeit(amicable_pairs, number=1))

