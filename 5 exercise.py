import random

N = 100
c = []
d = []
otvet = []
for x in range(N):
    a = random.randint(0, N)
    c.append(a)
    b = random.randint(0, N)
    d.append(b)
for x in c:
    if x in d:
        otvet.append(x)
Answear = list(set(otvet))
print(" list 1", c, "\n", "list 2", d)
print(Answear)
