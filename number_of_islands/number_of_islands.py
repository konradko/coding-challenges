class NumberOfIslands:
    TO_VISIT = "1"
    VISITED = "0"

    def __init__(self, grid: list[list[str]]):
        self.grid = grid
        self.grid_height = len(grid)
        self.grid_width = len(grid[0])

    def visit_cell(self, row: int, column: int):
        """
        Depth First Search during which each visited node is set to VISITED

        Args:
            row (int): Grid row index
            column (int): Grid column index
        """
        if (
            row < 0
            or column < 0
            or row >= self.grid_height
            or column >= self.grid_width
            or self.grid[row][column] != self.TO_VISIT
        ):
            return

        self.grid[row][column] = self.VISITED

        self.visit_cell_neighbours(row, column)

    def visit_cell_neighbours(self, row: int, column: int):
        """
        Depth First Search during which every visited node is set to VISITED

        Args:
            row (int): Grid row index
            column (int): Grid column index
        """
        # Visit cell above
        self.visit_cell(row - 1, column)
        # Below
        self.visit_cell(row + 1, column)
        # Left
        self.visit_cell(row, column - 1)
        # Right
        self.visit_cell(row, column + 1)

    def get_number_of_islands(self) -> int:
        """
        Performs linear scan of the grid. If a cell contains TO_VISIT, then it is a root node
        that triggers a Depth First Search. Number of root nodes is the number of islands.

        Returns:
            int: Number of islands in the grid
        """
        number_of_islands = 0

        for row in range(self.grid_height):
            for column in range(self.grid_width):
                if self.grid[row][column] == self.TO_VISIT:
                    # Visit all cells in this island
                    # and increment island count
                    self.visit_cell(row, column)
                    number_of_islands += 1

        return number_of_islands
