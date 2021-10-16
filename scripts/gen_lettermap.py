"""
gen_lettermap

Usage: python gen_lettermap.py > lettermap.js

Generates a map that maps Hangul Jaso characters to Hangul Compatible Jaso.
"""
import unicodedata

def flatten(*args):
    """
    flatten all arguments into single iterable
    """
    for arg in args:
        try:
            _ = iter(arg)
        except TypeError:
            yield arg
            continue
        for i in flatten(*arg):
            yield i


def main():
    """
    Create a js-style hangul letter map and print it into stdout.
    """
    print("export const hangulLetterMap = {")
    for i in flatten(range(0x1100, 0x1113), range(0x1161, 0x1176), range(0x11a8, 0x11c3)):
        base = chr(i)
        base_name = unicodedata.name(base)
        hangul, _, name = base_name.split(' ')
        letter_name = '{} LETTER {}'.format(hangul, name)
        letter = unicodedata.lookup(letter_name)
        letter_code = ord(letter)
        print("  '\\u{:04x}': '\\u{:04x}', // {}".format(i, letter_code, base_name))
    print("}")


if __name__ == '__main__':
    main()
