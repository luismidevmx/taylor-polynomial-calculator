from cachetools.func import ttl_cache
import sympy as sym

# precomputed factorials from 0 to 20
FACTORIALS = (
    1,
    1,
    2,
    6,
    24,
    120,
    720,
    5040,
    40320,
    362880,
    3628800,
    39916800,
    479001600,
    6227020800,
    87178291200,
    1307674368000,
    20922789888000,
    355687428096000,
    6402373705728000,
    121645100408832000,
    2432902008176640000,
)


@ttl_cache(maxsize=1024, ttl=2 * 60 * 60)
def taylor(strf: str, x0: float, grade: int) -> dict:
    """
    Calculate the Taylor Series of a function centered at x0 of a given grade.

    Args:
        strf (str): The function to be approximated as a string.
        x0 (float): The point at which to center the approximation.
        grade (int): The grade of the Taylor Series.

    Returns:
        dict: A dictionary containing the grade, the center point, the initial function,
        the result of the approximation, and the steps of the calculation.
    """
    x = sym.Symbol("x")
    fx = sym.parse_expr(strf, transformations="all").subs("e", sym.E)

    steps = list(map(lambda i: {"i": i}, range(grade + 1)))
    # print("taylor invoked with:", strf, x0, grade)
    result = sym.parse_expr("0")

    for step in steps:
        i = step["i"]
        dfx, dfx_data = cached_diff(fx, i)
        value = float(dfx.subs(x, x0))
        factor = float(value / FACTORIALS[i])
        result += factor * (x - x0) ** i

        step["factorial"] = FACTORIALS[i]
        step["value"] = value
        step["factor"] = factor

        step["derivative"] = dfx_data

        step["current_tp"] = {
            "inline": str(result),
            "latex": sym.latex(result, itex=True, ln_notation=True),
            "javascript": sym.jscode(result),
        }

    return {
        "grade": grade,
        "x0": x0,
        "initial_function": steps[0]["derivative"],
        "result": steps[-1]["current_tp"],
        "steps": steps,
    }


@ttl_cache(maxsize=1024, ttl=2 * 60 * 60)
def cached_diff(fx: sym.Expr, grade: int):
    """
    Checks if derivative is cached, if not, calculates.

    Args:
        fx: The input expression
        grade: The grade of the derivative

    Returns:
        The derivative of the input expression and a dictionary containing inline, latex, and javascript representations.
    """
    dfx = fx.diff("x", grade).simplify()

    return dfx, {
        "inline": str(dfx),
        "latex": sym.latex(dfx, itex=True, ln_notation=True),
        "javascript": sym.jscode(dfx),
    }


if __name__ == "__main__":
    from prettyprinter import cpprint as p

    (taylor("x*sin(x/3)**2 + exp(x/2) - log(x)", 1, 3))
    (taylor("x*sin(x/3)**2 + exp(x/2) - log(x)", 1, 3))
    (taylor("x*sin(x/3)**2 + exp(x/2) - log(x)", 1, 4))
    (taylor("x*sin(x/3)**2 + exp(x/2) - log(x)", 1, 3))
    p(taylor("x*sin(x/3)**2 + exp(x/2) - log(x)", 1, 6))
