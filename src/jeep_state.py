"""
    File describing each state of an instance
"""

class JeepState:
    def __init__(self,
                 reservoir: int,
                 init_fuel: int):
        self.reservoir: int = reservoir
        self.init_fuel: int = init_fuel

        self.deposits: dict[int, int] = {0: init_fuel}

        self.furthest_reached: int = -1
        self.position: int = 0
        self.fuel: int = 0


    def __str__(self) -> str:
        """
            String representation of the current Jeep state.
        """
        deposits_str = ', '.join(f'{pos_}: {fuel_}'
                                 for pos_, fuel_ in self.deposits.items())
        return (f'-----------------------------------\n'
                f'|======= 🚙 Jeep State 🚙 ========|\n'
                f'|----------------------------------\n'
                f'|🔹 Position actuelle     : {self.position}\n'
                f'|🔹 Distance max atteinte : {self.furthest_reached}\n'
                f'|⛽ Carburant transporté  : {self.fuel}/{self.reservoir}\n'
                f'|📍 Dépôts de carburant   : {deposits_str}\n'
                f'-----------------------------------\n')
