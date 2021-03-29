import copy
import random
from collections import Counter

# Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. 
# What is the probability that a random draw of 4 balls will contain at least 1 
# red ball and 2 green balls? While it would be possible to calculate the probability 
# using advanced mathematics, an easier way is to write a program to perform a 
# large number of experiments to estimate an approximate probability.

# The class should take a variable number of arguments that specify the number of
# balls of each color that are in the hat.
class Hat:
    def __init__(self, **kwargs):
        contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                contents += key.split()
        self.contents = contents

    # method that accepts an argument indicating the number of balls to draw from the
    # hat. This method should remove balls at random from `contents` and return those
    #  balls as a list of strings. 
    def draw(self, draw_numbers):
        draw_list = []
        contents = self.contents
        if draw_numbers >= len(contents):
            return contents
        for _ in range(draw_numbers):
            choice = random.choice(contents)
            contents.remove(choice)
            draw_list.append(choice)
        self.contents = contents
        return draw_list

# Function `experiment`, should accept the following arguments:
# * `hat`: A hat object containing balls that should be copied inside the function.
# * `expected_balls`: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. 
# * `num_balls_drawn`: The number of balls to draw out of the hat in each experiment.
# * `num_experiments`: The number of experiments to perform. 
# The `experiment` function should return a probability. 
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_list = []

    for key, value in expected_balls.items():
        for _ in range(value):
            expected_list += key.split()
    m = 0

    for _ in range(num_experiments):
        trial = copy.deepcopy(hat)
        draw = trial.draw(num_balls_drawn)
        result = list((Counter(expected_list) - Counter(draw)).elements())
        if not result:
            m += 1
    probability = m / num_experiments
    return probability



