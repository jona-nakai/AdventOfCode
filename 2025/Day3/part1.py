import sys

def max_bank_battery(bank):
    temp_bank = bank[:-1]
    max_left_digit = str(max(list(temp_bank)))
    max_left_digit_index = bank.find(max_left_digit)
    temp_bank_2 = bank[max_left_digit_index + 1:]
    max_right_digit = str(max(list(temp_bank_2)))

    return int(max_left_digit + max_right_digit) 

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
