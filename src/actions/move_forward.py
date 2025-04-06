"""
    File describing the [move_forward] action
"""
from .action import Action, UnfeasibleActionError
from ..jeep_state import JeepState

class MoveForward(Action):
    def __init__(self, param: int):
        super().__init__('move_forward', param)
    
    def check(self, jeep_st: JeepState) -> bool:
        if self.param == 0:
            return False
        return self.param <= jeep_st.fuel
    
    def apply(self, jeep_st: JeepState):
        if self.check(jeep_st):
            jeep_st.position += self.param
            jeep_st.fuel -= self.param
            jeep_st.furthest_reached = max(jeep_st.furthest_reached,
                                           jeep_st.position)
        else:
            raise UnfeasibleActionError(str(self))
