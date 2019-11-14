from abc import abstractmethod

from ga_abstract import GAAbstract
from population import Population
from individual import Individual
import numpy as np


class GAEngine(GAAbstract):
    def __init__(self, length=5):
        self._target = Individual(length, list(np.ones((length, ), dtype=int)))
        self._population = Population(self.target, 10)

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, target):
        self._target = target

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, population):
        self._population = population

    def selection(self):
        return self.population.get_n_best_individual(1)

    def mutation(self, individual):
        mutation_index = np.random.randint(0, len(self.target.get_value()))
        value = individual.get_value()
        value[mutation_index] = (int) (not value[mutation_index])
        individual.set_value(value)
        return individual

    def cross_over(self, individual1, individual2):
        pass

    def run(self):
        count = 0
        while True:
            # selection
            best_individual, best_score = self.selection()
            # print("best:", best_individual.get_value(), best_score)
            # mutate
            mutant = self.mutation(best_individual)
            mutant_score = self.population.calc_fitness_score(self.target, mutant)
            # print("mutant:", mutant.get_value(), mutant_score)
            if mutant_score > best_score:
                self.population.add_individual(mutant, mutant_score)
                print("new individual added")

            if mutant_score == len(self.target.get_value()):
                break
            count = count + 1
        print("Best individual is {} and target is {}; generations = {}".format(mutant.get_value(),
                                                                                self.target.get_value(), count))

    def should_exit(self):
        pass






