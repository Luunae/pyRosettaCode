# Task: Generate and show a table of ZNRs of the decimal numbers zero to twenty, in order.
# Note: This should be extensible to any arbitrary integer.
# Addendum: No two consecutive Fibonacci numbers can be used for a ZNR.


def znr(x):
    fibnum = fib(x)
    tmp = 0
    znr = ""
    for i in range(len(fibnum)):
        if fibnum[-1] + tmp <= x:
            tmp += fibnum.pop(-1)
            znr += "1"
        else:
            del fibnum[-1]
            znr += "0"
    if znr == "":
        print(0)
    else:
        print(int(znr))


def fib(x):
    fibnum = []
    tempa = 1
    tempb = 1
    a = True
    while (tempa or tempb) <= x:
        if tempa not in fibnum:
            fibnum.append(tempa)
        if tempb not in fibnum:
            fibnum.append(tempb)
        if a:
            tempa += tempb
            a = False
        else:
            tempb += tempa
            a = True
    return fibnum


for i in range(20):
    znr(i)
