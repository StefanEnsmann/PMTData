import sys
import argparse

def exclusion(value):
    try:
        return [int(value)]
    except:
        values = value.split('-')
        if len(values) != 2:
            raise argparse.ArgumentTypeError('Exclusion is neither an int nor a range x-y: ' + value)
        try:
            v1, v2 = int(values[0]), int(values[1])
            return list(range(v1, v2 + 1))
        except:
            raise argparse.ArgumentTypeError('Exclusion range could not be parsed to ints: ' + value)

def parse_arguments():
    parser = argparse.ArgumentParser('Number Range Generator')
    parser.add_argument('--lower', '-l', type=int, default=1)
    parser.add_argument('--upper', '-u', type=int, default=100)
    parser.add_argument('--separator', '-s', type=str, default=', ')
    parser.add_argument('--exclude', '-e', type=exclusion, nargs='*')
    return parser.parse_args(sys.argv[1:])

def main():
    args = parse_arguments()
    exc = [] if args.exclude is None else sum(args.exclude, [])
    print(args.separator.join([str(i) for i in range(args.lower, args.upper + 1) if i not in exc]))

if __name__ == "__main__":
    main()