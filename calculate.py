import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
    """
    Calculates the perimeter or area of a circle or square.

    Args:
        fig (str): The name of the figure, either 'circle' or 'square'.
        func (str): The function to calculate, either 'perimeter' or 'area'.
        size (list): A list of size values for the figure.
                     For a circle, it should contain one value (radius).
                     For a square, it should contain one value (side length).

    Returns:
        None. Prints the calculated result.
    """
    assert fig in figs, f"Invalid figure name. Choose from: {figs}"
    assert func in funcs, f"Invalid function name. Choose from: {funcs}"

    result = eval(f'{fig}.{func}(*{size})')
    print(f'{func} of {fig} is {result}')


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()
    
    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")
    
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")
    
    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
    
    calc(fig, func, size



