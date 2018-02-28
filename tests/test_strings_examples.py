import unittest
from sample.strings_example import StringsExamples


class TestStringsExamples(unittest.TestCase):
    def test_concat_strings(self):
        string1 = "hola"
        string2 = "adios"
        result = StringsExamples.concat_strings(string1, string2)
        assert result == "holaadios"


if __name__ == '__main__':
    unittest.main()
