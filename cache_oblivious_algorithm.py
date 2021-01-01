from matrix import Matrix


class CacheObliviousAlgorithm(Matrix):
    def transpose_part(self, i, j, width, height):
        if width <= 80 and height <= 80:
            for x in range(i, i + height):
                for y in range(j, j + width):
                    self.temp_matrix[y][x] = self.matrix[x][y]
        elif width >= height:
            self.transpose_part(i, j, width // 2, height)
            self.transpose_part(i, j + width // 2, width - width // 2, height)
        else:
            self.transpose_part(i, j, width, height // 2)
            self.transpose_part(i + height // 2, j, width, height - height // 2)

    def transpose(self):
        self.temp_matrix = [[0] * self.n for _ in range(self.n)]
        self.transpose_part(0, 0, self.n, self.n)
        self.matrix = self.temp_matrix
