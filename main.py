import sys
from sample.strings_counter import StringsCounter

if __name__ == "__main__":
    args = sys.argv[1:]
    print StringsCounter.count_strings(args)
