# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
import numpy as np
from RRT.src.rrt.rrt import RRT
from RRT.src.search_space.search_space import SearchSpace
from RRT.src.utilities.plotting import Plot
from Constant import *


def RRT_arm(obstacles, goalxy, thetas):
    X_dimensions = np.array([(0, EnviromBoundx), (0, EnviromBoundy)])  # dimensions of Search Space
    # obstacles
    Obstacles = np.array([(ob[0], 0, ob[1], ob[2]) for ob in obstacles])
    # Obstacles = np.array([(20, 20, 40, 40), (20, 60, 40, 80), (60, 20, 80, 40), (60, 60, 80, 80)])

    x_init = (initialx, initialy)  # starting location
    x_goal = (goalxy[0], goalxy[1])  # goal location
    if x_goal[0] > EnviromBoundx or x_goal[1] > EnviromBoundy:
        return False
    # print(x_goal)

    Q = np.array([(1, 1)])  # length of tree edges
    r = l1/10  # length of smallest edge to check for intersection with obstacles
    max_samples = 1024  # max number of samples to take before timing out
    prc = 0.1  # probability of checking for a connection to goal

    # create search space
    X = SearchSpace(X_dimensions, Obstacles)

    # create rrt_search
    rrt = RRT(X, Q, x_init, x_goal, max_samples, r, prc)
    path = rrt.rrt_search()

    # print(path)

    thetas_c = thetas.copy()
    print(thetas_c)
    for point in path:
        print(point)



    # plot
    # plot = Plot("rrt_2d")
    # plot.plot_tree(X, rrt.trees)
    # if path is not None:
    #     plot.plot_path(X, path)
    # plot.plot_obstacles(X, Obstacles)
    # plot.plot_start(X, x_init)
    # plot.plot_goal(X, x_goal)
    # plot.draw(auto_open=True)
