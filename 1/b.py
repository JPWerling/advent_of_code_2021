import sys

def main():
    input_path = sys.argv[1]

    with open(input_path, 'r') as inp:
        measurements = [int(i) for i in inp.readlines()]

    # Count number of increases
    incr = 0

    # Store previous sum. Start at huge to ensure no increase.
    prev = 99999

    for i,_ in enumerate(measurements):
        try:
            s = sum(measurements[i:i+3])
        except IndexError:
            pass
        if s > prev:
            incr += 1
        prev = s

    print(incr)


if __name__ == '__main__':
    main()
