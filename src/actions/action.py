"""
    File describing a generic action
"""
from ..jeep_state import JeepState

class UnfeasibleActionError(Exception):
    pass

class Action:
    def __init__(self,
                 name: str = '',
                 param: int = 0):
        self.name: str = name
        self.param: int = param
    
    def __str__(self):
        return f'Action [{self.name}] - {self.param}'

    def check(self, jeep_st: JeepState) -> bool:
        raise NotImplementedError
    
    def apply(self, jeep_st: JeepState):
        if self.check(jeep_st):
            raise NotImplementedError
        else:
            raise UnfeasibleActionError(str(self))

    def export(self):
        return (self.name, self.param)