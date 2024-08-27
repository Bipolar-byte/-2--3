number = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

end = 0

while end < len(number):

    if number[end] < 0:
        break

    if number[end] > 0:
        print(number[end])

    end += 1
#print(number)

