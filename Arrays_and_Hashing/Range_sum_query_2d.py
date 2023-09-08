class NumMatrix:
    def __init__(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        self.sumMap = [[0]* (cols+1) for r in range(rows+1)]

        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.sumMap[r][c+1]
                self.sumMap[r+1][c+1] = prefix + above



    def sumRegion(self, row1, row2, col1, col2):
        row1, row2, col1, col2 = row1+1, row2+1, col1+1, col2+1

        bottomRight = self.sumMap[row2][col2]
        above = self.sumMap[row1-1][col2]
        left = self.sumMap[row2][col1-1]
        topLeft = self.sumMap[row1-1][col1-1]

        return bottomRight - above-left +topLeft