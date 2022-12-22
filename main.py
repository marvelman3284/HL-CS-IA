import sympy as sp
from sympy.abc import x, y, z, t, a, b


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


class Parametric:
    def __init__(self, x_eq: str, y_eq: str):
        self.x_eq = clean_equation(x_eq)
        self.y_eq = clean_equation(y_eq)

    def __repr__(self) -> str:
        return f"({self.x_eq}, {self.y_eq})"


def main(parametric_eq1: Parametric, parametric_eq2: Parametric):
    parametric_eq1.x_eq = parametric_eq1.x_eq.subs(t, x)
    parametric_eq1.y_eq = parametric_eq1.y_eq.subs(t, x)

    parametric_eq2.x_eq = parametric_eq2.x_eq.subs(t, y)
    parametric_eq2.y_eq = parametric_eq2.y_eq.subs(t, y)

    eq3 = parametric_eq2.x_eq - parametric_eq1.x_eq
    eq4 = parametric_eq2.y_eq - parametric_eq1.y_eq

    a = sp.solve(eq3, x)  # DOC: solve eq3 for x
    b = eq4.subs(x, a[0])  # DOC: substitutes a[0] for x in eq4
    c = sp.solve(b, y)  # DOC: solves `b` for y
    d = sp.solve(eq3.subs(y, c[0]), x)
    e = Point(parametric_eq1.x_eq.subs(x, d[0]), parametric_eq1.y_eq.subs(x, d[0]))
    f = Point(parametric_eq2.x_eq.subs(y, c[0]), parametric_eq2.y_eq.subs(y, c[0]))
    g = Point(parametric_eq2.x_eq.subs(y, c[1]), parametric_eq2.y_eq.subs(y, c[1]))
    print(f"eq3: {eq3} \neq4: {eq4}")
    print(f"a: {a}, \nb: {b}, \nc: {c}, \nd: {d}, \ne: {e}, \nf: {f}, \ng: {g}")


if __name__ == "__main__":
    para = Parametric("t+1", "t**2")
    para1 = Parametric("3*t+1", "t**2+1")
    print(main(para, para1))
