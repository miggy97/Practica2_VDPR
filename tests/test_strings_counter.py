import unittest
from sample.strings_counter import StringsCounter


class TestStringsCounter(unittest.TestCase):
    #Aqui van los test
    def test_count_strings(self):
        text = ("verano verano verano primavera primavera primavera "
                "invierno invierno invierno")
        solution =  {'verano': 3, 'primavera': 3, 'invierno': 3}
        result = StringsCounter.count_strings(text)
        assert result == solution

if __name__ == '__main__':
    unittest.main()
