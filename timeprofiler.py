import cProfile
import re

cProfile.run('re.compile("main|generateExercise|generateFunction|generateAnswer|checkExercise")', sort=0)
