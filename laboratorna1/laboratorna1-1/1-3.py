import argparse

parser = argparse.ArgumentParser()
parser.add_argument('formula', type=str, help='formula')
args = parser.parse_args()

try:
    if args.formula[0].isdigit() and args.formula[-1].isdigit() and '++' not in args.formula.replace('-', '+') and args.formula.replace('-', '').replace('+', '').isdigit():
        print("True,", eval(args.formula))
    else:
        print("False, None")

except (EOFError, IndexError, SyntaxError, TypeError, KeyError, NameError, KeyboardInterrupt):
    print("Invalid Syntax")
