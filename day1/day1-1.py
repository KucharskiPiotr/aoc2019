import sys

def calc_required_fuel(mass):
    return mass // 3 - 2

if __name__ == '__main__':
    input_lines = filter(None, open('input', 'r').read().split('\n'))
    required_fuels = []
    for line in input_lines:
        required_fuels.append(calc_required_fuel(int(line)))
    print('Required fuel:', sum(int(i) for i in required_fuels))
