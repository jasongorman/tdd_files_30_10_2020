from functools import reduce

from dataclasses import replace, dataclass

clockwise = ['N', 'E', 'S', 'W']
vectors = [[0, 1], [1, 0], [0, -1], [-1, 0]]


@dataclass(frozen=True)
class Rover(object):
    position: (int, int)
    facing: str

    def go(self, instructions):
        return reduce(lambda rover, instruction: rover._do_command(instruction), instructions, self)

    def _do_command(self, instruction):
        return {
            "R": lambda: self._right(),
            "L": lambda: self._left(),
            "F": lambda: self._forward(),
            "B": lambda: self._back()
        }[instruction]()

    def _left(self):
        anti_clockwise = clockwise.copy()
        anti_clockwise.reverse()
        return self._turn(anti_clockwise)

    def _right(self):
        return self._turn(clockwise)

    def _turn(self, compass):
        current = compass.index(self.facing)
        return replace(self, facing=compass[(current + 1) % 4])

    def _back(self):
        vector = vectors[(clockwise.index(self.facing) + 2) % 4]
        return self._move(vector)

    def _forward(self):
        vector = vectors[clockwise.index(self.facing)]
        return self._move(vector)

    def _move(self, vector):
        return replace(self, position=(self.position[0] + vector[0], self.position[1] + vector[1]))
