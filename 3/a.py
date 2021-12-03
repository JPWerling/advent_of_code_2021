import sys

from collections import Counter


def main():
    input_path = sys.argv[1]

    with open(input_path, 'r') as inp:
        raw_binaries = [i.strip() for i in inp.readlines()]

    length = len(raw_binaries[0])

    gamma = ''
    epsi = ''
    for i in range(length):
        bin_ints = [e[i] for e in raw_binaries]

        most_common, least_common = Counter(bin_ints).most_common()
        gamma += most_common[0]
        epsi += least_common[0]

    power_consumption = int(gamma, base=2) * int(epsi, base=2)
    print(power_consumption)


if __name__ == '__main__':
    main()
