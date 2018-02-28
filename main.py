import sys
from sample.strings_example import StringsExamples

if __name__ == "__main__":
    args = sys.argv[1:]
    print StringsExamples.concat_strings(args[0], args[1])
