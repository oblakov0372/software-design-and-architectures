from abc import ABC, abstractmethod


class TrainingMode(ABC):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def get_id(self):
        pass


class BasicTrainingMode(TrainingMode):
    def get_title(self):
        return "Basic Training"

    def get_id(self):
        return "basic"


class CardioTrainingMode(TrainingMode):
    def get_title(self):
        return "Cardio Training"

    def get_id(self):
        return "cardio"


class StrengthTrainingMode(TrainingMode):
    def get_title(self):
        return "Strength Training"

    def get_id(self):
        return "strength"
