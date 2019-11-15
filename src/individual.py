#
# Copyright (c) 2019. Asutosh Nayak (nayak.asutosh@ymail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#

import numpy as np


class Individual:
    def __init__(self, size, value=None):
        if not value:
            self._value = list(np.random.randint(0, 2, size))
        else:
            if size != len(value):
                raise Exception("size parameter {} is different from length of individual {}".format(size, len(value)))
            self._value = value
        self.fitness_score = 0.0

    def set_fitness_score(self, score):
        self.fitness_score = score

    def get_fitness_score(self):
        return self.fitness_score

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value
