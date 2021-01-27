import matplotlib.pyplot as plt

file_in = open('results.txt', 'r', encoding='utf-8')
data = file_in.readlines()
size_data = [int(i.split()[0].strip()) for i in data]
naive_time_data = [float(i.split()[1].strip()) for i in data]
cache_oblivious_time_data = [float(i.split()[2].strip()) for i in data]

x1 = size_data
y1 = naive_time_data
plt.plot(x1, y1, label="Naive")
x2 = size_data
y2 = cache_oblivious_time_data
plt.plot(x2, y2, label="Cache oblivious")
plt.xlabel('Matrix size (n x n)')
plt.ylabel('Time, sec')
plt.title('Comparison of naive and cache oblivious matrix transposition algorithm')
plt.legend()
plt.savefig('graph.png')
plt.show()

