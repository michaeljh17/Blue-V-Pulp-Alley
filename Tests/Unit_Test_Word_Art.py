import unittest
import os
import sys
from ViewModel.Word_Art import *
from test.test_datetime import tearDownClass
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if path not in sys.path:
    sys.path.insert(1, path)
del path


class MainTests(unittest.TestCase):

    def setUp(self):
        self.wa = Word_Art()

    def test_01(self):
        print("Test 1 - combine_arrays()")
        array1 = ["Array1String1", "Array1String2"]
        array2 = ["Array2String1", "Array2String2"]
        result = self.wa.combine_arrays(array1, array2)
        expected_result = ["Array1String1Array2String1", "Array1" +
                           "String2Array2String2"]
        self.assertTrue(result == expected_result, "combine_arrays() is " +
                        "unable to combine the arrays appropriately")

    def test_02(self):
        print("Test 2 - convert_letter - c")
        result = self.wa.convert_letter("c")
        expected = ["      ",
                    "  ___ ",
                    " / __|",
                    "| (__ ",
                    " \___|",
                    "      "]
        for row in result:
            print(row)
        self.assertTrue(result == expected)

    def test_03(self):
        print("Test 3 - combining comvine_arrays and convert_letter")
        array1 = self.wa.convert_letter("A")
        array2 = self.wa.convert_letter("e")
        array3 = self.wa.convert_letter("c")
        result = self.wa.combine_arrays(array1, array2, array3)
        expected = ["                   ",
                    "  __ _   ___   ___ ",
                    " / _` | / _ \\ / __|",
                    "| (_| ||  __/| (__ ",
                    " \__,_| \___| \___|",
                    "                   "]
        self.assertTrue(result == expected)

        for row in result:
            print(row)

    def test_04(self):
        print("Test 4 - create(\"ace\")")
        result = self.wa.heading("ace")
        # expected = "                   \n  __ _   ___   ___ \n / _` | / __| / _ \\n| (_| || (__ |  __/\n \__,_| \___| \___|\n                   "
        print(result)
        # self.assertTrue(result == expected)

    def test_05(self):
        print("Test 5 - create(\"abcdefghij\")")
        result = self.wa.heading("abcdefghij")
        print(result)

    def test_06(self):
        print("Test 6 - create(\"ice ace\")")
        result = self.wa.heading("ice ace")
        print(result)

    def test_07(self):
        print("Test 7 - create(\"jklmnopqrstuvwxyz\")")
        result = self.wa.heading("jklmnopqrstuvwxyz")
        print(result)

    def test_08(self):
        print("Test 8 - create(\"one1 two2\") with numbers")
        result = self.wa.heading("one1 two2")
        print(result)
if __name__ == "__main__":
    unittest.main()
