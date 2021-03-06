import os
import sys
from pathlib import Path

from aoc_2021 import DayOne2021, DayTwo2021

# directory reach
current_file = Path(__file__)

# setting path
sys.path.append(current_file.parent.absolute())

from aoc_2021 import (
    DayOne2021,
    DayTwo2021,
    DayThree2021,
)

if __name__ == "__main__":

    print("Day 1, 2021")
    DayOne2021(year=2021, day=1)
    print("Day 2, 2021")
    DayTwo2021(year=2021, day=2)
    print("Day 3, 2021")
    DayThree2021(year=2021, day=3)
