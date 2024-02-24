import sympy as sp  # DOC: math operations
from sympy.abc import x, y  # DOC: specific math imports
import logging  # DOC: import built-in logging function
from rich import print  # DOC: pretty print
from helpers import Parametric, Point  # DOC: import classes from a local file


#  DOC: setup the logger
logging.basicConfig(filename="logger.log", filemode="w", level=logging.DEBUG)


def main(parametric_eq1: Parametric, parametric_eq2: Parametric):
    intersections: list[Point] = []
    dual_intersections = {"equation1": [], "equation2": []}

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
    logging.debug(f'put eq3 in terms of x(a): "x="{a}')

    for i in a:
        b = eq4.subs(x, i)  # DOC: substitutes `a[i]` for y in eq4
        logging.debug(f"substitue x into eq4(b): {b}")

        c = sp.solve(b, y)  # DOC: solves `b` for y
        logging.debug(f"solves eq4 for y(c): {c}")

        for j in c:
            d = sp.solve(eq3.subs(y, j), x)  # DOC: solves `eq3` with `c[i]`
            logging.debug(f"plug that solution back into eq 3(d): {d}")

            points = d + c

            for k in points:
                e = Point(
                    parametric_eq1.x_eq.subs(x, k), parametric_eq1.y_eq.subs(x, k)
                )
                if "I" in str(e):
                    # NOTE: we don't really care about imaginary intersections, but log them just in case
                    logging.info(f"Imaginary intersection: {e}")
                else:
                    # DOC: if it's real then append it to the list of intersections
                    dual_intersections["equation1"].append(e)

            for k in points:
                # DOC: repeat the same process as above, just with the second parametric equation
                e = Point(
                    parametric_eq2.x_eq.subs(y, k), parametric_eq2.y_eq.subs(y, k)
                )
                if "I" in str(e):
                    continue
                else:
                    dual_intersections["equation2"].append(e)

    logging.debug(
        f"plug values back into the original parametric equations: {dual_intersections}"
    )

    for i in dual_intersections["equation1"]:
        if i in dual_intersections["equation2"]:
            intersections.append(i)  # DOC: combine both lists

    return [*set(intersections)]  # DOC: transform into a set in order to remove duplicates and then return


if __name__ == "__main__":
    # NOTE: working: polynomial, radical, rational
    # FIX: not working: trig function,  exponential, rational to an exponent, abs?
    para = Parametric("t**2", "t/3")
    para1 = Parametric("t+8", "t**(1/3)")
    print(para, para1, sep="\n")
    print((main(para, para1)))
