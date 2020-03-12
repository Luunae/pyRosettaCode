# Amicable pairs are two numbers not equal to each other whos sum of proper divisors are
#   the same as the other.
from proper_divisors import pd

if __name__ == "__main__":
    amicables = []
    num = 0
    for i in range(1,20_000):
        for j in range(1,20_000):
            x = pd(i)
            y = pd(j)
            if x[2] == y[2]:
                nums = [x, y]
                amicables.append(nums)
    for pair in amicables:
        print(f"pair: {amicables[pair]}")