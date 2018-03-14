import sys
from sample.strings_counter import StringsCounter

if __name__ == "__main__":
    args = sys.argv[1:]
    #Esto imprimira el resultado de forma bonita
    dic = StringsCounter.count_strings(args)
    StringsCounter.print_solution(dic)
