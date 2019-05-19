import argparse


parser = argparse.ArgumentParser()
parser.add_argument("number", type=int, help="display a square of a number")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")

args = parser.parse_args()
answer = args.number**2

if args.verbose:
    print("the square of {} equals {}".format(args.number, answer))
else:
    print(answer)