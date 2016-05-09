#http://www.codeskulptor.org/#user41_fDmDTSjMeW_12.py
"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    new_line = []
    for i in line:
        if i != 0:
            new_line.append(i)

    while len(new_line)<len(line):
        new_line.append(0)

    #print '/n'
    #print 'newline', new_line
    newnew_line = [ ]
    #print 'newnew_line' ,newnew_line
    ii = 0
    while ii < len(line):
        try:
            if new_line[ii] == new_line[ii+1] and new_line[ii] !=0 :
                newnew_line.append(2 * new_line[ii])
                ii += 2
            else:
                newnew_line.append(new_line[ii])
                ii += 1
        except:
            newnew_line.append(new_line[ii])
            ii += 1

    #print 'newnew_line' ,newnew_line

    for i in new_line:
        if i == 0:
            new_line.remove(i)

    while len(newnew_line)<len(line):
        newnew_line.append(0)

    return newnew_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for widd in range(self.grid_width)]
                     for heii in range(self.grid_height)]
        #print self.grid
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """

        return str(self.grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height


    def get_grid_width(self):
        """
        Get the width of the board.
        """

        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if direction == 1:
            # up
            new_lis  = [[self.grid[a][b] for a in range(len(self.grid))]
                       for b in range(len(self.grid[0]))]

            old_grid = [[self.grid[a][b] for b in range(len(self.grid[0]))]
                         for a in range(len(self.grid))]


            for i in range(len(new_lis)):
                new_lis[i] = merge(new_lis[i])
            self.grid = [[new_lis[a][b] for a in range(len(new_lis))]
                         for b in range(len(new_lis[0]))]
            if old_grid != self.grid:
                self.new_tile()


        elif direction == 2:
            # down
            new_lis  = [[self.grid[a][b]
                         for a in range(len(self.grid)-1,-1,-1)]
                       for b in range(len(self.grid[0]))]
            old_grid = [[self.grid[a][b] for b in range(len(self.grid[0]))]
                         for a in range(len(self.grid))]
            print old_grid


            for i in range(len(new_lis)):
                new_lis[i] = merge(new_lis[i])
            self.grid = [[new_lis[a][b]
                          for a in range(len(new_lis))]
                         for b in range(len(new_lis[0])-1,-1,-1)]
            print self.grid
            if old_grid != self.grid:
                self.new_tile()


        elif direction == 3:
            # left
            old_grid = [[self.grid[a][b] for b in range(len(self.grid[0]))]
                         for a in range(len(self.grid))]
            for i in range(len(self.grid)):
                self.grid[i] = merge(self.grid[i])
            if old_grid != self.grid:
                self.new_tile()

        elif direction == 4:
            # right
            new_lis = [[self.grid[a][b]
                         for b in range(len(self.grid[0])-1,-1,-1)]
                       for a in range(len(self.grid))]
            old_grid = [[self.grid[a][b] for b in range(len(self.grid[0]))]
                         for a in range(len(self.grid))]

            for i in range(len(new_lis)):
                new_lis[i] = merge(new_lis[i])


            self.grid = [[new_lis[a][b]
                         for b in range(len(self.grid[0])-1,-1,-1)]
                       for a in range(len(self.grid))]
            if old_grid != self.grid:
                self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """

        lis_zeros = []
        for ran_row in range(len(self.grid)):
            for ran_col in range(len(self.grid[0])):
                if self.grid[ran_row][ran_col] == 0:
                    lis_zeros.append((ran_row,ran_col))

        try :
            pos = random.choice(lis_zeros)
            rand_in = random.choice([2,2,2,2,2,2,2,2,2,4])
            self.grid[pos[0]][pos[1]] = rand_in
        except :
            pass


    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 5))
