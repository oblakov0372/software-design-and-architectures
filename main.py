from gym import Gym
from athlete import Athlete
from training_program import (
    BasicTrainingProgram,
    CardioDecorator,
    StrengthTrainingDecorator,
)


if __name__ == "__main__":
    gym = Gym("Best Gym")

    athlete1 = Athlete("Athlete1", BasicTrainingProgram())
    athlete2 = Athlete("Athlete2", CardioDecorator(BasicTrainingProgram()))
    athlete3 = Athlete("Athlete3", StrengthTrainingDecorator(BasicTrainingProgram()))
    athlete4 = Athlete(
        "Athlete4", CardioDecorator(StrengthTrainingDecorator(BasicTrainingProgram()))
    )

    gym.add_athlete(athlete1)
    gym.add_athlete(athlete2)
    gym.add_athlete(athlete3)
    gym.add_athlete(athlete4)

    gym.run()
