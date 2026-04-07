import sys

def max_bank_battery(bank):
    temp_bank = bank
    joltage = ''
    i = 11

    while i >= 1:
        max_digit = str(max([int(d) for d in temp_bank[:-1 * i]]))
        max_digit_index = temp_bank.find(max_digit)
        temp_bank = temp_bank[max_digit_index + 1:]
        joltage += max_digit
        i -= 1

    max_digit = str(max([int(d) for d in temp_bank]))
    joltage += max_digit

    return int(joltage)

def main(banks):
    bank_total = 0
    for bank in banks:
        bank_total += max_bank_battery(bank)

    return bank_total

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        banks = f.read().split("\n")[:-1]
        print(main(banks))
