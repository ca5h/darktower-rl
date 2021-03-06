BLOCK_WALK = 1
BLOCK_LOS = 2
NONE = 4

ft_types = {
    "wall": 1,
    "floor": 0
}

class DungeonFeature(object):
    def __init__(self, char, color, dim_color, type=ft_types["wall"], flags=NONE):
        self.char = char
        self.color = color
        self.flags = flags
        self.dim_color = dim_color
        self.type = type
        self.seen = False
        self.color_back = [30, 30, 30]
        self.dim_color_back = [5, 5, 5]

    def is_wall(self):
        return self.type == ft_types["wall"]

    def is_floor(self):
        return self.type == ft_types["floor"]

    def passable(self):
        return not self.flags & BLOCK_WALK


def FT_FIXED_WALL(): return DungeonFeature('#', [130, 110, 50], [0, 0, 100], flags=BLOCK_LOS | BLOCK_WALK)


def FT_ROCK_WALL(): return DungeonFeature("#", [130, 110, 50], [0, 0, 100], flags=BLOCK_LOS | BLOCK_WALK)


def FT_GLASS_WALL(): return DungeonFeature("#", [30, 30, 160], [0, 0, 100], flags=BLOCK_WALK)


def FT_FLOOR(): return DungeonFeature(".", [255, 255, 255], [60, 60, 60], ft_types["floor"])