k = int(input('Укажите сдвиг: '))
values = [1,2,3,4,5]
length = len(values)
k = k % length
print(values)
print(values[-k:] + values[:-k])