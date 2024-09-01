import traceback
from simple_test.simple import get_stack

def test_stack():

    trace = get_stack()
    trace_list = traceback.format_list(trace)
    trace_length = len(trace_list)
    print("\n\n\n\n\n\n")
    print("trace: \n", trace_list)
    print("\n\n")
    print("trace length: \n", trace_length)
    print("\n\n\n\n\n\n")

    expected_trace_str_length = 34
    print("\n\n")
    assert trace_length == expected_trace_str_length

