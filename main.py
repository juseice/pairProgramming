from requirements import *
from checkExercise import checkExercise
from generateExercise import generateExercise


def main(argv):
    global efile, afile
    try:                    # reading arguments
        opts, args = getopt.getopt(argv, "hn:r:e:a:", ["num=", "rad=", "eFile=", "aFile="])
    except getopt.GetoptError:
        print('Arguments ERROR')
        sys.exit(2)
    n, r = 50, -1
    flage, flaga = 0, 0
    for opt, arg in opts:   # process arguments
        if opt == '-h':
            print('Myapp.exe -r <radius> [-n <number=10>] to generate n Exercise which between 0 and r. Or')
            print('Myapp.exe -e <exerciseFile> -a <answerFile> to check if answer right')
        if opt in ('-n', '--num'):
            try:
                n = int(arg)
                if n > 1e5:
                    print('n cannot larger than 1e6. Set r to 1e6')
                    n = int(1e5)
            except ValueError:
                print('n must be a number')
                sys.exit(2)
        if opt in ('-r', '--rad'):
            try:
                r = int(arg)
                if r > 1e6:
                    print('r cannot larger than 1e6. Set r to 1e6')
                    r = int(1e6)
            except ValueError:
                print('r must be a number')
                sys.exit(2)
        if opt in ('-e', '--eFile'):
            try:
                efile = open(arg, mode='r')
                flage = 1
            except [OSError, FileNotFoundError]:
                print('Exercise file not found. Please double check the path and your spelling.')
                sys.exit(2)
        if opt in ('-a', '--aFile'):
            try:
                afile = open(arg, mode='r')
                flaga = 1
            except [OSError, FileNotFoundError]:
                print('Answer file not found. Please double check the path and your spelling.')
                sys.exit(2)

    if flaga == 1 or flage == 1:
        if flaga == 1 and flage == 1:
            checkExercise(efile, afile)
            print('Checking exercise...')
        elif flaga == 1:
            print('Only open Answer file.')
            sys.exit(2)
        elif flage == 1:
            print('Only open Exercise file.')
            sys.exit(2)
    elif r > 0:
        generateExercise(n, r)
        print('Generating', n, 'exercise...')
    else:
        print('Require -r <radius> argument. Input Myapp.exe -h for further help.')
        sys.exit(2)
    if flage:       # close file
        efile.close()
    if flaga:
        afile.close()


if __name__ == '__main__':
    begin = time.time()
    main(sys.argv[1:])
    end = time.time()
    print('Time elapsed:', str(end - begin) + 's')
