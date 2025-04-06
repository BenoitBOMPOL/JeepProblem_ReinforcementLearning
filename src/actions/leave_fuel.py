"""
    File describing the [leave_fuel] action
"""
from .action import Action, UnfeasibleActionError
from ..jeep_state import JeepState

class LeaveFuel(Action):
    def __init__(self, param: int):
        super().__init__('leave_fuel', param)

    def check(self, jeep_st: JeepState) -> bool:
        if self.param == 0:
            return False
        return self.param <= jeep_st.fuel
    
    def apply(self, jeep_st: JeepState):
        if self.check(jeep_st):
            jeep_st.deposits[jeep_st.position] = jeep_st.deposits.get(jeep_st.position, 0) + self.param
            jeep_st.fuel -= self.param
        else:
            raise UnfeasibleActionError(str(self))
