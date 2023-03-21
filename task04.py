source = [0, -1, 5, 2, 3, 5]

count = 0
idx = 0
while idx < len(source) - 1:
    idx += 1
    if source[idx - 1] < source[idx]:
        count += 1

print(count)