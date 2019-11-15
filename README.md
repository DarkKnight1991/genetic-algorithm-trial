# genetic-algorithm-trial
Project to try out genetic algorithm first hand. Solves a simple problem of finding the target list starting from random lists.

Genetic algorithm has always facsinated me. It's logically clean and simple, and easy to understand. Yet people claim it works! I wanted to see how well it works. I am using GA here for simple task of reaching a target list from a set of random lists. One approach uses only "mutation" (which is nothing but random change on best individual and hoping for an improvement), second approach uses both mutation and cross-over of best parents to reach the target.

"main.py" solves this problem in a loop for 1000 times. The use of crossover gives significantly faster result (meaning it takes much lesser generations). I ran the program multiple times and each time I received almost similar results:

* Average generations taken to reach target: mutations_only = 1116.809 and full_ga = 276.959

* Average generations taken to reach target: mutations_only = 1172.752 and full_ga = 286.36

* Average generations taken to reach target: mutations_only = 1140.045 and full_ga = 273.27

The purpose of starting with this simple project is to get a good grasp on implementation of Genetic Algorithm so that I can use it to solve real world problems like finding better architecture for Neural Networks! That would be my next project.
