from typing import Optional
from dynapyt.analyses import BaseAnalysis


class TestAnalysis(BaseAnalysis):
    def begin_execution(self) -> None:
        print("begin execution")

    def enter_with(self, dyn_ast: str, iid: int):
        print(f"with statement entered")

    def exit_with(self, dyn_ast: str, iid: int):
        print(f"done with with statement")
        
    def end_execution(self) -> None:
        print("end execution")