lower = int(input("enter a upper range"))
upper = int(input("enter a lower number"))
print("Prime numbers between",lower,"and",upper,"áre")
for num in range(lower,upper +1):
    if num > 1:
        for i in range(2,num):
            if (num%i)==0:
                break
            else:
                print(num)
