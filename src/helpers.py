import sympy as sp
from sympy.abc import t
from typing import Any


def clean_equation(eq: str):
    """
    Return a sympified equation.

    Given a string turn it into a equation that is usable by sympy.

    Args:
        eq (str): the equation to be sympified

    Returns:
        Any: a sympify equation
    """

    # DOC: if not passed an equation then take an input
    if eq == "":
        eq = input("Enter an equation: ")

    try:
        return sp.sympify(eq)
    except ValueError:  # DOC: if a ValuError occurs then the equation is not formatted correctly
        print("Incorrect syntax!")
        print(
            "Enter one side of the equation (set everything equal to 0) using x and y (eg: x**2 - y == x**2 = y)"
        )
        new_eq: str = input("Enter the equation with correct syntax: ")
        return clean_equation(
            new_eq
        )  # DOC: take a new input and call again recursively


# DOC: define a 2-d point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # DOC: __repr__ needed in order to print to console (equivalent to the toString override method in java)
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    # DOC: __eq__ is used for checking equality
    def __eq__(self, o: object) -> bool:
        return self.x == o.x and self.y == o.y if isinstance(o, Point) else False

    #  DOC: __key and __hash__ needed to be able to call `set()` on the Point class
    def __key(self) -> tuple[Any]:
        return (self.x, self.y)

    def __hash__(self) -> int:
        return hash(self.__key())


# DOC: define a custom parametric equation class to be used as a custom type
class Parametric:
    # DOC: initalize values and clean the inputted data
    def __init__(self, x_eq: str, y_eq: str) -> None:
        self.x_eq = clean_equation(x_eq)
        self.y_eq = clean_equation(y_eq)

    # DOC: swap a different letter variable for t
    def swap(self, letter: str) -> None:
        letter = sp.symbols(letter)
        self.x_eq = self.x_eq.subs(t, letter)
        self.y_eq = self.y_eq.subs(t, letter)

    # DOC: __repr__ needed for printing to console
    def __repr__(self) -> str:
        return f"({self.x_eq}, {self.y_eq})"
