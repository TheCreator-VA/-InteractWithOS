from makingString import group_list
import unittest

class TestMakingString(unittest.TestCase):
    def test_basic(self):
        testcase = "Marketing", ["Mike", "Karen", "Jake", "Tasha"]
        expected = "Marketing: Mike, Karen, Jake, Tasha"
        self.assertEqual(group_list(testcase), expected)

unittest.main()