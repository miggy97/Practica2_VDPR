import unittest
import collections
from sample.strings_counter import StringsCounter


class TestStringsCounter(unittest.TestCase):

    def test_count_strings(self):
        text = ("verano verano verano")
        solution=[('verano', 3)]

        result=StringsCounter.count_strings(text)

        assert collections.Counter(result) == collections.Counter(solution)


    def test_meter_numeros_String(self):
        text=("1 2 3 1 2 3 1 2 3 4 alvaro 6")

        solution=[('1', 3), ('2', 3), ('3', 3), ('4', 1), ('alvaro', 1), ('6', 1)]

        result= StringsCounter.count_strings(text)

        assert collections.Counter(result) == collections.Counter(solution)


    def test_count_varios_Strings(self):
        text = ("verano verano verano primavera primavera primavera "
                "invierno invierno invierno")
        solution = [('verano', 3), ('primavera', 3), ('invierno', 3)]

        result = StringsCounter.count_strings(text)

        assert collections.Counter(result) == collections.Counter(solution)

    #12 tratamiento de siglas
    def test_una_sigla(self):
        text = ("C.I.A")

        solution = [('cia', 1)]

        result = StringsCounter.count_strings(text)

        assert collections.Count(result) == collections.Counter(solution)

if __name__ == '__main__':
    unittest.main()
