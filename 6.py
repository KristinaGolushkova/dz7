def custom_range(start, end, step=0):
    if start > end:
        start, end = end, start
    line = [start]
    while start < end:
        start += step
        line.append(start)
    return line

print(custom_range(77, 55, 2))

