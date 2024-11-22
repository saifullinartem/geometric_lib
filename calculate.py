# geometric_lib/calculate.py
from geometric_lib import circle, square, triangle  # noqa: F401

figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {
    'perimeter-circle': 1,
    'area-circle': 1,
    'perimeter-square': 1,
    'area-square': 1,
    'perimeter-triangle': 3,
    'area-triangle': 3
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
        'circle': circle,
        'square': square,
        'triangle': triangle
    }

    selected_module = function_map[fig]
    selected_function = getattr(selected_module, func)
    return selected_function(*size)


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    expected_size = sizes.get(f"{func}-{fig}", 1)
    while len(size) != expected_size:
        try:
            size = list(map(float, input(
                f"Input figure sizes separated by space, {expected_size} parameter(s) required:\n"
            ).split()))
        except ValueError:
            print("Please enter valid numbers.")
            size = []

    try:
        result = calc(fig, func, size)
        print(f'{func} of {fig} is {result}')
    except ValueError as ve:
        print(f"Error: {ve}")
