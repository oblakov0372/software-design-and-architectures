from abc import ABC, abstractmethod
from training_program import TrainingProgram
from utils.logger import logger


class Observer(ABC):
    @abstractmethod
    def update(self, message: str, mode_id: str):
        pass


class Athlete(Observer):
    def __init__(self, name: str, training_program: TrainingProgram) -> None:
        super().__init__()
        self.name = f"<Athlete> | {name}"
        self.training_program = training_program

    def update(self, message: str, mode_id: str):
        if mode_id in self.training_program.get_id():
            logger.info(f"{self.name} | Receive message: {message}")
