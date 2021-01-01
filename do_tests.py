import random
import sys
from time import perf_counter

from naive_algorithm import NaiveAlgorithm
from cache_oblivious_algorithm import CacheObliviousAlgorithm


class Tester:
    def __init__(self, num_tests, matrix_size_start, matrix_size_stop, matrix_size_step):
        self.test_count = num_tests
        self.size_start = matrix_size_start
        self.size_stop = matrix_size_stop
        self.size_step = matrix_size_step

    def generate_test(self, size):
        return [[random.randint(0, 1000) for _ in range(size)] for _ in range(size)]

    def run(self):
        for size in range(self.size_start, self.size_stop + 1, self.size_step):
            time_naive, time_cache_oblivious = 0, 0
            for _ in range(self.test_count):
                test_matrix = self.generate_test(size)
                result_naive = self.time_measure(self.run_naive, test_matrix)
                result_cache_oblivious = self.time_measure(self.run_cache_oblivious, test_matrix)
                time_naive += result_naive
                time_cache_oblivious += result_cache_oblivious
            print(size, round(time_naive / self.test_count, 10), round(time_cache_oblivious / self.test_count, 10))

    def run_naive(self, test_matrix):
        return NaiveAlgorithm(test_matrix).transpose()

    def run_cache_oblivious(self, test_matrix):
        return CacheObliviousAlgorithm(test_matrix).transpose()

    def time_measure(self, run, data):
        start_time = perf_counter()
        run(data)
        return perf_counter() - start_time


if __name__ == '__main__':
    test_count = int(sys.argv[1])
    matrix_size_start = int(sys.argv[2])
    matrix_size_stop = int(sys.argv[3])
    matrix_size_step = int(sys.argv[4])
    Tester(test_count, matrix_size_start, matrix_size_stop, matrix_size_step).run()
