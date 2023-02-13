import sympy as sp
from sympy.abc import t


def clean_equation(eq: str):
    """
    Return a sympified equation.

    Given a string turn it into a equation that is usable by sympy.

    Args:
        eq (str): the equation to be sympified

    Returns:
        Any: a sympify equation
    """

    if eq == "":
        eq = input("Enter an equation: ")

    try:
        return sp.sympify(eq)
    except ValueError:
        print("Incorrect syntax!")
        print(
            "Enter one side of the equation (set everything equal to 0) using x and y (eg: x**2 - y == x**2 = y)"
        )
        new_eq: str = input("Enter the equation with correct syntax: ")
        return clean_equation(new_eq)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, o: object) -> bool:
        return self.x == o.x and self.y == o.y if isinstance(o, Point) else False

    #  DOC: __key and __hash__ needed to be able to call `set()` on the Point class
    def __key(self):
        return (self.x, self.y)

    def __hash__(self):
        return hash(self.__key())


class Parametric:
    def __init__(self, x_eq: str, y_eq: str):
        self.x_eq = clean_equation(x_eq)
        self.y_eq = clean_equation(y_eq)

    def swap(self, letter: str):
        # DOC: plug in a letter for t
        letter = sp.symbols(letter)
        self.x_eq = self.x_eq.subs(t, letter)
        self.y_eq = self.y_eq.subs(t, letter)

    def __repr__(self) -> str:
        return f"({self.x_eq}, {self.y_eq})"
