a = list(range(10))

# print(a[0])
for i in range(10):
    # print(i)
    # print(a[i])
    a[i] = 9 - i
for i in range(10):
    a[i] = a[a[i]]

for i in range(10):
    print(a[i])
