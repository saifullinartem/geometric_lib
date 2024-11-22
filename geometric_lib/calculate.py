# calculate.py

from circle import area as circle_area, perimeter as circle_perimeter  # noqa: F401
from square import area as square_area, perimeter as square_perimeter  # noqa: F401
from triangle import (
    area as triangle_area,
    perimeter as triangle_perimeter,
)  # noqa: F401

figs = ["circle", "square", "triangle"]
funcs = ["perimeter", "area"]
sizes = {
    "perimeter-circle": 1,
    "area-circle": 1,
    "perimeter-square": 1,
    "area-square": 1,
    "perimeter-triangle": 3,
    "area-triangle": 3,
}


def calc(fig, func, size):
    """Вычисляет периметр или площадь заданной фигуры."""
    if fig not in figs:
        raise ValueError(f"Figure '{fig}' is not supported.")

    if func not in funcs:
        raise ValueError(f"Function '{func}' is not supported.")

    expected_size = sizes.get(f"{func}-{fig}")
    if expected_size is None:
        raise ValueError(f"Function '{func}' is not supported for figure '{fig}'.")
    if len(size) != expected_size:
        raise ValueError(
            f"Function '{func}' for figure '{fig}' expects {expected_size} parameter(s)."
        )

    # Используем словарь вместо eval для безопасности
    function_map = {
        "circle": circle_perimeter if func == "perimeter" else circle_area,
        "square": square_perimeter if func == "perimeter" else square_area,
        "triangle": triangle_perimeter if func == "perimeter" else triangle_area,
    }

    selected_function = function_map[fig]
    return selected_function(*size)


if __name__ == "__main__":
    func = ""
    fig = ""
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n").strip().lower()

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n").strip().lower()

    expected_size = sizes.get(f"{func}-{fig}", 1)
    while len(size) != expected_size:
        try:
            size_input = input(
                f"Input figure sizes separated by space, {expected_size} parameter(s) required:\n"
            )
            size = list(map(float, size_input.split()))
        except ValueError:
            print("Please enter valid numbers.")
            size = []

    try:
        result = calc(fig, func, size)
        print(f"{func} of {fig} is {result}")
    except ValueError as ve:
        print(f"Error: {ve}")
