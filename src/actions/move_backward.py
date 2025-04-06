"""
    File describing the [move_backward] action
"""
from .action import Action, UnfeasibleActionError
from ..jeep_state import JeepState

class MoveBackward(Action):
    def __init__(self, param: int):
        super().__init__('move_backward', param)

    def check(self, jeep_st: JeepState) -> bool:
        if self.param == 0:
            return False
        return self.param <= min(jeep_st.fuel,
                                 jeep_st.position)
    
    def apply(self, jeep_st: JeepState):
        if self.check(jeep_st):
            jeep_st.position -= self.param
            jeep_st.fuel -= self.param
        else:
            raise UnfeasibleActionError(str(self))
