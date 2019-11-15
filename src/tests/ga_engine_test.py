#
# Copyright (c) 2019. Asutosh Nayak (nayak.asutosh@ymail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#

import unittest
from src.population import Population
from src.individual import Individual
from src.ga_engine import GAEngine


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
        self.ga_engine = GAEngine(5, 4)

    def test_cross_over(self):
        individual = self.ga_engine.cross_over(self.individual1, self.individual2, [2, 5], [0, 3])
        self.assertEqual(individual.get_value(), [0, 0, 1, 0, 1])

        individual = self.ga_engine.cross_over(self.individual2, self.individual3, [1, 4], [2, 5])
        self.assertEqual(individual.get_value(), [1, 0, 1, 1, 0])

        individual = self.ga_engine.cross_over(self.individual4, self.individual3, [1, 2], [2, 3])
        self.assertEqual(individual.get_value(), [1, 0, 1, 1, 1])

        individual = self.ga_engine.cross_over(self.individual3, self.individual1, [0, 5], [0, 5])
        self.assertEqual(individual.get_value(), [0, 0, 1, 0, 1])  # self.individual1 has changed above

    def tearDown(self) -> None:
        pass