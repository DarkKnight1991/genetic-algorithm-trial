from ga_engine import GAEngine
import numpy as np


mutation_only_iterations = []
full_ga_iterations = []

for i in range(1000):
    mutation_only_iterations.append(GAEngine(10).run(True))
    full_ga_iterations.append(GAEngine(10).run())

print("Average generations taken to reach target: mutations_only = {} and full_ga = {}".format(
    np.mean(mutation_only_iterations), np.mean(full_ga_iterations)))
