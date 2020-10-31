import unittest

from parameterized import parameterized


class Rover(object):
    def __init__(self, facing):
        self.facing = facing

    def right(self):
        compass = ["N", "E", "S", "W"]
        current = compass.index(self.facing)
        self.facing = compass[(current + 1) % 4]


class RoverTests(unittest.TestCase):

    @parameterized.expand([
        ("N", "E"),
        ("E", "S"),
        ("S", "W"),
        ("W", "N")
    ])
    def test_turns_right_clockwise(self, startsFacing, endsFacing):
        rover = Rover(startsFacing)
        rover.right()
        self.assertEqual(rover.facing, endsFacing)


if __name__ == '__main__':
    unittest.main()
