import operator


class StringsCounter(object):
    """A class to play with the strings"""

    @staticmethod
    def count_strings(text):
        word_counter = {}

        # Si es un string lo dividimos en un array de strings
        if type(text) is str:
            text = text.split()

        # Quitar simbolos de puntuacion
        for i in range(len(text)):
            if not text[i].isdigit() and len(text[i])>1:
                text[i] = StringsCounter.clear_stopwords(text[i])
            else:
                text[i]=""

        # Poner todo el texto en minusculas
        text = list(map(str.lower, text))      
        set_text = set(text)
        
        #eliminamos elementos vacios
        if "" in set_text:
            set_text.remove("")
        # Contamos el numero de palabras repetidas y lo almacenamso en un diccionario
        
        for word in set_text:
            word_counter[word] = StringsCounter.count_words(word, text)        

        # Lo ordenamos el diccionario por el numero de veces que haya aparecido la palabra
        sorted_dic = sorted(word_counter.items(), key=operator.itemgetter(1), reverse=True)
       
        print (sorted_dic)
        print ("\nNumero de palabras: " + str(len(text)))
        print ("Numero de palabras diferentes: " + str(len(set_text)) + "\n")

        return sorted_dic

    @staticmethod
    def clear_stopwords(word):
        stopwords = set(['.', ',', '"', "'", '?', '!', ':',
                         ';', '(', ')', '[', ']', '{', '}'])
        for x in stopwords:
            word = word.replace(x, "")
        return word

    @staticmethod
    def count_words(word, text):
        cont = 0
        for i in range(len(text)):
            if word == text[i]:
                cont += 1
        return cont

    @staticmethod
    def print_solution(dic):
        print ("|      Words      | Count |")
        print ("---------------------------")
        for item in dic:
            space = 0
            for x in [ord(c) for c in item[0]]:
                if x > 128:
                    space = space + 1
            print("| " + item[0] + " " * (16 - len(item[0]) + space) +
                  "| " + str(item[1]) + " " * (6 - len(str(item[1]))) + "|")
        print ("\n")
