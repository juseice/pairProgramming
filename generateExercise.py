from generateFunction import generateFunction
from requirements import *


def generateExercise(n, r):
    random.seed()
    ans = ()
    been = (0, 1,)
    div = 1
    for i in range(1, r + 1):
        for j in range(0, r - i + 1):
            if i == 1 and j == 0 and random.random() < 0.8:
                continue
            for k in (2, 3, 4):
                if i + (j * (k - 1)) <= r:
                    if random.random() < 0.6:
                        ans += generateFunction(i, k, j, div, r)
                        if len(ans) >= 0.9 * n:
                            break
                if len(ans) >= 0.9 * n:
                    break
            if len(ans) >= 0.9 * n:
                break
        if len(ans) >= 0.9 * n:
            break
    rem = n - len(ans)
    tr = 0
    while len(ans) < n:
        while div in been:
            if tr > 10:
                print('r is too small. Enlarge r 10 times.')
                r = r * 10
            div = int(random.random() * r)
            tr = tr + 1
        been += (div,)
        tr = 0
        t = 0
        # print(div)
        while t <= rem / 4:
            a, b, c = random.choice(range(1, r * div)), random.choice(range(0, div - 1)), random.choice(range(2, 4))
            if a + (b * (c - 1)) <= div * r:
                ans += generateFunction(a, c, b, div, r)
            t = t + 1
    for i, j in ans:
        print(i + j)
    return
