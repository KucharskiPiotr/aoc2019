import sys

def calc_required_fuel(mass):
    return mass // 3 - 2

def calc_fuel_for_fuel(fuel_mass):
    res = 0
    r = calc_required_fuel(fuel_mass)
    while(r > 0):
        res = res + r
        r = calc_required_fuel(r)
    return res

if __name__ == '__main__':
    input_lines = filter(None, open('input', 'r').read().split('\n'))
    required_fuels = []
    for line in input_lines:
        fuel_for_module = calc_required_fuel(int(line))
        fuel_for_fuel = calc_fuel_for_fuel(fuel_for_module)
        required_fuels.append(fuel_for_module + fuel_for_fuel)

    fuel_required = sum(int(i) for i in required_fuels)
    print('Required fuel:', fuel_required)
