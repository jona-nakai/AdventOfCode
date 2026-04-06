with open("input") as f:
    content = f.read()
    # print(content)

floor = 0
position = 1

for a in content:
    if a == '(':
        floor = floor + 1
    else:
        floor = floor - 1
    
    if floor == - 1: 
        print(position)
        break

    position = position + 1

