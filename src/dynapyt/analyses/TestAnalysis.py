from .BaseAnalysis import BaseAnalysis
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple, Union

class TestAnalysis(BaseAnalysis):
    # def __init__(self) -> None:
    #     super().__init__()
    

    # def enter_try(self, dyn_ast: str, iid: int) -> None:
    #     print("Enter try called: ", iid)

    # def clean_exit_try(self, dyn_ast: str, iid: int) -> None:
    #     print("Exit try called: ", iid)

    # def enter_control_flow(
    #     self, dyn_ast: str, iid: int, cond_value: bool
    # ) -> Optional[bool]:
    #     print("Enter control flow: ", iid)

    # def exit_control_flow(self, dyn_ast: str, iid: int) -> None:
    #     print("Exit control flow : ", iid)


    # def enter_if(self, dyn_ast: str, iid: int, cond_value: bool) -> Optional[bool]:
    #     print("Enter if called: ", iid)

    # def exit_if(self, dyn_ast, iid):
    #     print("Exit if called: ", iid)

    # def enter_for(
    #     self, dyn_ast: str, iid: int, next_value: Any, iterable: Iterable
    # ) -> Optional[Any]:
    #     print("Enter for called: ", iid)

    # def exit_for(self, dyn_ast, iid):
    #     print("Exit for called: ", iid)

    # def boolean(self, dyn_ast: str, iid: int, val: Any) -> Any:
    #     print("Boolean hook called: ", iid)


    # def enter_while(self, dyn_ast: str, iid: int, cond_value: bool) -> Optional[bool]:
    #     print("Enter while called: ", iid)

    # def exit_while(self, dyn_ast, iid):
    #     print("Exit while called: ", iid)

    def enter_with(self, dyn_ast: str, iid: int, func, args) -> None:
        print("Enter with called: ", iid)

    def exit_with(self, dyn_ast, iid):
        print("Exit with called: ", iid)

    # def binary_operation(
    #     self, dyn_ast: str, iid: int, op: str, left: Any, right: Any, result: Any
    # ) -> Any:
    #     print("Binary operation called: ", iid)


    
