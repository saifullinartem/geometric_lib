from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter


figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']

figures = {
    'circle': {'area': circle_area, 'perimeter': circle_perimeter},
    'square': {'area': square_area, 'perimeter': square_perimeter},
    'triangle': {'area': triangle_area, 'perimeter': triangle_perimeter}
}

sizes = {
    'circle-area': 1,
    'circle-perimeter': 1,
    'square-area': 1,
    'square-perimeter': 1,
    'triangle-area': 3,
    'triangle-perimeter': 3
}


def calc(fig, func, size):
    assert fig in figs, f"Unknown figure: {fig}"
    assert func in funcs, f"Unknown function: {func}"

    key = f'{fig}-{func}'
    assert len(size) == sizes[key], f"Invalid size for {fig} {func}"

    return figures[fig][func](*size)


if __name__ == "__main__":
    func = ''
    fig = ''
    size = []

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}: \n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}: \n")

    while len(size) != sizes.get(f"{fig}-{func}", 1):
        size = list(
            map(
                int,
                input("Input figure sizes separated by space\n").split()
            )
        )

    result = calc(fig, func, size)
    print(f"Result: {result}")
