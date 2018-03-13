import unittest
import collections
from sample.strings_counter import StringsCounter


class TestStringsCounter(unittest.TestCase):

    def test_count_strings(self):
        text = ("verano verano verano primavera primavera primavera "
                "invierno invierno invierno")
        solution = [('verano', 3), ('primavera',3), ('invierno', 3)]

        result, words, set_words = StringsCounter.count_strings(text)

        assert collections.Counter(result) == collections.Counter(solution)

        

if __name__ == '__main__':
    unittest.main()
