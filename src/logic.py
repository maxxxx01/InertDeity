from networkx import DiGraph
from random import randint

class Neighbors:
    def get_neighbors(rows: int, columns: int, method: str, breadth: int, has_center: bool) -> DiGraph:
        neighbors = eval("Neighbors." + method + "(breadth)")
        if not has_center:
            neighbors.remove((0, 0))
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
        
        return neighbors
    
    def utriangle(breadth: int) -> set:
        neighbors = set()
        extension = 0
        for i in range(-breadth, 1):
            for j in range(-extension, (extension + 1)):
                neighbors.add((i, j))
            extension += 1
        
        return neighbors
    
    def dtriangle(breadth: int) -> set:
        neighbors = set()
        extension = breadth
        for i in range(0, (breadth + 1)):
            for j in range(-extension, (extension + 1)):
                neighbors.add((i, j))
            extension -= 1
        
        return neighbors
    
    def ltriangle(breadth: int) -> set:
        neighbors = set()
        extension = 0
        for j in range(-breadth, 1):
            for i in range(-extension, (extension + 1)):
                neighbors.add((i, j))
            extension += 1
        
        return neighbors
    
    def rtriangle(breadth: int) -> set:
        neighbors = set()
        extension = breadth
        for j in range(0, (breadth + 1)):
            for i in range(-extension, (extension + 1)):
                neighbors.add((i, j))
            extension -= 1
        
        return neighbors
    
    def rhombus(breadth: int) -> set:
        neighbors = set()
        extension = 0
        for i in range(-breadth, 1):
            for j in range(-extension, (extension + 1)):
                neighbors.add((i, j))
            extension += 1
        
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
        
        return neighbors
    
    def rparallelogram(breadth: int) -> set:
        neighbors = set()
        extension = 0
        for i in range(-breadth, (breadth + 1)):
            for j in range((-breadth + extension), (breadth + extension + 1)):
                neighbors.add((i, j))
            extension -= 1
        
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
        
        return neighbors
    
    def vminus(breadth: int) -> set:
        neighbors = set()
        for i in range(-breadth, (breadth + 1)):
            neighbors.add((i, 0))
        
        return neighbors
    
    def hminus(breadth: int) -> set:
        neighbors = set()
        for j in range(-breadth, (breadth + 1)):
            neighbors.add((0, j))
        
        return neighbors
    
    def plus(breadth: int) -> set:
        return Neighbors.vminus(breadth).union(Neighbors.hminus(breadth))
    
    def tree(breadth: int) -> set:
        neighbors = Neighbors.utriangle(breadth)
        for i in range(1, (breadth + 1)):
            neighbors.add((i, 0))
        
        return neighbors

class Grid:
    nf_info = {"neighbors": ["square", "utriangle", "dtriangle", "ltriangle", "rtriangle", "rhombus", "lparallelogram",
                             "rparallelogram", "circle", "vminus", "hminus", "plus", "tree"],
               "formulas": ["AntiLife", "InverseLife", "B01245/S01245", "Wickstretcher And The Parasites", "Oils",
                            "B017/S01", "B026/S1", "Invertamaze", "Neon Blobs", "H-trees", "Fuzz", "Gnarl", "Snakeskin",
                            "Solid islands grow amongst static", "Replicator", "Fredkin", "Feux", "Seeds",
                            "Live Free or Die", "B2/S13", "B2/S2345", "B2/S23456", "B2/S2345678", "Serviettes",
                            "B25/S4", "Iceballs", "Life without death", "DotLife", "Star Trek", "Flock", "Mazectric",
                            "Maze", "Magnezones", "SnowLife", "Corrosion of Conformity", "EightFlock", "LowLife", "B3/S2",
                            "Conway's Life", "B3/S2378", "EightLife", "Shoots and Roots", "Lifeguard 2", "Coral",
                            "3-4 Life", "Dance", "Bacteria", "Never happy", "Blinkers", "Assimilation", "Long Life",
                            "Spiral and polygonal growth", "Gems", "Gems Minor", "Grounded Life", "Land Rush", "B35/S236",
                            "Bugs", "Cheerios", "Holstein", "Diamoeba", "Amoeba", "Pseudo Life", "Geology", "HighFlock",
                            "2x2", "IronFlock", "HighLife", "Land Rush 2", "Blinker Life", "IronLife", "sqrt replicator rule",
                            "Slow Blob", "DrighLife", "2x2 2", "Castles", "B3678/S23", "Stains", "Day & Night", "B368/S12578",
                            "LowFlockDeath", "Life SkyHigh", "LowDeath", "Morley", "DryLife without Death", "DryFlock",
                            "Mazectric with Mice", "Maze with Mice", "DryLife", "Plow World", "Coagulations",
                            "Pedestrian Life without Death", "Pedestrian Flock", "HoneyFlock", "Pedestrian Life", "HoneyLife",
                            "Electrified Maze", "Oscillators Rule", "Walled cities", "Majority", "Vote 4/5", "Lifeguard 1",
                            "Rings 'n' Slugs", "Vote"]}
    
    def __init__(self, rows: int, columns: int, neighbors: str = "square", breadth: int = 1, has_center: bool = False,
                 formula: str = None, birth_conditions = None, survival_conditions = None):
        self.rows = rows
        self.columns = columns
        self.random_grid(rows, columns)
        
        self.neighbors = Neighbors.get_neighbors(rows, columns, neighbors, breadth, has_center)
        
        if formula:
            self.set_formula(formula)
        if (birth_conditions and survival_conditions):
            self.set_personalized_formula(birth_conditions, survival_conditions)
        
        self.updates = 0
        
        print("A grid " + str(rows) + " x " + str(columns) + " has been created.")
    
    def info(self, what: str = "all") -> None:
        if (what == "all"):
            print("The neighbors of each individual can be taken as:")
            print(str(self.nf_info["neighbors"]))
            print(str(len(self.nf_info["neighbors"])))
            
            print()
            
            print("The formulas to determine the birth/survival of each individual are:")
            print(str(self.nf_info["formulas"]))
            print("len = " + str(len(self.nf_info["formulas"])))
        elif (what == "neighbors"):
            print("The neighbors of each individual can be taken as:")
            print(str(self.nf_info["neighbors"]))
            print(str(len(self.nf_info["neighbors"])))
        elif (what == "formulas"):
            print("The formulas to determine the birth/survival of each individual are:")
            print(str(self.nf_info["formulas"]))
            print("len = " + str(len(self.nf_info["formulas"])))
    
    def get_rows(self) -> int:
        return self.rows
    
    def get_columns(self) -> int:
        return self.columns
    
    def get_grid(self) -> set:
        return self.grid
    
    def get_num_alives(self) -> int:
        return len(self.grid)
    
    def set_formula(self, formula: str) -> None:
        # Life-like rules
        match formula:
            case "AntiLife":
                self.formula = {"B": [0, 1, 2, 3, 4, 7, 8], "S": [0, 1, 2, 3, 4, 6, 7, 8]}
            case "InverseLife":
                self.formula = {"B": [0, 1, 2, 3, 4, 7, 8], "S": [3, 4, 6, 7, 8]}
            case "B01245/S01245":
                self.formula = {"B": [0, 1, 2, 4, 5], "S": [0, 1, 2, 4, 5]}
            case "Wickstretcher And The Parasites":
                self.formula = {"B": [0, 1, 3, 5, 6], "S": [0, 1, 2, 3, 4, 5]}
            case "Oils":
                self.formula = {"B": [0, 1, 4], "S": [2]}
            case "B017/S01":
                self.formula = {"B": [0, 1, 7], "S": [0, 1]}
            case "B026/S1":
                self.formula = {"B": [0, 2, 6], "S": [1]}
            case "Invertamaze":
                self.formula = {"B": [0, 2, 8], "S": [0, 1, 2, 4]}
            case "Neon Blobs":
                self.formula = {"B": [0, 8], "S": [4]}
            case "H-trees":
                self.formula = {"B": [1], "S": [0, 1, 2, 3, 4, 5, 6, 7, 8]}
            case "Fuzz":
                self.formula = {"B": [1], "S": [0, 1, 4, 5, 6, 7]}
            case "Gnarl":
                self.formula = {"B": [1], "S": [1]}
            case "Snakeskin":
                self.formula = {"B": [1], "S": [1, 3, 4, 5, 6, 7]}
            case "Solid islands grow amongst static":
                self.formula = {"B": [1, 2, 6, 7, 8], "S": [1, 5, 6, 7, 8]}
            case "Replicator":
                self.formula = {"B": [1, 3, 5, 7], "S": [1, 3, 5, 7]}
            case "Fredkin":
                self.formula = {"B": [1, 3, 5, 7], "S": [0, 2, 4, 6, 8]}
            case "Feux":
                self.formula = {"B": [1, 3, 5, 8], "S": [0, 2, 4, 7]}
            case "Seeds":
                self.formula = {"B": [2], "S": []}
            case "Live Free or Die":
                self.formula = {"B": [2], "S": [0]}
            case "B2/S13":
                self.formula = {"B": [2], "S": [1, 3]}
            case "B2/S2345":
                self.formula = {"B": [2], "S": [2, 3, 4, 5]}
            case "B2/S23456":
                self.formula = {"B": [2], "S": [2, 3, 4, 5, 6]}
            case "B2/S2345678":
                self.formula = {"B": [2], "S": [2, 3, 4, 5, 6, 7, 8]}
            case "Serviettes":
                self.formula = {"B": [2, 3, 4], "S": []}
            case "B25/S4":
                self.formula = {"B": [2, 5], "S": [4]}
            case "Iceballs":
                self.formula = {"B": [2, 5, 6, 7, 8], "S": [5, 6, 7, 8]}
            case "Life without death":
                self.formula = {"B": [3], "S": [0, 1, 2, 3, 4, 5, 6, 7, 8]}
            case "DotLife":
                self.formula = {"B": [3], "S": [0, 2, 3]}
            case "Star Trek":
                self.formula = {"B": [3], "S": [0, 2, 4, 8]}
            case "Flock":
                self.formula = {"B": [3], "S": [1, 2]}
            case "Mazectric":
                self.formula = {"B": [3], "S": [1, 2, 3, 4]}
            case "Maze":
                self.formula = {"B": [3], "S": [1, 2, 3, 4, 5]}
            case "Magnezones":
                self.formula = {"B": [3], "S": [1, 2, 3, 6, 7, 8]}
            case "SnowLife":
                self.formula = {"B": [3], "S": [1, 2, 3, 7]}
            case "Corrosion of Conformity":
                self.formula = {"B": [3], "S": [1, 2, 4]}
            case "EightFlock":
                self.formula = {"B": [3], "S": [1, 2, 8]}
            case "LowLife":
                self.formula = {"B": [3], "S": [1, 3]}
            case "B3/S2":
                self.formula = {"B": [3], "S": [2]}
            case "Conway's Life":
                self.formula = {"B": [3], "S": [2, 3]}
            case "B3/S2378":
                self.formula = {"B": [3], "S": [2, 3, 7, 8]}
            case "EightLife":
                self.formula = {"B": [3], "S": [2, 3, 8]}
            case "Shoots and Roots":
                self.formula = {"B": [3], "S": [2, 4, 5, 6, 7, 8]}
            case "Lifeguard 2":
                self.formula = {"B": [3], "S": [4, 5, 6, 7]}
            case "Coral":
                self.formula = {"B": [3], "S": [4, 5, 6, 7, 8]}
            case "3-4 Life":
                self.formula = {"B": [3, 4], "S": [3, 4]}
            case "Dance":
                self.formula = {"B": [3, 4], "S": [3, 5]}
            case "Bacteria":
                self.formula = {"B": [3, 4], "S": [4, 5, 6]}
            case "Never happy":
                self.formula = {"B": [3, 4, 5], "S": [0, 4, 5, 6]}
            case "Blinkers":
                self.formula = {"B": [3, 4, 5], "S": [2]}
            case "Assimilation":
                self.formula = {"B": [3, 4, 5], "S": [4, 5, 6, 7]}
            case "Long Life":
                self.formula = {"B": [3, 4, 5], "S": [5]}
            case "Spiral and polygonal growth":
                self.formula = {"B": [3, 4, 5, 6, 8], "S": [1, 5, 6, 7, 8]}
            case "Gems":
                self.formula = {"B": [3, 4, 5, 7], "S": [4, 5, 6, 8]}
            case "Gems Minor":
                self.formula = {"B": [3, 4, 5, 7, 8], "S": [4, 5, 6]}
            case "Grounded Life":
                self.formula = {"B": [3, 5], "S": [2, 3]}
            case "Land Rush":
                self.formula = {"B": [3, 5], "S": [2, 3, 4, 5, 7, 8]}
            case "B35/S236":
                self.formula = {"B": [3, 5], "S": [2, 3, 6]}
            case "Bugs":
                self.formula = {"B": [3, 5, 6, 7], "S": [1, 5, 6, 7, 8]}
            case "Cheerios":
                self.formula = {"B": [3, 5, 6, 7, 8], "S": [3, 4, 5, 6, 7]}
            case "Holstein":
                self.formula = {"B": [3, 5, 6, 7, 8], "S": [4, 6, 7, 8]}
            case "Diamoeba":
                self.formula = {"B": [3, 5, 6, 7, 8], "S": [5, 6, 7, 8]}
            case "Amoeba":
                self.formula = {"B": [3, 5, 7], "S": [1, 3, 5, 8]}
            case "Pseudo Life":
                self.formula = {"B": [3, 5, 7], "S": [2, 3, 8]}
            case "Geology":
                self.formula = {"B": [3, 5, 7, 8], "S": [2, 4, 6, 7, 8]}
            case "HighFlock":
                self.formula = {"B": [3, 6], "S": [1, 2]}
            case "2x2":
                self.formula = {"B": [3, 6], "S": [1, 2, 5]}
            case "IronFlock":
                self.formula = {"B": [3, 6], "S": [1, 2, 8]}
            case "HighLife":
                self.formula = {"B": [3, 6], "S": [2, 3]}
            case "Land Rush 2":
                self.formula = {"B": [3, 6], "S": [2, 3, 4, 5, 7, 8]}
            case "Blinker Life":
                self.formula = {"B": [3, 6], "S": [2, 3, 5]}
            case "IronLife":
                self.formula = {"B": [3, 6], "S": [2, 3, 8]}
            case "sqrt replicator rule":
                self.formula = {"B": [3, 6], "S": [2, 4, 5]}
            case "Slow Blob":
                self.formula = {"B": [3, 6, 7], "S": [1, 2, 5, 6, 7, 8]}
            case "DrighLife":
                self.formula = {"B": [3, 6, 7], "S": [2, 3]}
            case "2x2 2":
                self.formula = {"B": [3, 6, 7, 8], "S": [1, 2, 5, 8]}
            case "Castles":
                self.formula = {"B": [3, 6, 7, 8], "S": [1, 3, 5, 6, 7, 8]}
            case "B3678/S23":
                self.formula = {"B": [3, 6, 7, 8], "S": [2, 3]}
            case "Stains":
                self.formula = {"B": [3, 6, 7, 8], "S": [2, 3, 5, 6, 7, 8]}
            case "Day & Night":
                self.formula = {"B": [3, 6, 7, 8], "S": [3, 4, 6, 7, 8]}
            case "B368/S12578":
                self.formula = {"B": [3, 6, 8], "S": [1, 2, 5, 7, 8]}
            case "LowFlockDeath":
                self.formula = {"B": [3, 6, 8], "S": [1, 2, 8]}
            case "Life SkyHigh":
                self.formula = {"B": [3, 6, 8], "S": [2, 3, 6]}
            case "LowDeath":
                self.formula = {"B": [3, 6, 8], "S": [2, 3, 8]}
            case "Morley":
                self.formula = {"B": [3, 6, 8], "S": [2, 4, 5]}
            case "DryLife without Death":
                self.formula = {"B": [3, 7], "S": [0, 1, 2, 3, 4, 5, 6, 7, 8]}
            case "DryFlock":
                self.formula = {"B": [3, 7], "S": [1, 2]}
            case "Mazectric with Mice":
                self.formula = {"B": [3, 7], "S": [1, 2, 3, 4]}
            case "Maze with Mice":
                self.formula = {"B": [3, 7], "S": [1, 2, 3, 4, 5]}
            case "DryLife":
                self.formula = {"B": [3, 7], "S": [2, 3]}
            case "Plow World":
                self.formula = {"B": [3, 7, 8], "S": [0, 1, 2, 3, 4, 5, 6, 7, 8]}
            case "Coagulations":
                self.formula = {"B": [3, 7, 8], "S": [2, 3, 5, 6, 7, 8]}
            case "Pedestrian Life without Death":
                self.formula = {"B": [3, 8], "S": [0, 1, 2, 3, 4, 5, 6, 7, 8]}
            case "Pedestrian Flock":
                self.formula = {"B": [3, 8], "S": [1, 2]}
            case "HoneyFlock":
                self.formula = {"B": [3, 8], "S": [1, 2, 8]}
            case "Pedestrian Life":
                self.formula = {"B": [3, 8], "S": [2, 3]}
            case "HoneyLife":
                self.formula = {"B": [3, 8], "S": [2, 3, 8]}
            case "Electrified Maze":
                self.formula = {"B": [4, 5], "S": [1, 2, 3, 4, 5]}
            case "Oscillators Rule":
                self.formula = {"B": [4, 5], "S": [1, 2, 3, 5]}
            case "Walled cities":
                self.formula = {"B": [4, 5, 6, 7, 8], "S": [2, 3, 4, 5]}
            case "Majority":
                self.formula = {"B": [4, 5, 6, 7, 8], "S": [5, 6, 7, 8]}
            case "Vote 4/5":
                self.formula = {"B": [4, 6, 7, 8], "S": [3, 5, 6, 7, 8]}
            case "Lifeguard 1":
                self.formula = {"B": [4, 8], "S": [2, 3, 4]}
            case "Rings 'n' Slugs":
                self.formula = {"B": [5, 6], "S": [1, 4, 5, 6, 8]}
            case "Vote":
                self.formula = {"B": [5, 6, 7, 8], "S": [4, 5, 6, 7, 8]}
    
    def set_personalized_formula(self, birth_conditions: list, survival_conditions: list) -> None:
        self.formula = {"B": birth_conditions, "S": survival_conditions}
    
    def get_updates(self) -> int:
        return self.updates
    
    def random_grid(self, rows: int, columns: int) -> None:
        self.grid = set()
        for i in range(rows):
            for j in range(columns):
                if randint(0, 2) == 1:
                    self.grid.add((i, j))
    
    def update(self) -> None:
        new_grid = set()
        for i in range(self.rows):
            for j in range(self.columns):
                neighbors_sum = 0
                for neighbor in self.neighbors[i, j]:
                    if neighbor in self.grid:
                        neighbors_sum += 1
                
                if ((i, j) in self.grid):
                    if neighbors_sum in self.formula["S"]:
                        new_grid.add((i, j))
                else:
                    if neighbors_sum in self.formula["B"]:
                        new_grid.add((i, j))
        self.grid = new_grid
    
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