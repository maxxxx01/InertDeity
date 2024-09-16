import ctypes
import pygame

class Window:
    m_info = set(("squares", "circles"))
    
    def __init__(self, width: int, height: int, rows: int, columns: int, how: str,
                 background: tuple = (0, 0, 0), individual_color: tuple = (255, 255, 255),
                 connection_color: tuple = (0, 0, 255)):
        width = min(width, ctypes.windll.user32.GetSystemMetrics(0))
        height = min(height, ctypes.windll.user32.GetSystemMetrics(1))
        
        self.back_grid = {}
        prefix_x = ((width % rows) / 2)
        prefix_y = ((height % columns) / 2)
        self.cell_width = ((width - (prefix_x * 2)) / columns)
        self.cell_height = ((height - (prefix_y * 2)) / rows)
        for i in range(rows):
            for j in range(columns):
                self.back_grid[(i, j)] = ((prefix_x + 1 + (self.cell_width * j)), (prefix_y + 1 + (self.cell_height * i)))
        
        self.how = how
        
        self.radius = (min(self.cell_width, self.cell_height) // 3)
        line_width = int(min(self.cell_width, self.cell_height) / 10)
        self.line_width = line_width if line_width >= 1 else 1
        
        self.background = background
        self.individual_color = individual_color
        self.connection_color = connection_color
        
        self.window = pygame.display.set_mode((width, height))
        self.window.fill(self.background)
        
        print("A " + str(width) + " x " + str(height) + " window has been created.")
    
    def info(self, what: str = "all") -> None:
        if (what == "all"):
            print("The methods to print the elements of the grid are:")
            print(str(self.m_info))
    
    def is_alive(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
    
    def draw_squares(self, grid: set) -> None:
        for pos in grid:
            pygame.draw.rect(self.window, self.individual_color,
                             pygame.Rect(self.back_grid[pos], (self.cell_width - 1, self.cell_height - 1)), 2)
    
    def draw_circles(self, grid: set) -> None:
        offset = ((self.cell_width // 2), (self.cell_height // 2))
        
        for pos in grid:
            for i in range((pos[0] - 1), (pos[0] + 2)):
                for j in range((pos[1] - 1), (pos[1] + 2)):
                    if (i, j) in grid:
                        pygame.draw.line(self.window, self.connection_color,
                                         (self.back_grid[pos][0] + offset[0], self.back_grid[pos][1] + offset[1]),
                                         (self.back_grid[(i, j)][0] + offset[0], self.back_grid[(i, j)][1] + offset[1]),
                                         self.line_width)
        for pos in grid:
            pygame.draw.circle(self.window, self.individual_color,
                               (self.back_grid[pos][0] + offset[0], self.back_grid[pos][1] + offset[1]), self.radius)
    
    def draw(self, grid: set, delay: int = 0) -> None:
        eval("self.draw_" + self.how + "(grid)")
        
        pygame.display.update()
        pygame.time.wait(delay)
    
    def clear(self) -> None:
        self.window.fill(self.background)