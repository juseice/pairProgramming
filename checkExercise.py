from requirements import *
from generateAnswer import generateAnswer


def checkExercise(efile, afile):
    # exc = efile.readlines()
    # ans = afile.readlines()
    correct = ()
    wrong = ()
    exc = efile.readline()
    ans = afile.readline()
    pid = 1
    while exc != "" and ans != "":
        # print(exc[len(str(pid)) + 1:-3], ans[len(str(pid)) + 1:])
        a = generateAnswer(exc[len(str(pid)) + 1:-3])
        b = generateAnswer(ans[len(str(pid)) + 1:])
        if abs(a - b) < 0.000001:
            correct += (pid,)
        else:
            wrong += (pid,)
            # print(a, b)
        exc = efile.readline()
        ans = afile.readline()
        pid = pid + 1
    ofile = open("Grade.txt", 'w')
    ofile.write("Correct: " + str(len(correct)) + str(correct) + "\n")
    ofile.write("Wrong: " + str(len(wrong)) + str(wrong) + "\n")
    return
