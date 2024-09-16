from graphics import Window
from logic import Grid

def preparation() -> (Window, Grid):
    grid = Grid(50, 50, "circle", 2)
    window = Window(1080, 640, grid.get_rows(), grid.get_columns(), "circles")
    
    return window, grid

def play(window: Window, grid: Grid) -> None:
    window.draw(grid.get_grid(), delay = 80)
    print("Number of individuals = " + str(grid.get_num_alives()))
    
    while (window.is_alive()):
        grid.update()
        window.clear()
        window.draw(grid.get_grid(), delay = 80)
        print("Number of individuals = " + str(grid.get_num_alives()))
    
    print("The grid has been updated " + str(grid.get_updates()) + " times.\n")