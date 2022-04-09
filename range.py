import sys
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser('Number Range Generator')
    parser.add_argument('--lower', '-l', type=int, default=1)
    parser.add_argument('--upper', '-u', type=int, default=100)
    parser.add_argument('--separator', '-s', type=str, default=', ')
    parser.add_argument('--exclude', '-e', type=int, nargs='*')
    return parser.parse_args(sys.argv[1:])

def main():
    args = parse_arguments()
    exc = [] if args.exclude is None else args.exclude
    print(args.separator.join([str(i) for i in range(args.lower, args.upper + 1) if i not in exc]))

if __name__ == "__main__":
    main()