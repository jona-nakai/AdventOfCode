import sys

def main(id_ranges):
    invalid_sum = 0
    for id_range in id_ranges:
        id_range_list = [int(item) for item in id_range.split("-")]
        for id in range(id_range_list[0], id_range_list[1] + 1):
            id_str = str(id)
            id_length = len(id_str)
            if id_length % 2 == 0:
                id_half = int(id_length / 2)
                if id_str[:id_half] == id_str[id_half:]:
                    invalid_sum += id

    print(invalid_sum)

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        id_ranges = f.read().split(",")
        main(id_ranges)