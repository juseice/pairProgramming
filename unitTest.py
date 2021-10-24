import unittest
from requirements import *
from generateAnswer import generateAnswer
from checkExercise import checkExercise
from generateExercise import generateExercise
from generateFunction import generateFunction
from generateFunction import fractionsNormalize

class TestAns(unittest.TestCase):
    def test_ans1(self):
        answer = generateAnswer('1 + 1')
        self.assertEqual(answer, 2)

    def test_ans2(self):
        answer = generateAnswer("1\'1/2 + 1\'1/4")
        self.assertTrue(abs(answer - decimal.Decimal(11/4)) < 0.0000001)

    def test_ans3(self):
        answer = generateAnswer("1 ÷ 3/4")
        self.assertEqual(answer, 4/3)

    def test_ans4(self):
        answer = generateAnswer('1\'1/4 × 2\'3/8 + (5\'1/6 - 4\'1/3)')
        self.assertTrue(abs(answer - decimal.Decimal(365/96)) < 0.0000001)

    def test_ansex(self):
        answer = generateAnswer('5/4 × 19/8 + (31/6 - 13/3)')
        self.assertTrue(abs(answer - decimal.Decimal(365/96)) < 0.0000001)

    def test_ans5(self):
        answer = generateAnswer('(7 + 5) ÷ (5 - 1/2)')
        self.assertTrue(abs(answer - decimal.Decimal(8/3)) < 0.0000001)

    def test_ans6(self):
        answer = generateAnswer('19 ÷ (8 × 5) + 2')
        self.assertTrue(abs(answer - decimal.Decimal(99/40)) < 0.0000001)

    def test_ans7(self):
        answer = generateAnswer('60 × 80 - 3\'1/4')
        self.assertEqual(answer,4796.75)


class TestExe(unittest.TestCase):
    def test_fun1(self):
        print(generateExercise(10,2))

    def test_fun2(self):
        print(generateExercise(10,20))


class TestFun(unittest.TestCase):
    def test_norm1(self):
        answer = fractionsNormalize(19187/4,100)
        self.assertEqual(answer,'4796\'3/4')

    def test_norm2(self):
        answer = fractionsNormalize(41/2336,3000)
        self.assertEqual(answer,'41/2336')

    def test_fun1(self):
        print(generateFunction(1,4,3,1,10))

    def test_fun2(self):
        print(generateFunction(10,4,30,10,10))

if __name__ == '__main__':
    unittest.main()
