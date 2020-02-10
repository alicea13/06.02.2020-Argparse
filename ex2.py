import sys
import argparse


parser = argparse.ArgumentParser()
args = parser.parse_args([i.strip() for i in sys.argv[1:]])


barbie, cars, movie = 50, 50, 50

parser.add_argument("args", metavar="arg", nargs='*')
parser.add_argument('--cars', type=int, nargs='?', default=50)
parser.add_argument('--barbie', type=int, nargs='?', default=50)
parser.add_argument('--movie', type=str, nargs='?', default='other', action='store_true')


# print(args.movie)

'''
for i in args.args[::2]:
    print(i)
    if i == '--barbie':
        print(args.args[args.args.index(i) + 1])
        barbie = args.args[args.args.index(i) + 1]
    if i == '--cars':
        print(args.args[args.args.index(i) + 1])
        cars = args.args[args.args.index(i) + 1]
    if i == '--movie':
        print(args.args[args.args.index(i) + 1])
        if args.args[args.args.index(i) + 1] == 'melodrama':
            movie = 0
        if args.args[args.args.index(i) + 1] == 'football':
            movie = 100'''
# print(args.barbie)

boy = (100 - args.barbie + args.cars + args.movie) / 3
girl = (100 - boy)
print(int(boy))
print(girl)