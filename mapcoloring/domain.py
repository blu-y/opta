from optapy import problem_fact, planning_id

@problem_fact
class Color:
    def __init__(self, id, color):
        self.id = id
        self.color = color
    
    @planning_id
    def get_id(self):
        return self.id

    def __str__(self):
        return f"Color(id={self.id}, color={self.color})"
    
    
from optapy import planning_entity, planning_variable

@planning_entity
class State:
    def __init__(self, id, name, neighbor=None, color=None):
        self.id = id
        self.name = name
        self.color = color
        self.neighbor = neighbor
    
    @planning_id
    def get_id(self):
        return self.id
    
    @planning_variable(Color, ["colorRange"])
    def get_color(self):
        return self.color
    
    def set_color(self, new_color):
        self.color = new_color

    def __str__(self):
        return (
            f"State(id={self.id}, "
            f"name={self.name}, "
            f"color={self.color})"
        )

from optapy import planning_solution, planning_entity_collection_property, \
                   problem_fact_collection_property, \
                   value_range_provider, planning_score
from optapy.score import HardSoftScore

def format_list(a_list):
    return ',\n'.join(map(str, a_list))

@planning_solution
class Map:
    def __init__(self, color_list, state_list, score=None):
        self.color_list = color_list
        self.state_list = state_list
        self.score = score

    @problem_fact_collection_property(Color)
    @value_range_provider("colorRange")
    def get_color_list(self):
        return self.color_list
    
    @planning_entity_collection_property(State)
    def get_state_list(self):
        return self.state_list
    
    @planning_score(HardSoftScore)
    def get_score(self):
        return self.score
    
    def set_score(self, score):
        self.score = score

    def __str__(self):
        return (
            f"Map("
            f"color_list={format_list(self.color_list)}, \n"
            f"state_list={format_list(self.state_list)}, \n"
            f"score={str(self.score.toString()) if self.score is not None else 'None'})"
        )
    
def isAdjacent(state1, state2):
    if state1.id in state2.neighbor:
        return True
    else: return False

def generate_problem():
    color_list = [
        Color(1, 'Red'),
        Color(2, 'Green'),
        Color(3, 'Blue')
    ]
    state_list = [
        State(1, 'Western Austrailia', [2,3]),
        State(2, 'Northern Territory', [1,3,4]),
        State(3, 'South Austrailia', [1,2,4,5,6]),
        State(4, 'Queensland', [2,3,5]),
        State(5, 'New South Wales', [3,4,6]),
        State(6, 'Victoria', [3,5]),
        State(7, 'Tasmania', []),
    ]
    
    state = state_list[0]
    state.set_color(color_list[0])

    return Map(color_list, state_list)