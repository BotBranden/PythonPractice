user = input("Give me a number, U FOOL! ")
user = int(user)
numbers = range(1, user + 1)
a = []
for x in numbers:
    if user % x == 0:
        a.append(x)
print(a)
