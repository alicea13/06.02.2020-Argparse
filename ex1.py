import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("args", metavar="arg", nargs='*')

args = parser.parse_args([i.strip() for i in sys.argv[1:]])
if args.args:
    for i in args.args:
        print(i)
else:
    print('no args')
