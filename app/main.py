import sys

def input():
    while True:
        try:
            sys.stdout.write("$ ")
            command = input()
            if not command:
                continue
            print(f"{command}: command not found")
        except (EOFError, KeyboardInterrupt):
            print()
            break



if __name__ == "__main__":
    input()
