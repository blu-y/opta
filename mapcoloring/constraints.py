from domain import Color, State, isAdjacent
from optapy import constraint_provider, get_class
from optapy.constraint import Joiners
from optapy.score import HardSoftScore

ColorClass = get_class(Color)
StateClass = get_class(State)

@constraint_provider
def define_constrains(constraint_factory):
    return [
        color_conflict(constraint_factory)
    ]

def color_conflict(constraint_factory):
    return constraint_factory \
            .forEach(StateClass) \
            .join(StateClass,
                  [
                      Joiners.equal(lambda state: state.color),
                      Joiners.filtering(lambda state1, state2: isAdjacent(state1, state2))
                ]) \
            .penalize("Color conflict", HardSoftScore.ONE_HARD)