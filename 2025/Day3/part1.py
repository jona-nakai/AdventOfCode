import sys

def main():
    pass

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        content = f.read().split("\n")[:-1]
        print(content)
        main()
