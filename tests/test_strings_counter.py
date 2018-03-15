import unittest
import collections
from sample.strings_counter import StringsCounter


class TestStringsCounter(unittest.TestCase):

    def test_count_strings(self):
        text = ("verano verano verano")
        solution = [('verano', 3)]

        result = StringsCounter.count_strings(text)

        assert collections.Counter(result) == collections.Counter(solution)


    def test_meter_numeros_String(self):
        text = ("1 2 3 1 2 3 1 2 3 4 alvaro 6")

        solution = [('1', 3), ('2', 3), ('3', 3), ('4', 1), ('alvaro', 1), ('6', 1)]

        result = StringsCounter.count_strings(text)

        assert collections.Counter(result) == collections.Counter(solution)

    def test_count_varios_Strings(self):
        text = ("verano verano verano primavera primavera primavera "
                "invierno invierno invierno")
        solution = [('verano', 3), ('primavera', 3), ('invierno', 3)]

        result = StringsCounter.count_strings(text)

        assert collections.Counter(result) == collections.Counter(solution)

    #8
    def test_check_one_string_is_the_same(self):
        text = ("hola")
        solution = ['hola']
        result = StringsCounter.count_strings(text)
        assert result[0][0]==solution[0]
        
    def test_check_several_strings_are_the_same(self):
        text = ("hola caracola, esto es un texto de prueba!!")
        solution=['hola','caracola','esto', 'es', 'un', 'texto', 'de', 'prueba']
        result = StringsCounter.count_strings(text)
        same = True
        for i in range(0,7):
            if result[i][0] not in solution == True:
                same = False
                break
        assert same == True
        
if __name__ == '__main__':
    unittest.main()
