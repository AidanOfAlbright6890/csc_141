from random import choice
class RandomWalk:
    """A class to generate random walks."""
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]
        

    def get_step(self):
        """Calculate all the points in the walk."""
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            # Decide which direction to go, and how far to go.
            x_step = choice([1, -1])
            x_step = choice([8, 8, 8, 8, 8])
            x_step = x_step * x_step
            y_step = choice([1, -1])
            y_step = choice([8, 8, 8, 8, 8])
            y_step = y_step * y_step
            x_step = self.get_step()
            y_step = self.get_step()
            