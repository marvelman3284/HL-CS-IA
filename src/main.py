import sympy as sp
import logging
from rich import print
from sympy.abc import x, y
from helpers import Parametric, Point

logging.basicConfig(filename="logger.log", filemode="w", level=logging.DEBUG)


def main(parametric_eq1: Parametric, parametric_eq2: Parametric):
    intersections = {
        "equation1": {"real": [], "imaginary": []},
        "equation2": {"real": [], "imaginary": []},
    }

    # DOC: swap t for x and y in parametric equation 1 and 2, respectively
    parametric_eq1.swap("x")
    parametric_eq2.swap("y")

    eq3 = (
        parametric_eq2.x_eq - parametric_eq1.x_eq
    )  # DOC: set the two 'x' equations equal to each other and move everything to one side of the equation
    logging.debug(f"setting the two x equations equal to each other: {eq3} ")

    eq4 = (
        parametric_eq2.y_eq - parametric_eq1.y_eq
    )  # DOC: set the two 'y' eqatuions equal to each other and move everything to one side of the equation
    logging.debug(f"setting the two y equations equal to each other: {eq4}")

    a = sp.solve(eq3, x)  # DOC: solve eq3 for x
    logging.debug(f'put eq3 in terms of x: "x="{a}')

    b = eq4.subs(x, a[0])  # DOC: substitutes a[0] for y in eq4
    logging.debug(f"substitue x into eq4: {b}")

    c = sp.solve(b, y)  # DOC: solves `b` for y
    logging.debug(f"solves eq4 for y: {c}")

    d = sp.solve(eq3.subs(y, c[0]), x)  # DOC: solves equation 3 with c[0]
    logging.debug(f"plug that solution back into eq 3: {d}")

    for i in d:
        e = Point(parametric_eq1.x_eq.subs(x, i), parametric_eq1.y_eq.subs(x, i))
        if "I" in str(e):
            intersections["equation1"]["imaginary"].append(e)
        else:
            intersections["equation1"]["real"].append(e)

    for i in c:
        e = Point(parametric_eq2.x_eq.subs(y, i), parametric_eq2.y_eq.subs(y, i))
        if "I" in str(e):
            intersections["equation2"]["imaginary"].append(e)
        else:
            intersections["equation2"]["real"].append(e)

    logging.debug(
        f"plug values back into the original parametric equations: {intersections}"
    )

    return intersections


if __name__ == "__main__":

    # NOTE: working: polynomial, radical, rational
    # FIX: not working: trig function,  exponential, rational to an exponent, abs?
    para = Parametric("t**2", "t")
    para1 = Parametric("t", "2*t")
    print((main(para, para1)))
