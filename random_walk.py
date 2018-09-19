from random import choice

class RandomWalk():
    #class to generate random walks
    def __init__(self, num_points = 5000):
        #initialize attributes of walk
        self.num_points = num_points

        #start walk at origin
        self.x_val = [0]
        self.y_val = [0]

    def fill_walk(self):
        #calculate points in the walk
        #keep taking steps until walk reaches desired length
        while len(self.x_val) < self.num_points:
            #decide direction to go
            x_dir = choice([1,-1])
            x_dist = choice([0,1,2,3,4,5,6,7,8])
            x_step = x_dir * x_dist

            y_dir = choice([1,-1])
            y_dist = choice([0,1,2,3,4,5,6,7,8])
            y_step = y_dir * y_dist

            #reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            #calc next x and y vals
            next_x = self.x_val[-1] + x_step
            next_y = self.y_val[-1] + y_step

            self.x_val.append(next_x)
            self.y_val.append(next_y)
