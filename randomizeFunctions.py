from random import randrange
from math import cos, sin, pi


def get_random_pos(pos, corner_pos):
    """
    :param pos: (x,y) position
    :param corner_pos: (x,y) corner position
    :return: pose with tolerance as new pos
    use randomized position between pos and corner_pos
    """
    x, y = pos
    corner_x, corner_y = corner_pos
    radius = int(pow((x - corner_x) ** 2 + (y - corner_y) ** 2, 1 / 2))
    random_r = randrange(start=-radius, stop=radius)
    random_radian = randrange(start=-0, stop=int(200 * pi)) / 10
    new_x, new_y = int(random_r * cos(random_radian)), int(random_r * sin(random_radian))
    new_pos = (x + new_x, y + new_y)
    return new_pos
