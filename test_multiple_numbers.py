import unittest
import multiple_numbers


class testMultiplesNumbers(unittest.TestCase):

    def test_multiples_numbers(self):
        multipleOfThree = multiple_numbers.multipleNumbers(18)
        multipleOfFive = multiple_numbers.multipleNumbers(35)
        multipleOfThreeAndFive = multiple_numbers.multipleNumbers(90)

        self.assertEqual(multipleOfThree, 'Three')
        self.assertEqual(multipleOfFive, 'Five')
        self.assertEqual(multipleOfThreeAndFive, 'ThreeFive')


if __name__ == '__main__':
    unittest.main()