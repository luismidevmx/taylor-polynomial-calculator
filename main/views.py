from django.shortcuts import render

from main.taylor import taylor
from main.languages import error_labels, index_labels, solve_labels, error_module, select_language as sl


def index(request, lang="en"):
    """
    Renders the index page based on the specified language.

    Args:
    - request: The HTTP request object.
    - lang: The language code, defaults to "en".

    Returns:
    - The rendered index page.
    """
    return render(request, f"{sl(lang)}/index.html", index_labels(lang))


def solve(request, lang="en"):
    """
    Solves a problem based on the specified language.

    Args:
    - request: The HTTP request object.
    - lang: The language code, defaults to "en".

    Returns:
    - The result of solving the problem.
    """

    errors = error_module(lang)

    try:
        grade = int(request.GET["grade"])
        x0 = float(request.GET["x0"])
        f = request.GET["f"].replace(r"\n?\r?\t", "")

        if grade < 3:
            return render(request, "error.html", error_labels(lang, errors.GRADE_TOO_LOW_ERROR), status=400)

        if grade > 20:
            return render(request, "error.html", error_labels(lang, errors.GRADE_TOO_HIGH_ERROR), status=400)

        return render(
            request,
            f"{sl(lang)}/solve.html",
            {
                **taylor(f, x0, grade),
                **solve_labels(lang),
            },
        )

    except ValueError as e:
        err = str(e).split(":", 1)[0]

        if err == "invalid literal for int() with base 10":
            return render(request, "error.html", error_labels(lang, errors.INVALID_NUMBER_ERROR), status=400)

        if err == "could not convert string to float":
            return render(request, "error.html", error_labels(lang, errors.INVALID_X0_ERROR), status=400)

        return render(request, "error.html", error_labels(lang, errors.INVALID_EXPRESSION_ERROR), status=400)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return render(request, "error.html", error_labels(lang, errors.UNKNOWN_ERROR), status=500)


def index_en(request):
    """
    Shortcut for rendering the index page in English.

    Args:
    - request: The HTTP request object.

    Returns:
    - The rendered index page in English.
    """
    return index(request, "en")


def solve_en(request):
    """
    Shortcut for solving a problem in English.

    Args:
    - request: The HTTP request object.

    Returns:
    - The result of solving the problem in English.
    """
    return solve(request, "en")
