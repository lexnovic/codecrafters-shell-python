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

def find_in_path(cmd):
    paths = os.environ.get("PATH", "").split(os.pathsep)
    for path in paths:
        full_path = (os.path.join(path, cmd))
        path_count = 0
        if os.path.exists(full_path):
            path_count += 1
            if path_count == 2:
                return full_path

def do_type(parts):
    if len(parts) == 1:
        print("Specify command.")
    else:
        cmd = parts[1]
        if cmd in builtin_commands:
            print(f"{cmd} is a shell builtin")
        else:
            path = find_in_path(cmd)
            if path:
                print(f"{cmd} is {path}")
            else:
                print(f"{cmd}: not found")


if __name__ == "__main__":
    repl()
