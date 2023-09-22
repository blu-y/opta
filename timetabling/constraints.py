from domain import Lesson, Room
from optapy import constraint_provider, get_class
from optapy.constraint import Joiners
from optapy.score import HardSoftScore

# Constraint Factory takes Java Classes, not Python Classes
LessonClass = get_class(Lesson)
RoomClass = get_class(Room)

@constraint_provider
def define_constraints(constraint_factory):
    return [
        # Hard constraints
        room_conflict(constraint_factory),
        teacher_conflict(constraint_factory),
        student_group_conflict(constraint_factory),
        # Soft constraints are only implemented in the optapy-quickstarts code
    ]

def room_conflict(constraint_factory):
    # A room can accommodate at most one lesson at the same time.
    return constraint_factory \
            .forEach(LessonClass) \
            .join(LessonClass,
                [
                    # ... in the same timeslot ...
                    Joiners.equal(lambda lesson: lesson.timeslot),
                    # ... in the same room ...
                    Joiners.equal(lambda lesson: lesson.room),
                    # ... and the pair is unique (different id, no reverse pairs) ...
                    Joiners.lessThan(lambda lesson: lesson.id)
                ]) \
            .penalize("Room conflict", HardSoftScore.ONE_HARD)


def teacher_conflict(constraint_factory):
    # A teacher can teach at most one lesson at the same time.
    return constraint_factory \
                .forEach(LessonClass)\
                .join(LessonClass,
                        [
                            Joiners.equal(lambda lesson: lesson.timeslot),
                            Joiners.equal(lambda lesson: lesson.teacher),
                    Joiners.lessThan(lambda lesson: lesson.id)
                        ]) \
                .penalize("Teacher conflict", HardSoftScore.ONE_HARD)

def student_group_conflict(constraint_factory):
    # A student can attend at most one lesson at the same time.
    return constraint_factory \
            .forEach(LessonClass) \
            .join(LessonClass,
                [
                    Joiners.equal(lambda lesson: lesson.timeslot),
                    Joiners.equal(lambda lesson: lesson.student_group),
                    Joiners.lessThan(lambda lesson: lesson.id)
                ]) \
            .penalize("Student group conflict", HardSoftScore.ONE_HARD)