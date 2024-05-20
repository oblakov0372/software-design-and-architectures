from abc import ABC, abstractmethod


class TrainingProgram(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_id(self):
        pass

    def __str__(self):
        return f"{self.get_description()}: {self.get_cost()} BGN"


class BasicTrainingProgram(TrainingProgram):
    def get_description(self):
        return "Basic training program"

    def get_cost(self):
        return 20

    def get_id(self):
        return "basic"


class TrainingProgramDecorator(TrainingProgram):
    def __init__(self, decorated_program: TrainingProgram) -> None:
        self._decorated_program = decorated_program

    def get_description(self):
        return self._decorated_program.get_description()

    def get_cost(self):
        return self._decorated_program.get_cost()

    def get_id(self):
        return self._decorated_program.get_id()


class CardioDecorator(TrainingProgramDecorator):
    def get_description(self):
        return f"{self._decorated_program.get_description()} + Cardio exercises"

    def get_cost(self):
        return self._decorated_program.get_cost() + 10

    def get_id(self):
        return f"{self._decorated_program.get_id()}_cardio"


class StrengthTrainingDecorator(TrainingProgramDecorator):
    def get_description(self):
        return f"{self._decorated_program.get_description()} + Strength Training"

    def get_cost(self):
        return self._decorated_program.get_cost() + 20

    def get_id(self):
        return f"{self._decorated_program.get_id()}_strength"
