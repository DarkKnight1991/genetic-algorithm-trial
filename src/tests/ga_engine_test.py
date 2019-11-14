import unittest
from src.population import Population
from src.individual import Individual


class PopulationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.target = Individual(5, [1, 1, 1, 1, 1])
        self.individual1 = Individual(5, [0, 0, 0, 0, 0])
        self.individual2 = Individual(5, [1, 0, 1, 0, 0])
        self.individual3 = Individual(5, [0, 1, 0, 1, 1])
        self.individual4 = Individual(5, [1, 1, 1, 1, 1])
        self.population = Population(self.target, 4, [self.individual1, self.individual2, self.individual3,
                                                      self.individual4])
        self.population.calc_fitness_scores()



    def tearDown(self) -> None:
        pass