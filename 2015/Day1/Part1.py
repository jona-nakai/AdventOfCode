with open("input") as f:
    content = f.read()
    # print(content)

floor = 0

for a in content:
    if a == '(':
        floor = floor + 1
    else:
        floor = floor - 1

print(floor)