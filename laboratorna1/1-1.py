import argparse

parser = argparse.ArgumentParser()
parser.add_argument('test', type=int)
parser.add_argument('test2', type=str)
parser.add_argument('test3', type=int)

args = parser.parse_args()
if args.test2 == '*':
    print(args.test * args.test3)
elif args.test2 == '-':
    print(args.test-args.test3)
elif args.test2 == '+':
    print(args.test+args.test3)
elif args.test2 == '/':
    if not args.test3:
        print('Division by zero')
    else:
        print(args.test/args.test3)
else:
    print('Wrong data')
