from generateFunction import generateFunction
from requirements import *


def generateExercise(n, r):
    random.seed()       # initial random
    ans = []
    again = False
    while len(ans) < n:
        been = (0, 1,)
        div = 1
        for i in range(1, r + 1):
            if again and r < 3:
                break
            for j in range(0, r - i + 1):
                if i == 1 and j == 0 and random.random() < 0.8 and r > 2:
                    continue
                for k in (2, 3, 4):
                    if again and k == 2:
                        continue
                    if i + (j * (k - 1)) <= r:
                        if random.random() < 0.6:   # call generateFunction to generate integer function
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
                if tr > 10:     # check if r is too small or it will death loop
                    if again:
                        print('r is too small. Enlarge r 10 times.')
                        r = r * 10
                    break
                div = int(random.random() * r)
                tr = tr + 1
            if tr > 10:
                again = True
                break
            been += (div,)
            tr = 0
            t = 0
            # print(div)
            while t <= rem / 4:     # call generateFunction to generate fraction function
                a, b, c = random.choice(range(1, r * div)), random.choice(range(0, div - 1)), random.choice(range(2, 4))
                if a + (b * (c - 1)) <= div * r:
                    ans += generateFunction(a, c, b, div, r)
                t = t + 1
    random.shuffle(ans)
    excfile = open("Exercise.txt", mode='w')
    ansfile = open("Answer.txt", mode='w')
    # for i, j in ans:
    #     print(i + j)
    for i in range(0, n):
        excfile.write(str(1 + i) + '. ' + ans[i][0] + '\n')
        ansfile.write(str(1 + i) + '. ' + ans[i][1] + '\n')
    excfile.close()
    ansfile.close()
    return
