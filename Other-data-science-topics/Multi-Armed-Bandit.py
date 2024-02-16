#CODE BASED ON:
#######################################################################
# Copyright (C)                                                       #
# 2016-2018 Shangtong Zhang(zhangshangtong.cpp@gmail.com)             #
# 2016 Tian Jun(tianjun.cpp@gmail.com)                                #
# 2016 Artem Oboturov(oboturov@gmail.com)                             #
# 2016 Kenta Shimada(hyperkentakun@gmail.com)                         #
# Permission given to modify the code as long as you keep this        #
# declaration at the top                                              #
#######################################################################
#WITH SOME CHANGES AND SIMPLIFICATIONS.

import matplotlib.pyplot as plt
import numpy as np
from tqdm import trange

# Multi-Armed-Bandit class
class MAB:
    def __init__(self, k_arm=10, epsilon=0., initial=0., step_size=0.1, true_reward=0.):
        # number of arms
        self.k = k_arm
        # probability of randomly choosing an action
        self.epsilon = epsilon
        # initial value estimated for each action
        self.initial = initial
        # step size in the process of estimation
        self.step_size = step_size
        # true reward increment to be added to q_true
        self.true_reward = true_reward
        # initial time/step in the process of estimation
        self.time = 0
        # array of indices for k arms to be used in the random choice with probability epsilon
        self.indices = np.arange(self.k)

    # Function to reset variables to standard values
    def reset(self):
        # true reward values for k arms representing q*(a) (inititalization)
        self.q_true = np.random.randn(self.k) + self.true_reward
        # Q(a) estimation (inititalization)
        self.q_estimation = np.zeros(self.k) + self.initial
        # inititalization of an action counter
        self.action_count = np.zeros(self.k)
        # best true action selected from q*(a)
        self.best_action = np.argmax(self.q_true)
        # inititalization of steps counter
        self.time = 0

    # Function representing a single action taken
    def act(self):
        # condition to randomly pick a k arm with probability epsilon
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.indices)
        # take the best (maximum) value among Q values
        q_best = np.max(self.q_estimation)
        # return the index of Q values that corresponds to q_best
        return np.random.choice(np.where(self.q_estimation == q_best)[0])
    
    # Function representing a step
    def step(self, action):
        # reward Rn based on a action over the true q*(a) with addition to some randomness
        reward = np.random.randn() + self.q_true[action]
        # reward = self.q_true[action]
        # increasing the time counter with 1
        self.time += 1
        # increasing the list of action count with 1
        self.action_count[action] += 1
        # Q(n+1) in the incremental implementation: Q(n+1) = Qn + 1/n(Rn - Qn), or Q(n+1) = Qn + step_size(Rn - Qn), with step_size being alpha
        self.q_estimation[action] += self.step_size * (reward - self.q_estimation[action])
        # return the reward Rn
        return reward


if __name__ == '__main__':
    #SIMULATION
        
    # number of runs: for each run we have a different q_true (q*(a)) with k arms, and consequently an improvement of the estimate of the action with maximum reward
    # at the end we average the reward of each step along the number of runs
    runs = 2000
    # number of time steps of the simulation
    time = 1000
    # non greedy paramenter epsilon
    eps = 0.1
    # creating an instance of the MAB class
    bandit = MAB(epsilon=eps)

    # initiate a null matrix of rewards
    rewards = np.zeros((time, runs))
    # initiate a null matrix of action counts
    best_action_counts = np.zeros(rewards.shape)

    # loop over the runs
    for r in trange(runs):
        # reset the instance variables
        bandit.reset()
        # loop over the time steps
        for t in range(time):
            # generate an action
            action = bandit.act()
            # get a reward from an action
            reward = bandit.step(action)
            # fill the matrix of rewards
            rewards[t,r] = reward
            # if the action corresponds to the best one, fill the action counts matrix
            if action == bandit.best_action:
                best_action_counts[t,r] = 1

    # average of action counts over runs for each step (i.e. average of step 1 for all runs)
    mean_best_action_counts = best_action_counts.mean(axis=1)
    # average of rewards over runs for each step
    mean_rewards = rewards.mean(axis=1)

    #plot mean rewards as a function of steps
    plt.plot(mean_rewards, label=r'Average Rewards')
    # plt.plot(mean_best_action_counts, label=r'% Best actions')
    plt.xlabel('Steps')
    plt.ylabel('Average Reward')
    plt.legend()
    plt.show()