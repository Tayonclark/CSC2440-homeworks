My_List = [2, 5, 3, 1, 4, 7, 6]
total = 0
count = 0
for number in My_List:
    if number % 2 ==0:
        total = total + number
        count = count + 1
Average_Even = total / count

My_List.sort()
My_List.reverse()
print(My_List)
print(Average_Even)