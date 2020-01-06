import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--value", help="the basic value")
parser.add_argument("--loc", help="the loc")
args = parser.parse_args()
if args.value:
    print("value is {0}".format(args.value))
    
if args.loc:
    print("loc is {0}".format(args.loc))
