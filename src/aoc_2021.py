import math

from collections import defaultdict, deque
from typing import Any, List, Tuple, Union
from utils import decimal_from_list

from utils import AbstractSolutionClass

from aocd import get_data


class DayOne2021(AbstractSolutionClass):
    def prep_data(self) -> None:
        """Just need to split the text data on whitespace and cast to int for this one."""

        self.depths: List[int] = [int(d) for d in self.data.split()]

    def get_part_one(self) -> None:
        """count the number of times a depth measurement increases from the
        previous measurement.  (There is no measurement before the first measurement.)
        """

        n_increases: int = 0
        for old_depth, new_depth in zip(self.depths, self.depths[1:]):
            if new_depth > old_depth:
                n_increases += 1

        self.solutions.part_one = n_increases

    def get_part_two(self) -> None:
        """Considering every single measurement isn't as useful as you expected:
        there's just too much noise in the data.
        Instead, consider sums of a three-measurement sliding window.
        """

        window_size = 3
        window: deque = deque(self.depths, maxlen=window_size)
        n_increases: int = 0
        old_window_sum: float = math.inf
        for depth in self.depths:
            window.append(depth)
            if len(window) >= window_size and sum(window) > old_window_sum:
                n_increases += 1
            old_window_sum = sum(window)

        self.solutions.part_two = n_increases


class DayTwo2021(AbstractSolutionClass):
    def prep_data(self) -> None:
        """Split each instruction into a direction and a distance."""

        self.instructions: List[Tuple[str, int]] = []
        for item in self.data.split("\n"):
            direction, distance = item.split()
            self.instructions.append((direction, int(distance)))

    def get_part_one(self) -> None:
        """count the number of times a depth measurement increases from the
        previous measurement.  (There is no measurement before the first measurement.)
        """

        forward: int = 0
        depth: int = 0
        for direction, distance in self.instructions:
            match direction:
                case "forward":
                    forward += distance
                case "up":
                    depth -= distance
                case "down":
                    depth += distance

        self.solutions.part_one = forward * depth

    def get_part_two(self) -> None:
        """Based on your calculations, the planned course doesn't seem to make any
        sense. You find the submarine manual and discover that the process is actually
        slightly more complicated.

        In addition to horizontal position and depth, you'll also need to track a third
        value, aim, which also starts at 0. The commands also mean something entirely
        different than you first thought:

          - down X increases your aim by X units.
          - up X decreases your aim by X units.
          - forward X does two things:
            - It increases your horizontal position by X units.
            - It increases your depth by your aim multiplied by X.

        Again note that since you're on a submarine, down and up do the opposite of
        what you might expect: "down" means aiming in the positive direction.

        Calculate the horizontal position and depth you would have after following the
        planned course. What do you get if you multiply your final horizontal position
        by your final depth?
        """

        forward: int = 0
        depth: int = 0
        aim: int = 0
        for direction, distance in self.instructions:
            match direction:
                case "forward":
                    forward += distance
                    depth += aim * distance
                case "up":
                    aim -= distance
                case "down":
                    aim += distance

        self.solutions.part_two = forward * depth


class DayThree2021(AbstractSolutionClass):
    def prep_data(self) -> None:
        """Transform input to list the digits by column instead of row."""
        self.diagnostics: List[str] = [row for row in self.data.split("\n")]
        self.n_columns: int = len(self.diagnostics[0])
        self.n_rows: int = len(self.diagnostics)
        self.columnar: defaultdict[int, int] = defaultdict(list)
        for _, row in enumerate(self.diagnostics):
            for col_ind, digit in enumerate(row):
                self.columnar[col_ind].append(int(digit))

    def get_part_one(self) -> None:
        """Find the most common bit in the corresponding position of all numbers in
        the diagnostic report.

        If the most common digit is 1, the gamma value for that column is 1.
        Epsilon is the boolean not of gamma.

        Convert the binary numbers gamma and epsilon to decimal.

        The answer is the product of the decimal values for gamma and epsilon.
        """
        self.gamma = []
        for _, vector in self.columnar.items():
            if vector.count(1) > vector.count(0):
                self.gamma.append(1)
            else:
                self.gamma.append(0)

        self.epsilon = [1 - g for g in self.gamma]

        self.solutions.part_one = decimal_from_list(self.gamma) * decimal_from_list(
            self.epsilon
        )
