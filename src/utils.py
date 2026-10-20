import os
import sys


def clear():print("\033[H\033[J", end="")
def check(tasks, id):
    return str(id).isdigit() and 1 <= int(id) <= len(tasks)

def get_dase_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.realpath(__file__))