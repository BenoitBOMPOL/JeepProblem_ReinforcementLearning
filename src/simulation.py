from .jeep_state import JeepState
from .actions.action import Action
from .actions.leave_fuel import LeaveFuel
from .actions.pick_up_fuel import PickUpFuel
from .actions.move_forward import MoveForward
from .actions.move_backward import MoveBackward

def list_feasible_actions(jeep_st: JeepState) -> list[Action]:
    """
        List all feasible actions
    """
    feasible_actions: list[Action] = []

    amt_lf = 1
    lf = LeaveFuel(amt_lf)
    while lf.check(jeep_st):
        feasible_actions.append(lf)
        amt_lf += 1
        lf = LeaveFuel(amt_lf)

    amt_puf = 1
    puf = PickUpFuel(amt_puf)
    while puf.check(jeep_st):
        feasible_actions.append(puf)
        amt_puf += 1
        puf = PickUpFuel(amt_puf)

    amt_mf = 1
    mf = MoveForward(amt_mf)
    while mf.check(jeep_st):
        feasible_actions.append(mf)
        amt_mf += 1
        mf = MoveForward(amt_mf)

    amt_mb = 1
    mb = MoveBackward(amt_mb)
    while mb.check(jeep_st):
        feasible_actions.append(mb)
        amt_mb += 1
        mb = MoveBackward(amt_mb)
    
    return feasible_actions


import random as rd

def simulation(reservoir: int, init_fuel: int) -> list[str]:
    jp_st: JeepState = JeepState(reservoir, init_fuel)
    actions: list[Action] = list_feasible_actions(jp_st)
    plan: list[tuple[str, int]] = []
    while len(actions) > 0:
        chosen_action = rd.choice(actions)
        plan.append(chosen_action.export())
        print(chosen_action)
        chosen_action.apply(jp_st)
        print(jp_st)
    return plan
