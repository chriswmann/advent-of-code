from ast import Call
import math

from collections import deque
from typing import List

from utils import AbstractSolutionClass

from aocd import get_data

class DayOne2021(AbstractSolutionClass):


    def prep_data(self) -> None:
        """Just need to split the text data on whitespace and cast to int for this one.
        """

        self.depths: List[int] = [int(d) for d in self.data.split()]

    def get_part_one(self) -> None:
        """count the number of times a depth measurement increases from the
        previous measurement.  (There is no measurement before the first measurement.)
        """

        n_increases: int = 0

        old_depth: float = math.inf
        for depth in self.depths:
            if depth > old_depth:
                n_increases += 1
            old_depth = depth

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
