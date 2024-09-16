from networkx import DiGraph
from random import randint

class Neighbors:
    def get_neighbors(rows: int, columns: int, method: str, breadth: int) -> DiGraph:
        neighbors = eval("Neighbors." + method + "(breadth)")
        graph = DiGraph()
        
        # adding neighbors in the middle of the grid
        for i in range(breadth, (rows - breadth)):
            for j in range(breadth, (columns - breadth)):
                for neighbor in neighbors:
                    graph.add_edge((i, j), (i + neighbor[0], j + neighbor[1]))
        
        # adding neighbors on the left and right sides of the grid
        for i in range(rows):
            for j in range(0, breadth):
                for neighbor in neighbors:
                    if (0 <= (i + neighbor[0]) < rows) and ((j + neighbor[1]) >= 0):
                        graph.add_edge((i, j), (i + neighbor[0], j + neighbor[1]))
            
            for j in range((columns - breadth), columns):
                for neighbor in neighbors:
                    if (0 <= (i + neighbor[0]) < rows) and ((j + neighbor[1]) < columns):
                        graph.add_edge((i, j), (i + neighbor[0], j + neighbor[1]))
        
        # adding neighbors on the top and bottom sides of the grid
        for j in range(breadth, (columns - breadth)):
            for i in range(0, breadth):
                for neighbor in neighbors:
                    if ((i + neighbor[0]) >= 0):
                        graph.add_edge((i, j), (i + neighbor[0], j + neighbor[1]))
            
            for i in range((rows - breadth), rows):
                for neighbor in neighbors:
                    if ((i + neighbor[0]) < rows):
                        graph.add_edge((i, j), (i + neighbor[0], j + neighbor[1]))
        
        return graph
    
    def square(breadth: int) -> set:
        neighbors = set()
        for i in range(-breadth, (breadth + 1)):
            for j in range(-breadth, (breadth + 1)):
                neighbors.add((i, j))
        neighbors.remove((0, 0))
        
        return neighbors
    
    def utriangle(breadth: int) -> set:
        neighbors = set()
        extension = 0
        for i in range(-breadth, 1):
            for j in range(-extension, (extension + 1)):
                neighbors.add((i, j))
            extension += 1
        neighbors.remove((0, 0))
        
        return neighbors
    
    def dtriangle(breadth: int) -> set:
        neighbors = set()
        extension = breadth
        for i in range(0, (breadth + 1)):
            for j in range(-extension, (extension + 1)):
                neighbors.add((i, j))
            extension -= 1
        neighbors.remove((0, 0))
        
        return neighbors
    
    def ltriangle(breadth: int) -> set:
        neighbors = set()
        extension = 0
        for j in range(-breadth, 1):
            for i in range(-extension, (extension + 1)):
                neighbors.add((i, j))
            extension += 1
        neighbors.remove((0, 0))
        
        return neighbors
    
    def rtriangle(breadth: int) -> set:
        neighbors = set()
        extension = breadth
        for j in range(0, (breadth + 1)):
            for i in range(-extension, (extension + 1)):
                neighbors.add((i, j))
            extension -= 1
        neighbors.remove((0, 0))
        
        return neighbors
    
    def rhombus(breadth: int) -> set:
        neighbors = set()
        extension = 0
        for i in range(-breadth, 1):
            for j in range(-extension, (extension + 1)):
                neighbors.add((i, j))
            extension += 1
        neighbors.remove((0, 0))
        
        extension -= 2
        for i in range(1, (breadth + 1)):
            for j in range(-extension, (extension + 1)):
                neighbors.add((i, j))
            extension -= 1
        
        return neighbors
    
    def lparallelogram(breadth: int) -> set:
        neighbors = set()
        extension = 0
        for i in range(-breadth, (breadth + 1)):
            for j in range((-breadth + extension), (breadth + extension + 1)):
                neighbors.add((i, j))
            extension += 1
        neighbors.remove((0, 0))
        
        return neighbors
    
    def rparallelogram(breadth: int) -> set:
        neighbors = set()
        extension = 0
        for i in range(-breadth, (breadth + 1)):
            for j in range((-breadth + extension), (breadth + extension + 1)):
                neighbors.add((i, j))
            extension -= 1
        neighbors.remove((0, 0))
        
        return neighbors
    
    def circle(breadth: int) -> set:
        # Bresenham's circle algorithm
        x, y, err = breadth, 0, 0
        neighbors = set()
        while x >= y:
            neighbors.add((x, y))
            neighbors.add((y, x))
            neighbors.add((-y, x))
            neighbors.add((-x, y))
            neighbors.add((-x, -y))
            neighbors.add((-y, -x))
            neighbors.add((y, -x))
            neighbors.add((x, -y))
        
            y += 1
            err += 1 + (2 * y)
            if (2 * (err - x)) + 1 > 0:
                x -= 1
                err += 1 - (2 * x)
        
        # filling the circle
        for i in range((-breadth + 1), breadth):
            j = 0
            while((i, j) not in neighbors):
                neighbors.add((i, j))
                j += 1
            j = -1
            while((i, j) not in neighbors):
                neighbors.add((i, j))
                j -= 1
        neighbors.remove((0, 0))
        
        return neighbors
    
    def vminus(breadth: int) -> set:
        neighbors = set()
        for i in range(-breadth, (breadth + 1)):
            neighbors.add((i, 0))
        neighbors.remove((0, 0))
        
        return neighbors
    
    def hminus(breadth: int) -> set:
        neighbors = set()
        for j in range(-breadth, (breadth + 1)):
            neighbors.add((0, j))
        neighbors.remove((0, 0))
        
        return neighbors
    
    def plus(breadth: int) -> set:
        return Neighbors.vminus(breadth).union(Neighbors.hminus(breadth))
    
    def tree(breadth: int) -> set:
        neighbors = Neighbors.utriangle(breadth)
        for i in range(1, (breadth + 1)):
            neighbors.add((i, 0))
        
        return neighbors

class Grid:
    nf_info = {"neighbors": ["square", "utriangle", "dtriangle", "ltriangle", "rtriangle", "rhombus",
                             "lparallelogram", "rparallelogram", "circle", "vminus", "hminus", "plus", "tree"],
               "formulas": ["conway"]}
    
    def __init__(self, rows: int, columns: int, neighbors: str, breadth: int, formula: str = "conway"):
        self.rows = rows
        self.columns = columns
        self.random_grid(rows, columns)
        
        self.neighbors = Neighbors.get_neighbors(rows, columns, neighbors, breadth)
        self.formula = "self." + formula
        
        self.updates = 0
        
        print("A grid " + str(rows) + " x " + str(columns) + " has been created.")
    
    def info(self, what: str = "all") -> None:
        if (what == "all"):
            print("The neighbors of each individual can be taken as:")
            print(str(self.nf_info["neighbors"]))
            
            print("The formulas to determine the survival of each individual are:")
            print(str(self.nf_info["formulas"]))
        elif (what == "neighbors"):
            print("The neighbors of each individual can be taken as:")
            print(str(self.nf_info["neighbors"]))
        elif (what == "formulas"):
            print("The formulas to determine the survival of each individual are:")
            print(str(self.nf_info["formulas"]))
    
    def get_rows(self) -> int:
        return self.rows
    
    def get_columns(self) -> int:
        return self.columns
    
    def get_grid(self) -> set:
        return self.grid
    
    def get_num_alives(self) -> int:
        return len(self.grid)
    
    def get_updates(self) -> int:
        return self.updates
    
    def random_grid(self, rows: int, columns: int) -> None:
        self.grid = set()
        for i in range(rows):
            for j in range(columns):
                if randint(0, 2) == 1:
                    self.grid.add((i, j))
    
    def conway(self) -> None:
        new_grid = set()
        for i in range(self.rows):
            for j in range(self.columns):
                neighbors_sum = 0
                for neighbor in self.neighbors[i, j]:
                    if neighbor in self.grid:
                        neighbors_sum += 1
                if ((neighbors_sum == 3) or ((neighbors_sum == 2) and ((i, j) in self.grid))):
                    new_grid.add((i, j))
        self.grid = new_grid
    
    def update(self) -> None:
        eval(self.formula + "()")
        self.updates += 1
    
    def print_grid(self) -> None:
        print("Printing of the grid:")
        for i in range(self.rows):
            print("-", end = "")
            for j in range(self.columns):
                if (i, j) in self.grid:
                    print(1, end = "-")
                else:
                    print(0, end = "-")
            print()
        print()