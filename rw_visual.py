import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    #make a random walk and plot
    rw = RandomWalk(15000)
    rw.fill_walk()
    plt.figure(dpi=128,figsize=(10,6))

    point_nums = list(range(rw.num_points)) #list of numbers equal to num of points in walk
    plt.scatter(rw.x_val, rw.y_val, c = point_nums, cmap=plt.cm.Blues, edgecolor = 'none', s= 1)

    #emphasize first and last points
    plt.scatter(0,0, c='green', edgecolors = 'none', s=100)
    plt.scatter(rw.x_val[-1], rw.y_val[-1], c = 'red', edgecolors = 'none', s = 100)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
