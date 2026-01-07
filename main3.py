print("Enter your marks")
maths = int(input("maths"))
english = int(input("english"))
science = int(input("science"))
history = int(input("history"))

sum = maths + english + science +history
print("total marks:",sum)

percentage = (sum/400)*100
print("percentage",percentage)