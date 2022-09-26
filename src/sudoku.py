import random

class SudokuSolver:
    MAX_STARTING_VALUES = 27
    MIN_STARTING_VALUES = 23
    dim = 3
    colored = 0
    g = {}

    def __init__(self, game=None):
        self.colors = [0]*self.dim**4
        self.available = [False]*self.dim**4
        self.mkgraph()
        if game:
            self.read_game(game)

    def get_col(self, position):
        """
                its column is the rest of the division of the el by the dim**2
        """
        return position % (self.dim**2)

    def get_row(self, position):
        """
                its row is the quotient of the division of the el by the dim**2
        """
        return int(position/(self.dim**2))

    def get_grid(self, row, col):
        """
                To know in witch grid a cell at position (row, col) is, we need to represent grids
                in format of a plane with (x, y), its x is the rest of row by dim and y is the rest of col by dim
                then we save its value in the polinomial for mapping to only 1 dimension
        """

        return int(row/self.dim)*self.dim + int(col/self.dim)

    def mkgraph(self):
        rows, cols, grids = [], [], []
        dim = 3

        for i in range(dim**2):
            rows.append([])
            cols.append([])
            grids.append([])

        for i in range(dim**4):
            row = self.get_row(i)
            col = self.get_col(i)
            grid = self.get_grid(row, col)

            cols[col] += [i]
            rows[row] += [i]
            grids[grid] += [i]

        for i in range(dim**4):
            row = self.get_row(i)
            col = self.get_col(i)
            grid = self.get_grid(row, col)
            # we get all cells in the same row, col and grid to create the graph (the comparable cells are its conections)
            self.g[i] = list(set(rows[row] + cols[col] + grids[grid]) - set([i])) # set for removing duplicates
    
    def create_game(self, inplace=False):
        n_starting_values = int(random.randrange(
            self.MIN_STARTING_VALUES, self.MAX_STARTING_VALUES+1))
        r = [-1]*(self.dim**4)

        for _ in range(n_starting_values):
            while True:
                val = int(random.randrange(1, self.dim**2 + 1))
                cell = int(random.randrange(0, self.dim**4))

                adj = self.g[cell]

                if r[cell] <= 0 and val not in [r[x] for x in adj]:
                    r[cell] = val
                    break
        
        if inplace: self.read_game(r)
        return r
                    

    

    # read a game in list format and create the solver
    def read_game(self, game):
        for i, val in enumerate(game):

            # if it has no value, then pass
            if val == -1:
                continue
            
            # if it has a value, set it as not available and the color of it
            self.available[i] = True
            self.colors[i] = int(val)
            self.colored += 1

    # return the neighbors of a vertex
    def neighbors(self, vertex):
        neighboors = set([])

        for u in self.g[vertex]:
            if self.colors[u] > 0:
                neighboors = neighboors.union({self.colors[u]})
            
        return neighboors
    
    # returns the first free vertex
    def first_free(self):
        for v, color in enumerate(self.colors):
            if color == 0:
                return v
        
        return -1
    
    def color(self):
        if self.colored >= self.dim**4:
            return [self.colors*1]
        
        v = self.first_free()

        # if there is no free vertex, we dont have a solution
        if v == -1:
            return []

        legal_colors = set(range(1,10)).difference(self.neighbors(v))

        # if the free vertex cant have any colors, then we have no solution
        if len(legal_colors) == 0:
            return []

        self.colored += 1
        solutions = []

        for color in legal_colors:
            self.colors[v] = color

            new_solution = self.color()

            solutions += new_solution
        
        self.colors[v] = 0
        self.colored -= 1

        return solutions
    def get_game(self, game):
        s = ""
        for i in range(self.dim**2):

            if i % self.dim == 0 and i != 0:
                s += '-'*(2*(self.dim**2) + 2*self.dim)
                s += '\n'

            for j in range(self.dim**2):
                if game[(self.dim**2)*i + j] == -1:
                    s+= "  "
                else:
                    s += " {}".format(game[(self.dim**2)*i + j])

                if j % self.dim == (self.dim - 1) and j != (self.dim**2 - 1):
                    s += " |"

            s += '\n'
        
        return s

    def get_solutions(self, solutions):
        s = ""
        for k, solution in enumerate(solutions):
            s += 'Solution #{}: \n\n'.format(k)

            s += self.get_game(solution)
            
            s += '\n\n\n'

        if s == "":
            return "No solution :("

        return s

