import random

class MazeGrid:
    
    TILE_DICT = {0:'◌', # Void
                 1:'·', # Floor
                 2:'█',  # Wall
                 3:'⛔', # Entrance
                 4:'🏁', # Exit
                 5:'☺' # Player
                }
    
    def __init__(self, width, height):
        self.grid = self._create_blank_grid(width, height)
        self._create_maze(width, height)
        
    def _create_blank_grid(self, width, height):
        grid = []
        
        for row in range(height):
            new_row = []
            for col in range(width):
                new_row.append(0)
            grid.append(new_row)
        
        return grid
    
    def print_grid(self, raw=False):
        for row in self.grid:
            for tile in row:
                match raw:
                    case True : print(tile, end='')
                    case False: print(MazeGrid.TILE_DICT[tile], end='')
                    case _    :
                        print(f'Error! Invalid option (raw={raw}).')
                        return False
            print()
    
    def _create_maze(self, width, height):
        # First, fill in the grid with solid stone:
        for row_counter in range( len(self.grid) ):
            for col_counter in range( len(self.grid[row_counter]) ):
                self.grid[row_counter][col_counter] = 2
        
        # Then, set A and B (entrance and exit):
            # TO DO
        way_in_row  = random.randint(0, height) # Both included
        way_out_row = random.randint(0, height) # Both included
        
        # 3: Entrance, 4: Exit
        self.grid[way_in_row ][   0   ] = 3 #   0   = First col (left )
        self.grid[way_out_row][width-1] = 4 # width = Last  col (right)
        
        # Then, carve out a path between A and B:
            # TO DO