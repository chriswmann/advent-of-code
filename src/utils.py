from abc import ABC, abstractmethod
from typing import Callable, List

from aocd import get_data


class SolutionCollection:
    """Utility class to store and print solutions.

    Used with AbstractSolutionClass.
    """

    def __repr__(self):

        solutions: List[str] = [f"{k}: {v}" for k, v in self.__dict__.items()]
        return "\n".join(solutions)


class AbstractSolutionClass(ABC):
    def __init__(self, year, day) -> None:

        self.data: str = get_data(year=year, day=day)

        self.solutions: SolutionCollection = SolutionCollection()
        self.prep_data()
        self.get_solutions()

    @abstractmethod
    def prep_data(self) -> None:
        """Prepare the raw data for processing."""

        raise NotImplementedError("This is the abstract method.")

    def get_solutions(self) -> None:
        """Call the methods for each part.

        Requires any solutions to be computed in methods that have names starting with
        `get_part_`.

        Each `get_part` method needs to save its result to `self.solutions`.
        """

        for method_name in dir(self):
            if method_name.startswith("get_part_"):
                method: Callable = getattr(self, method_name)
                method()

        print(self.solutions)


def decimal_from_list(binary):
    """Convert a list of 0s and 1s to a decimal number.

    Args:
        binary (list[int]): List of 0s and 1s.

    Returns:
        int: Input as a decimal number.
    """

    return sum(val * (2**idx) for idx, val in enumerate(reversed(binary)))
