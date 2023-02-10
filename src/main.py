import sympy as sp
from sympy.abc import a, b
import logging
from rich import print
from helpers import Parametric, Point

logging.basicConfig(filename="logger.log", filemode="w", level=logging.DEBUG)


def main(parametric_eq1: Parametric, parametric_eq2: Parametric):
    ints = []
    parametric_eq1.swap('a')
    parametric_eq2.swap('b')

    x_equations = parametric_eq2.x_eq - parametric_eq1.x_eq
    y_equations = parametric_eq2.y_eq - parametric_eq1.y_eq

    x_equations = sp.solveset(x_equations, a)
    y_equations = y_equations.subs(a, list(x_equations)[0])

    y_equations = sp.solve(y_equations, b, check=False)

    for i in y_equations:
        ints.append(Point(parametric_eq1.x_eq.subs(a, i), parametric_eq1.y_eq.subs(a, i)))

    print(x_equations, y_equations, ints, sep="\n")


if __name__ == "__main__":

    # NOTE: working: polynomial, radical, rational
    # FIX: not working: trig function,  exponential, rational to an exponent, abs?
    para = Parametric("t**3", "t")
    para1 = Parametric("t", "t*(1/8)")
    print((main(para, para1)))
