dictionary = [
    {"V": "S001"}, 
    {"V":"S002"}, 
    {"VI":"S001"}, 
    {"VI": "S005"}, 
    {"VII": "S005"}, 
    {"V":"S009"}, 
    {"VIII":"S007"}
]
unique = {''}
unique.clear()
for item in dictionary:
    print(item)
    for temp in item:
        unique.add(f'{item[temp]}')        
print(unique)