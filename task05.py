str1 = "a a a b c a a d c d d"


def twin_counter(str1):
    str1 = str1.split(" ")
    temp = []

    for i in range(len(str1)):
        counter = 0
        for j in str1[:i]:
            if str1[i] == j:
                counter += 1
        if counter > 0:
            counter = f'_{counter}'
        else:
            counter = ''

        temp.append(f"{str1[i]}{counter}")

    print(temp)


twin_counter(str1)