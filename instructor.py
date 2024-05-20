from athlete import Athlete, Observer
from training_mode import TrainingMode
from utils.logger import logger


class Instructor:
    def __init__(self, name: str):
        self._observers: list[Observer] = []
        self.name = f"<Instructor> | {name}"
        self.training_mode = None

    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, message: str):
        print()
        logger.debug(f"{self.name} | {message}")
        print()
        for observer in self._observers:
            observer.update(message, self.training_mode.get_id())

    def set_training_mode(self, training_mode: TrainingMode):
        self.training_mode = training_mode
        message = f"Training mode was changed to {self.training_mode.get_title()}"
        self.notify(message=message)
