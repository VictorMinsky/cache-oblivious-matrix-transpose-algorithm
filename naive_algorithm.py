from matrix import Matrix


class NaiveAlgorithm(Matrix):
    def transpose(self):
        self.temp_matrix = [[0] * self.n for _ in range(self.n)]
        for j in range(self.n):
            for i in range(self.n):
                self.temp_matrix[j][i] = self.matrix[i][j]
        self.matrix = self.temp_matrix
