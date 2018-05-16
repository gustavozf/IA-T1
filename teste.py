import statistics

x = [1, 2, 3, 4]
y = [-100, -200, -300, -400]

print(
    statistics.pstdev([i/sum(x) for i in x]),
    statistics.pstdev([i/sum(y) for i in y]))
