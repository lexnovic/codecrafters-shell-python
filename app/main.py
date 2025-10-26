import sys

def repl():
    while True:
        try:
            sys.stdout.write("$ ")
            command = input()
            if not command:
                continue
            if "exit" in command:
                do_exit()
            elif "echo" in command:
                do_echo(command)
            else:
                print(f"{command}: command not found")
        except (EOFError, KeyboardInterrupt):
            print()
            break

def do_exit():
    sys.exit(0)

def do_echo(command):
    parts = command.split()
    if len(parts) > 1:
        print(" ".join(parts[1:]))
    else:
        print()


if __name__ == "__main__":
    repl()
