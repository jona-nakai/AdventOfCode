def main(rotations):
    password = 0
    dial = 50
    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])
        if direction == "L":
            new_dial = (dial - distance) % 100
        elif direction == "R":
            new_dial = (dial + distance) % 100
        else:
            raise ValueError(f"First character in rotation was {direction}. Must be 'L' or 'R'")

        if new_dial == 0:
            password += 1
        
        dial = new_dial
    
    print(password)

if __name__ == "__main__":
    with open("input") as f:
        rotations = f.read().splitlines()
        main(rotations)