from domain import State, Map, generate_problem
from constraints import define_constrains
from optapy import get_class
import optapy.config
from optapy.types import Duration

solver_config = optapy.config.solver.SolverConfig() \
    .withEntityClasses(get_class(State)) \
    .withSolutionClass(get_class(Map)) \
    .withConstraintProviderClass(get_class(define_constrains)) \
    .withTerminationSpentLimit(Duration.ofSeconds(10))

from optapy import solver_factory_create

solution = solver_factory_create(solver_config)\
    .buildSolver()\
    .solve(generate_problem())
print(solution)

from plotter import plot
plot(solution)