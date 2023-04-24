user = input("Write a number, BITCH! ")
user = int(user)
a = [1, 1, 2, 3, 5, 5, 5, 7, 6, 4, 8, 27, 37, 56, 78, 100]
x = []
for num in a:
    if num <= user:
        x.append(num)
print("List1:", x)

# x = [for num in a if num <=5 x.append(num)]
# print (x)
