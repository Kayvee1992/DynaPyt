from importlib import import_module
from inspect import getmembers, isclass
import json
from pathlib import Path
import pytest
import sys

from dynapyt.analyses.BaseAnalysis import BaseAnalysis
from dynapyt.instrument.instrument import instrument_file
from dynapyt.utils.hooks import get_hooks_from_analysis

here = Path(__file__).parent

def run_project(project: Path):
    project_dir = project.resolve()
    json_report_file = project_dir / "result.json"
    result = pytest.main(["-v", "--json-report", "--json-report-file="+str(json_report_file), str(project_dir/"tests"), ])
    with open(json_report_file, "r") as f:
        result = f.read()

    result_json = json.loads(result)
    test_result_map = {}
    for item in result_json["tests"]:
        test_result_map[item["nodeid"]] = item["outcome"]
    print(f"Test result without instrumentation: ")
    for key, value in test_result_map.items():
        print(f"{key}: {value}")

    json_report_file.unlink()
    
    return test_result_map


def run_instrumented_project(project):

    selected_hooks = get_hooks_from_analysis(["dynapyt.analyses.ExecutionInvarianceTestAnalysis.Analysis"])
    print(f"Selected hooks: {selected_hooks}")
    project_dir = project.resolve()
    project_src_dir = project_dir / "src"
    for code_file in project_src_dir.rglob("*.py"):
        instrument_file(str(project_dir / code_file), selected_hooks)

    json_report_file = project_dir / "instrumented_result.json"
    result = pytest.main(["-v", "--json-report", "--json-report-file="+str(json_report_file), str(project_dir/"tests"), ])
    with open(json_report_file, "r") as f:
        result = f.read()
    
    result_json = json.loads(result)
    test_result_map = {}
    for item in result_json["tests"]:
        test_result_map[item["nodeid"]] = item["outcome"]
    print(f"Test result with instrumentation: ")
    for key, value in test_result_map.items():
        print(f"{key}: {value}")

    # Clean up the project
    for code_file in project_dir.rglob("*.py.orig"):
            metadata_file = (
                project_dir
                / Path(*(code_file.parts[:-1]))
                / (code_file.name[:-8] + "-dynapyt.json")
            )
            metadata_file.unlink()
            correct_file = (
                project_dir
                / Path(*(code_file.parts[:-1]))
                / (code_file.name[:-8] + ".py")
            )
            code_file.rename(correct_file)
    json_report_file.unlink()

    return test_result_map


def run_tests():
    end_to_end_tests_dir = here.parent
    project_dir = end_to_end_tests_dir / "projects"
    failed = False
    # Run the tests with and without instrumentation
    for project in project_dir.iterdir():
        print(f"Running project {project.name}")
        test_result = run_project(project)
        instrumented_test_result = run_instrumented_project(project)
        for test, result in test_result.items():
            if (test not in instrumented_test_result):
                print(f"Test {test} not found in instrumented test results")
                failed = True
                break
            if (result != instrumented_test_result[test]):
                print(f"Test {test} results do not match")
                failed = True
                break
        print(f"Test results match for project {project.name} before and after instrumentation")
    print("All tests passed")

    if failed:
        print("Test results do not match before and after instrumentation")
        return False
    return True
            

                   
                    


if __name__ == "__main__":
    run_tests()