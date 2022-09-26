import argparse
import math
import operator

parser = argparse.ArgumentParser()
parser.add_argument("operation", type=str)
parser.add_argument("formula", nargs="*", type=int)

args = parser.parse_args()
try:
    check_operation = getattr(operator, args.operation)
    print(check_operation(*args.formula))
except Exception:
    try:
        check_math = getattr(math, args.operation)
        print(check_math(*args.formula))
    except Exception:
        print("Wrong data")
