import numpy as np


class Individual:
    def __init__(self, size, value=None):
        if not value:
            self.value = list(np.random.randint(0, 2, size))
        else:
            self.value = value
        self.fitness_score = 0.0

    def set_fitness_score(self, score):
        self.fitness_score = score

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
