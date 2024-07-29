# DYNAPYT: DO NOT INSTRUMENT


from dynapyt.runtime import RuntimeEngine
_rt = RuntimeEngine()

_dynapyt_ast_ = "/Users/keerthiv/Masters/Masters/University_of_Stuttgart/Job/dynapyt/dynapyt/DynaPyt/tests/trace_single_hook/with/with_multiple_items/program.py" + ".orig"
try:
    import os
    
    dir_name = os.path.dirname(os.path.realpath(__file__))
    file_path_1 = os.path.join(dir_name, "expected.txt")
    file_path_2 = os.path.join(dir_name, "analysis.py")
    with _rt._enter_with_(_dynapyt_ast_, 0, open(file_path_1, "r")) as file1, _rt._enter_with_(_dynapyt_ast_, 1, open(file_path_2, "r")) as file2:
        content = file1.readline()
        print("Line read from expected.txt: ", content)
        content = file2.readline()
        print("Line read from analysis.py: ", content)
        print("content has been read from the files")
    
    print("file has been closed")
except Exception as _dynapyt_exception_:
    _rt._catch_(_dynapyt_exception_)

