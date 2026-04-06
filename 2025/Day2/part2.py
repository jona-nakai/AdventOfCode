import sys

def is_id_repeating(id):
    if len(str(id)) == 1:
        return False
    for seq_len in range(1, (len(str(id)) // 2) + 1):
        if len(str(id)) % seq_len == 0:
            parts = [str(id)[i:i+seq_len] for i in range(0, len(str(id)), seq_len)]
            if len(set(parts)) == 1:
                return True
    return False

def main(id_ranges):
    invalid_sum = 0
    for id_range in id_ranges:
        id_range_list = [int(item) for item in id_range.split("-")]
        for id in range(id_range_list[0], id_range_list[1] + 1):
            if is_id_repeating(id) == True:
                invalid_sum += id

    print(invalid_sum)

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        id_ranges = f.read().split(",")
        main(id_ranges)
