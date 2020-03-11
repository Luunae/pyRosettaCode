# Tasks:
# -Create a routine to generate all the proper divisors of a number.
# -Use it to show the proper divisors of the numbers one to ten inclusive.
# -Find a number in the range 1 to 20_000 with the most proper divisors.
# --Show the number and just the count of how many proper divisors it has.


def pd(x):
    divisors = []
    for i in range(1, x):
        if x % i == 0:
            divisors.append(i)
    leng = len(divisors)
    divisors = str(divisors)[1:-1]
    pd = [x, leng, divisors]
    return pd


def pt_one():  # Display all proper divisors for numbers 1 to 10, inclusive.
    for i in range(1, 11):
        results = pd(i)
        print(f"{i} has {results[1]} proper divisors: {results[2]}")


def pt_two():  # Find number in range(1,20_000) with most proper divisors.
    max = [0, 0, 0]
    for i in range(1, 20_001):
        num = pd(i)
        max = check_if_max(num, max)
    print(f"The number with the most pdivs is: {max[0]}")
    print(f"The number of pdivs it has is: {max[1]}")


def check_if_max(current, max):
    if current[1] > max[1]:
        return current
    else:
        return max


def go():
    pt_one()
    pt_two()


go()
