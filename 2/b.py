import sys


class Navigation:
    def __init__(self, pos_vt, pos_hz, aim):
        self.current_vt = pos_vt
        self.current_hz = pos_hz
        self.current_aim = aim

    def move_forward(self, n):
        self.current_hz = self.current_hz + n
        self.current_vt = self.current_vt + (self.current_aim * n)

    def aim_down(self, n):
        self.current_aim = self.current_aim - n

    def aim_up(self, n):
        self.current_aim = self.current_aim + n

    def move(self, direction, n):
        n  = int(n)
        if direction == 'forward':
            self.move_forward(n)
        if direction == 'down':
            self.aim_down(n)
        if direction == 'up':
            self.aim_up(n)


def main():
    input_path = sys.argv[1]

    with open(input_path, 'r') as inp:
        commands = inp.readlines()

    Nav = Navigation(0, 0, 0)
    for command in commands:
        direction, n = command.split(' ')
        Nav.move(direction, n)

    print(Nav.current_vt * -Nav.current_hz)  # NOTE: Negative as we count depth as negative vertical


if __name__ == '__main__':
    main()
