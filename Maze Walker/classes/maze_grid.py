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
        self.width  = width
        self.height = height
        self.grid   = self._create_blank_grid()
        self._create_maze()
        
    def _create_blank_grid(self):
        grid = []
        
        for row in range(self.height):
            new_row = []
            for col in range(self.width):
                new_row.append(0)
            grid.append(new_row)
        
        return grid
    
    def print_grid(self, raw=False):
        print('0123456789')
        for row in self.grid:
            for tile in row:
                match raw:
                    case True : print(tile, end='')
                    case False: print(MazeGrid.TILE_DICT[tile], end='')
                    case _    :
                        print(f'Error! Invalid option (raw={raw}).')
                        return False
            print()
        print('0123456789')
    
    def _create_maze(self):
        # First, fill in the grid with solid stone:
        for row_counter in range( len(self.grid) ):
            for col_counter in range( len(self.grid[row_counter]) ):
                self.grid[row_counter][col_counter] = 2
        
        # Then, set A and B (entrance and exit):
        way_in_row  = random.randint(0, self.height-2) # Both included
        way_out_row = random.randint(0, self.height-2) # Both included
        
        # 3: Entrance, 4: Exit
        self.grid[way_in_row ][   0   ]      = 3 #   0   = First col (left )
        self.grid[way_out_row][self.width-1] = 4 # width = Last  col (right)
        
        # Then, carve out a path between A and B:
        carver_coords = [way_in_row, 1] # row, col
        self.grid[carver_coords[0]][carver_coords[1]] = 1 # = Floor
        
        pedometer = 0
        while True:
            print(f'Step {pedometer}: row {carver_coords[0]}, col {carver_coords[1]};')
            self.print_grid(raw=False)
            
            match (move := random.choice(('up', 'down', 'left', 'right'))):
                case 'right' if carver_coords[1] < self.width-1:
                    carver_coords[1] +=1 # One col forward
                case 'up'    if carver_coords[0] > 1:
                    carver_coords[0] -=1 # One row up
                case 'down'  if carver_coords[0] < self.height-1:
                    carver_coords[0] +=1 # One row down
            
            print(move, carver_coords)
            
            if not (self.grid[carver_coords[0]][carver_coords[1]] == 4): # Exit
                self.grid[carver_coords[0]][carver_coords[1]] = 1 # = Floor
            else:
                print('Exit reached!')
                break
            
            pedometer +=1