import traceback
import os.path

def add_one(x: int) -> int:
    return x + 1


def multiply_two(x: int) -> int:
    return x * 2


def add_together(x: int, y: int) -> int:
    return x + y


def get_stack():
    trace = traceback.extract_stack()
    trace_list = traceback.format_list(trace)
    trace_length = len(trace_list)
    filename = "trace_length.txt"
    if os.path.exists(filename):
        filename = "trace_length1.txt"
    with open(filename, "w") as f:
        f.write(str(trace_length))
        f.write("\n")
        f.write(str(trace_list))
    
    return trace