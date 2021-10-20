from requirements import *


def repl(matched):
    res = '(' + matched.group() + ')'
    res = res.replace('\'', '+')
    return str(res)


def generateAnswer(func):
    func = str(re.sub("[1-9][0-9]*\'[1-9][0-9]*/[1-9][0-9]*", repl, func))
    func = str(re.sub("[1-9][0-9]*/[1-9][0-9]*", repl, func))
    # print(func)
    func = func.replace('÷', '/')
    func = func.replace('×', '*')
    ans = decimal.Decimal(eval(func))
    return ans
