# coding=utf-8
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
        solution = [('alvaro',1)]
        result = StringsCounter.count_strings(text)
        assert collections.Counter(result) == collections.Counter(solution)

    def test_count_varios_Strings(self):
        text = ("verano verano verano primavera primavera primavera "
                "invierno invierno invierno")
        solution = [('verano', 3), ('primavera', 3), ('invierno', 3)]
        result = StringsCounter.count_strings(text)
        assert collections.Counter(result) == collections.Counter(solution)

    #8 verificar que mete bien las palabras
    def test_check_one_string_is_the_same(self):
        text = ("hola")
        solution = ['hola']
        result = StringsCounter.count_strings(text)
        assert result[0][0]==solution[0]
        
    def test_check_several_strings_are_the_same(self):
        text = ("hola caracola, esto es un texto de prueba!!")
        solution=['hola','caracola','esto', 'texto', 'de', 'prueba']
        result = StringsCounter.count_strings(text)
        same = True
        for i in range(0,len(solution)):
            if result[i][0] not in solution == True:
                same = False
                break
        assert same
        
    def test_strings_are_more_than_1_char(self):   
        text = ("a b cd efg h i jk")
        solution = [('cd',1),('efg',1),('jk',1)]
        result = StringsCounter.count_strings(text)
        assert collections.Counter(result) == collections.Counter(solution)
        
    #10 tratamiento de numeros
    def test_numbers_without_string(self):
        text = ("1 2 3")
        solution = []
        result = StringsCounter.count_strings(text)
        assert collections.Counter(result) == collections.Counter(solution)
    
    def test_numbers_in_string(self):
        text = ("1 4m 4 133t h4ck3r")
        solution = [('4m',1),('133t',1),('h4ck3r',1)]
        result = StringsCounter.count_strings(text)
        assert collections.Counter(result) == collections.Counter(solution)
        
    #11 simbolos de puntuacion
    def test_punctuation_symbol_alone(self):
        text = (". . .")
        solution = []
        result = StringsCounter.count_strings(text)
        assert collections.Counter(result) == collections.Counter(solution)
    
    def test_punctuation_symbol_with_string(self):
        text = ("Hola...")
        solution = [('hola',1)]
        result = StringsCounter.count_strings(text)
        assert collections.Counter(result) == collections.Counter(solution)
    
    def test_punctuation_symbol_with_strings_of_diferent_lenght(self):
        text = ("a... bc! def??")
        solution = [('bc',1),('def',1)]
        result = StringsCounter.count_strings(text)
        assert collections.Counter(result) == collections.Counter(solution)
    
    #Metodos internos de la clase strings_counter    
    def test_method_clear_stopword(self):
        word = "aquel"
        solution = ""
        result = StringsCounter.clear_stopwords(word)
        assert collections.Counter(result) == collections.Counter(solution)
        
    def test_method_clear_punctiation_symbols_alone(self):
        word = "!"
        solution = ""
        result = StringsCounter.clear_punctiation_symbols(word)
        assert collections.Counter(result) == collections.Counter(solution)
        
    def test_method_clear_punctiation_symbols_at_end_of_string(self):
        word = "Hola?"
        solution = "Hola"
        result = StringsCounter.clear_punctiation_symbols(word)
        assert collections.Counter(result) == collections.Counter(solution)
        
    def test_method_clear_punctiation_symbols_inside_string(self):
        word = "H<o.l;a)"
        solution = "Hola"
        result = StringsCounter.clear_punctiation_symbols(word)
        assert collections.Counter(result) == collections.Counter(solution)
        
    def test_count_words(self): 
        word = "Hola"
        text = ['Hola','Hola','Hola']
        solution = 3
        result = StringsCounter.count_words(word,text)
        assert result == solution 
        
    def test_count_words_uneven_text(self): 
        word = "Hola"
        text = ['Hola','este','texto','es','de','prueba','Hola']
        solution = 2
        result = StringsCounter.count_words(word,text)
        assert result == solution 
    
    #3 text null   
    def test_null_text(self):
        text = None
        self.assertRaises(TypeError, StringsCounter.count_strings,text)
        
    def test_empty_text(self):        
        text = ("")
        solution = []
        result = StringsCounter.count_strings(text)
        assert collections.Counter(result) == collections.Counter(solution)
        
    #7 Palabras iguales con diferentes mayusculas
    def test_different_capital_letters_same_word(self):
        text = ("HoLA hola HOLA")
        solution = [('hola',3)]
        assert solution[0][0] == StringsCounter.count_strings(text)[0][0]

    def test_different_capital_letters_same_number(self):
        text = ("HoLA hola HOLA")
        solution = [('holi',3)]
        assert solution[0][1] == StringsCounter.count_strings(text)[0][1]
    
    #9 Orden de la lista
    def test_correct_order(self):
        text = ("hola hola hola adios adios buenas")
        solution = [('hola', 3), ('adios', 2), ('buenas', 1)]
        assert solution == StringsCounter.count_strings(text)
        
    #12 tratamiento de siglas
    def test_sigla_unica(self):
        text = ("C.I.A")
        solution = [('cia', 1)]
        result = StringsCounter.count_strings(text)
        assert collections.Counter(result) == collections.Counter(solution)

    def test_varias_siglas(self):
        text = ("C.I.A  N.A.S.A")
        solution = [('cia', 1), ('nasa', 1)]
        result = StringsCounter.count_strings(text)
        assert collections.Counter(result) == collections.Counter(solution)

    def test_varias_siglas_con_strings(self):
        text = ("la C.I.A esta trabajando con la N.A.S.A")
        solution = [('nasa', 1), ('trabajando', 1), ('cia', 1)]
        result = StringsCounter.count_strings(text)
        assert collections.Counter(result) == collections.Counter(solution)

    #4 Unicode
    def test_unicode(self):
        text = ("❤ ❤ ❤")
        solution = []
        result = StringsCounter.count_strings(text)
        assert collections.Counter(result) == collections.Counter(solution)

    def test_unicode_diferentes(self):
        text = ("❤ ☢ ❤ ☢")
        solution = []
        result = StringsCounter.count_strings(text)
        assert collections.Counter(result) == collections.Counter(solution)

    def test_unicode_string(self):
        text = ("las armas ☢ son peligrosas")
        solution = [('armas', 1), ('son', 1), ('peligrosas', 1)]
        result = StringsCounter.count_strings(text)
        assert collections.Counter(result) == collections.Counter(solution)

if __name__ == '__main__':
    unittest.main()
