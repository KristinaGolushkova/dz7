def sum_range(x, y):
    if x > y:
        x, y = y, x
    return sum(range(x, y+1))

print(sum_range(2, 25))
print(sum_range(204, 25))