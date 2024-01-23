def regression_line(x, y):
    return round((sum(y) - (len(x) * sum(i * j for i, j in zip(x, y)) - sum(x) * sum(y)) / (len(x) * sum(i**2 for i in x) - sum(x)**2) * sum(x)) / len(x)
, 4), round((len(x) * sum(i * j for i, j in zip(x, y)) - sum(x) * sum(y)) / (len(x) * sum(i**2 for i in x) - sum(x)**2), 4)