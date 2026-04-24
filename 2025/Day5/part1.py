import sys

def main(id_ranges, ids):
    fresh_ids = 0
    for id in ids:
        for id_range in id_ranges:
            if int(id_range[0]) <= int(id) <= int(id_range[1]):
                fresh_ids +=1
                break

    return fresh_ids

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        content = f.read()
        content_split = content.split('\n')

        id_ranges = list()
        ids = list()
        id_or_range = 0
        for item in content_split[:-1]:
            if item == '':
                id_or_range = 1
            elif id_or_range == 0:
                id_ranges.append(item.split('-'))
            else:
                ids.append(item)

        print(main(id_ranges, ids))
