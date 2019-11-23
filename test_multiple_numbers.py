import unittest # added library
import multiple_numbers # referring another python core file


class testMultiplesNumbers(unittest.TestCase):
    """
    Class to create functions to validate our numbers
    """

    def test_multiples_numbers(self):
        """
        Function implementing a value to each case of number, multiple of 3, multiple of 5 or both
        """
        multipleOfThree = multiple_numbers.multipleNumbers(18)
        multipleOfFive = multiple_numbers.multipleNumbers(35)
        multipleOfThreeAndFive = multiple_numbers.multipleNumbers(90)

        self.assertEqual(multipleOfThree, 'Three')
        self.assertEqual(multipleOfFive, 'Five')
        self.assertEqual(multipleOfThreeAndFive, 'ThreeFive')


if __name__ == '__main__':
    unittest.main()
