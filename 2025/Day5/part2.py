import sys

def main(id_ranges):
    fresh_id_ranges = list()
    for id_range in id_ranges:
        if len(fresh_id_ranges) == 0:
            fresh_id_ranges.append(id_range)
        else:
            for fresh_id_range in fresh_id_ranges:
                if all([
                    int(fresh_id_range[0]) <= int(id_range[0]) <= int(fresh_id_range[1]),
                    int(id_range[0]) <= int(fresh_id_range[0])
                ]):
                    pass
                    # need to make range() for indeces of fresh_id_range

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        content = f.read()
        content_split = content.split('\n')
        id_ranges = list()
        for item in content_split:
            if item == '':
                break
            id_ranges.append(item)
        print(main(id_ranges))
