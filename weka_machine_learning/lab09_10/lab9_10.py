# -*- coding: utf-8 -*-
# Lab 9-10: Online Learning
# Author: Dylan Rapanan, Danial Saber, Winter 2024

# NOTE: You may use any Python library you want to complete this lab. 

# NOTE: You may add as many additional helper functions as you like.

# NOTE: Imagine the following repeated game:
# In each round t = 1, . . . , T
# • An adversary choose a real number in yt ∈ [0, 1] and he keeps it secret;
# • You try to guess the real number, choosing xt ∈ [0, 1];
# • The adversary’s number is revealed and you pay the squared difference (xt − yt)^2.
# • Your goal is to implement a strategy that minimizes the total loss over T rounds.
# • You should see a plot where the regret line looks like a logarithmic curve.

import numpy as np
import matplotlib.pyplot as plt

# This is the adversary's strategy, do not modify this function
def adversary_strategy(prev_user_choices):
    # be mean and choose as far away from the user's choice as possible
    if len(prev_user_choices) == 0:
        return np.random.normal(0.25, 1)
    if prev_user_choices[-1] < 0.5:
        y = np.random.normal(0.75, 0.1)
    else:
        y = np.random.normal(0.25, 0.1)
    return y

# Implement your strategy here, make sure to return a number in [0, 1]
# Parameters:
# prev_adversary_choices: A list of the adversary's choices in the previous rounds
# t: The current round number
# Returns: A number in [0, 1]
# Feel free to modify the function parameters if needed
def user_strategy(prev_adversary_choices, t):
            
    # TODO: Implement a strategy to minimize the loss over T rounds
    if(t == 1):
        x = 0.5
    else:
        x = sum(prev_adversary_choices)/len(prev_adversary_choices)
    return x

# This function calculates the regret, do not modify this function
def regret(prev_adversary_choices, prev_user_choices):
    sum_loss = 0
    sum_u_loss = 0
    for t in range(1, len(prev_adversary_choices)):
        sum_loss += (prev_user_choices[t] - prev_adversary_choices[t])**2
        sum_u_loss += (0.5 - prev_adversary_choices[t])**2

    return sum_loss - sum_u_loss

# Leave this main method as is, this will allow you to see the performance of your strategy
if __name__ == "__main__":
    T = 2000 # The number of rounds, leave this as is
    prev_adversary_choices = [] # A list of the adversary's choices in the previous rounds
    prev_user_choices = [] # A list of your choices in the previous rounds
    regret_values = [] # A list of the regret values for each round

    for t in range(1, T):
        # Your number from your strategy
        x = user_strategy(prev_adversary_choices, t)
        prev_user_choices.append(x)

        # Adversary's number from their strategy
        y = adversary_strategy(prev_user_choices)
        prev_adversary_choices.append(y)

        # Calculate the regret
        if len(prev_adversary_choices) != 0:
            regret_values.append(regret(prev_adversary_choices, prev_user_choices))

    # calculate similarity between regret and log curve
    log_curve = np.log(np.arange(1, T))
    similarity = np.corrcoef(regret_values, log_curve)[0, 1]

    # plot the regret curve, it should look like a logarithmic curve if your strategy is learning
    plt.plot(regret_values)
    plt.title('Regret Curve')
    plt.xlabel('Rounds')
    plt.ylabel('Regret')

    # include text for similarity
    plt.text(100, 0, f"Similarity between regret and log curve: {similarity:.2f}", fontsize=12)
    plt.show()