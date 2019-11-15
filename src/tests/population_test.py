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


class PopulationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.target = Individual(5, [1, 1, 1, 1, 1])
        self.individual1 = Individual(5, [0, 0, 0, 0, 0])
        self.individual2 = Individual(5, [1, 0, 1, 0, 0])
        self.individual3 = Individual(5, [0, 1, 0, 1, 1])
        self.individual4 = Individual(5, [1, 1, 1, 1, 1])

        self.population = Population(self.target, 4, [self.individual1, self.individual2, self.individual3,
                                                      self.individual4])

    def test_calc_fitness_score(self):
        self.population.calc_fitness_scores()
        self.assertTrue(self.population.calc_fitness_score(self.target, self.individual1) == 0, "ind 1 score wrong")
        self.assertTrue(self.population.calc_fitness_score(self.target, self.individual3) == 3, "ind 3 score wrong")
        self.assertTrue(self.population.calc_fitness_score(self.target, self.individual4) == 5, "ind 4 score wrong")

    def test_calc_fitness_scores(self):
        self.assertEqual(self.population.fitness_scores, [0, 2, 3, 5], "fitness scores list wrong")

    def test_get_n_best_individual(self):
        self.assertEqual(self.population.get_n_best_individual(1), (self.individual4, 5), "best ind returned wrong")
        self.assertEqual(self.population.get_n_best_individual(3), (self.individual2, 2), "3rd best ind returned wrong")

    def test_add_individual(self):
        temp_individual = Individual(5, [1, 0, 0, 0, 0])
        self.population.add_individual(temp_individual)
        self.assertEqual(self.population.individuals, [temp_individual, self.individual2, self.individual3,
                                                       self.individual4], "post addition scores wrong")
        self.assertEqual(self.population.fitness_scores, [1, 2, 3, 5], "post addition scores wrong")

        temp_individual = Individual(5, [1, 0, 1, 1, 1])
        self.population.add_individual(temp_individual)
        self.assertEqual(self.population.individuals, [temp_individual, self.individual2, self.individual3,
                                                       self.individual4], "post addition scores wrong")
        self.assertEqual(self.population.fitness_scores, [4, 2, 3, 5], "post addition scores wrong")

    def tearDown(self) -> None:
        pass