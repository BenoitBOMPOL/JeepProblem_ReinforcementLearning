"""
    File describing the [pick_up_fuel] action
"""
from .action import Action, UnfeasibleActionError
from ..jeep_state import JeepState

class PickUpFuel(Action):
    def __init__(self, param: int):
        super().__init__('pick_up_fuel', param)

    def check(self, jeep_st: JeepState) -> bool:
        if self.param == 0:
            return False
        if jeep_st.position not in jeep_st.deposits:
            return False
        if jeep_st.deposits.get(jeep_st.position) < self.param:
            return False
        if self.param + jeep_st.fuel > jeep_st.reservoir:
            return False
        return True
    
    def apply(self, jeep_st: JeepState):
        if self.check(jeep_st):
            jeep_st.deposits[jeep_st.position] -= self.param
            jeep_st.fuel += self.param
        else:
            raise UnfeasibleActionError(str(self))
