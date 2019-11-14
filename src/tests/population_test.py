import unittest
from population import Population
from individual import Individual


class PopulationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.target = Individual(5, [1, 1, 1, 1, 1])
        self.individual1 = Individual(5, [0, 0, 0, 0, 0])
        self.individual2 = Individual(5, [1, 0, 1, 0, 0])
        self.individual3 = Individual(5, [0, 1, 0, 1, 1])
        self.individual4 = Individual(5, [1, 1, 1, 1, 1])

        self.population = Population(target, 4, [self.individual1, self.individual2, self.individual3, self.individual4])

    def test_calc_fitness_score(self):
        self.assertTrue(self.population.calc_fitness_score(self.target, self.individual1) == 0, "tc 1 passed")
        self.assertTrue(self.population.calc_fitness_score(self.target, self.individual3) == 3, "tc 2 passed")
        self.assertTrue(self.population.calc_fitness_score(self.target, self.individual4) == 5, "tc 3 passed")

    def tearDown(self) -> None:
        pass