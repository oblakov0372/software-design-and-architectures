import random
import time
from instructor import Instructor
from athlete import Athlete
from training_modes import BasicTrainingMode, CardioTrainingMode, StrengthTrainingMode
from training_program import (
    BasicTrainingProgram,
    CardioDecorator,
    StrengthTrainingDecorator,
)
from utils.logger import logger


class Gym:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Gym, cls).__new__(cls)
        return cls._instance

    def __init__(self, name):
        if not hasattr(self, "_initialized"):
            self.name = name
            self._initialized = True
            self.instructor = Instructor("Ivan Ivanov")
            self.athletes: list[Athlete] = []
            self.training_programs = {
                "basic": BasicTrainingProgram(),
                "cardio": CardioDecorator(BasicTrainingProgram()),
                "strength": StrengthTrainingDecorator(BasicTrainingProgram()),
                "full": StrengthTrainingDecorator(
                    CardioDecorator(BasicTrainingProgram())
                ),
            }
            self.training_modes = {
                "basic": BasicTrainingMode(),
                "cardio": CardioTrainingMode(),
                "strength": StrengthTrainingMode(),
            }

    def add_athlete(self, athlete: Athlete):
        self.athletes.append(athlete)
        self.instructor.attach(athlete)

    def remove_athlete(self, athlete: Athlete):
        try:
            self.athletes.remove(athlete)
            self.instructor.detach(athlete)
        except Exception as e:
            logger.error(f"Can't remove athlete: {e}")

    def run(self):
        print()
        print(f"{40*'-'}{self.name}{40*'-'}")
        print()
        for _, program in self.training_programs.items():
            logger.info(program)
        print()
        print(f"{40*'-'}{len(self.name)*'-'}{40*'-'}")

        for _, mode in self.training_modes.items():
            self.instructor.set_training_mode(mode)
