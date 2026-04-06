import sys

def main(rotations):

    # intialize password and dial
    password = 0
    dial = 50

    for rotation in rotations:

        # parse inputs into direction (L or R) and distance
        direction = rotation[0]
        distance = int(rotation[1:])

        if direction == "L":
            moved_dial = dial - distance
            if dial == 0:
                counter_0 = abs(((moved_dial - 1) // 100) + 1)
            elif dial != 0:
                counter_0 = abs((moved_dial - 1) // 100)

        elif direction == "R":
            moved_dial = dial + distance
            counter_0 = moved_dial // 100

        password += counter_0
        dial = moved_dial % 100
    
    print(password)

if __name__ == "__main__":
    filename = sys.argv[1]

    with open(filename) as f:
        rotations = f.read().splitlines()
        main(rotations)