
a = [2, 1, 5, 4, 3, 0, 0]

dip = None
for i in range(len(a) - 2, -1, -1):
    print(i)
    if a[i] < a[i + 1]:
        dip = i
        break

if dip is not None:
    for i in range(len(a) - 1, dip, -1):
        if a[i] > a[dip]:
            a[i], a[dip] = a[dip], a[i]
            break

a = a[:dip + 1] + a[dip + 1:][::-1]
print(a)



        
