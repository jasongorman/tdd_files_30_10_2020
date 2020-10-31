import unittest

from parameterized import parameterized

from mars_rover import Rover


class MarsRoverTest(unittest.TestCase):
    @parameterized.expand([
        ('N', 'E'),
        ('E', 'S'),
        ('S', 'W'),
        ('W', 'N')
    ])
    def test_turns_right_clockwise(self, starts_facing, ends_facing):
        rover = Rover((0, 0), starts_facing)
        rover = rover.go('R')
        self.assertEqual(ends_facing, rover.facing)

    @parameterized.expand([
        ('N', 'W'),
        ('W', 'S'),
        ('S', 'E'),
        ('E', 'N')
    ])
    def test_turns_left_anticlockwise(self, starts_facing, ends_facing):
        rover = Rover((0, 0), starts_facing)
        rover = rover.go('L')
        self.assertEqual(ends_facing, rover.facing)

    @parameterized.expand([
        ('N', (5, 6)),
        ('E', (6, 5)),
        ('S', (5, 4)),
        ('W', (4, 5))
    ])
    def test_moves_forward_in_direction_facing(self, facing, end_position):
        rover = Rover((5, 5), facing)
        rover = rover.go('F')
        self.assertEqual(end_position, rover.position)

    @parameterized.expand([
        ('N', (5, 4)),
        ('E', (4, 5)),
        ('S', (5, 6)),
        ('W', (6, 5))
    ])
    def test_moves_back_in_opposite_direction_facing(self, facing, end_position):
        rover = Rover((5, 5), facing)
        rover = rover.go('B')
        self.assertEqual(end_position, rover.position)

    def test_executes_sequence_of_instructions(self):
        rover = Rover((5, 5), 'N')
        rover = rover.go('RF')
        self.assertEqual('E', rover.facing)
        self.assertEqual((6, 5), rover.position)


if __name__ == '__main__':
    unittest.main()
