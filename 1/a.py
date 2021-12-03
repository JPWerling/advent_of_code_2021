import sys


def main():
    input_path = sys.argv[1]

    with open(input_path, 'r') as inp:
        measurements = [int(i) for i in inp.readlines()]

    # Count number of increases
    incr = 0

    # Store previous depth. Start at huge to ensure no increase.
    prev = 99999

    for m in measurements:
        if m > prev:
            incr += 1
        prev = m

    print(incr)


if __name__ == '__main__':
    main()
