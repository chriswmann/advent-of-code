import os
import sys
from pathlib import Path

# directory reach
current_file = Path(__file__)

# setting path
sys.path.append(current_file.parent.absolute())

from aoc_2021 import (
    DayOne2021,
)

if __name__ == '__main__':


    DayOne2021(year=2021, day=1)
