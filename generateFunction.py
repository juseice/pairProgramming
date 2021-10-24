from generateAnswer import generateAnswer
from requirements import *


def fractionsNormalize(s, r):       # formalize fractions
    x = fractions.Fraction(s)
    x = x.limit_denominator(r)
    if x.denominator == 1:
        return str(x.numerator)     # integer
    elif x > 1:
        t = int(x.numerator / x.denominator)
        b = int(x.numerator % x.denominator)
        return str(t) + '\'' + str(b) + '/' + str(x.denominator)    # fractions which > 1
    else:
        return str(x.numerator) + '/' + str(x.denominator)          # fractions which < 1


# use five arguments to generate function
def generateFunction(init, num, inc, div, r):
    ans = -1
    a, b = -1, -1
    if random.random() < 0.5:   # find two position to insert parentheses
        a = random.choice(range(0, num - 1))
        b = random.choice(range(a + 1, num))
    if a == 0 and b == num - 1:
        a, b = -1, -1
    while ans < 0:
        if inc > 0:
            arr = list(range(init, init + num * inc, inc))
            random.shuffle(arr)
        else:
            arr = [init, ] * num
        dec = [""] * num
        for i in range(0, num):
            if i == a:      # insert left parentheses before number
                dec[i] += '('
            if div == 1:
                dec[i] += str(arr[(-i - 1)])
            else:
                dec[i] += fractionsNormalize(arr[i] / (div + random.choice(range(-div + 2, div))), div)
            if i == b:      # insert right parentheses after number
                dec[i] += ')'
        char = [random.choice(calcChar), ]
        for i in range(1, num - 1):
            char += [random.choice(calcChar), ]

        for i in range(0, num - 1):     # avoid negative number
            if char[i] == '-' and arr[-i - 1] < arr[-i - 2]:
                char[i] = '+'
        func = str(dec[0])
        for i in range(1, num):
            func += ' ' + char[i - 1] + ' ' + dec[i]
        func += ' = '
        try:
            ans = generateAnswer(func[:-2])
        except ZeroDivisionError:
            ans = -1
        if '÷' in char and ans == round(ans):   # avoid no fraction generate
            ans = -1
    ans = fractionsNormalize(ans, max(1000 * div, 1000 * r))
    return [func, ans],
