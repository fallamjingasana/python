l = [2,5,6,3,9,4]
print("print original list:",l)
count = 0
for i in l:
    count+=i
avg = count/len(l)
print("sum =",count)
print("average",avg)
l.sort()
print(l[0])
print(l[-1])
