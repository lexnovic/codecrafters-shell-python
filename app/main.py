import sys

builtin_commands = ["exit", "echo", "type"]

def repl():
    while True:
        try:
            sys.stdout.write("$ ")
            command = input()
            if not command:
                continue
            elif "exit" in command:
                do_exit()
            elif "echo" in command:
                do_echo(command)
            elif "type" in command:
                do_type(command)
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

def do_type(command):
    parts = command.split()
    if len(parts) == 1:
        print("Specify command.")
    else:
        if parts[1] in builtin_commands:
            print(f"{parts[1]} is a shell builtin")
        else:
            print(f"{parts[1]}: command not found")


if __name__ == "__main__":
    repl()
