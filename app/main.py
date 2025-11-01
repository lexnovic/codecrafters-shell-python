import sys
import os

builtin_commands = ["exit", "echo", "type"]

def repl():
    while True:
        try:
            sys.stdout.write("$ ")
            command = input()
            parts = command.split()
            if not command:
                continue
            elif parts[0] == "exit":
                do_exit()
            elif parts[0] == "echo":
                do_echo(parts)
            elif parts[0] == "type":
                do_type(parts)
            else:
                print(f"{command}: command not found")
        except (EOFError, KeyboardInterrupt):
            print()
            break

def do_exit():
    sys.exit(0)

def do_echo(parts):
    if len(parts) > 1:
        print(" ".join(parts[1:]))
    else:
        print()

def do_type(parts):
    if len(parts) == 1:
        print("Specify command.")
    else:
        if parts[1] in builtin_commands:
            print(f"{parts[1]} is a shell builtin")
        elif parts[1] not in builtin_commands:
            if os.path.exists(parts[1:]):
                print(f"{os.path.dirname(parts[1:])}")
            else:
                print(f"{parts[1]}: not found")


if __name__ == "__main__":
    repl()
