import argparse

parser = argparse.ArgumentParser()
parser.add_argument("arg1")
parser.add_argument("arg2", help="echo this string")
parser.add_argument("int_args", metavar="N", type=int,
                    nargs='+', help="echo some integers")
args = parser.parse_args('-h')

print(args.arg1)
print(args.arg2)
print(args.int_args)