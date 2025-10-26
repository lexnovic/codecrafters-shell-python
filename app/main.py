import sys

def repl():
    while True:
        try:
            sys.stdout.write("$ ")
            command = input()
            if not command:
                continue
            if "exit" in command:
                exit()
            print(f"{command}: command not found")
        except (EOFError, KeyboardInterrupt):
            print()
            break

def exit():
    sys.exit(0)


if __name__ == "__main__":
    repl()
