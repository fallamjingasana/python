def add(P,Q):
    return P +Q
def subtract(P,Q):
    return P-Q
def multiply(P,Q):
    return P*Q
def divide(P,Q):
    return P/Q

print("please select the opperation")
print("a. Add")
print("'b. subtract")
print("c.multiply" )
print("d, divide")

choice = input("please enter the first number")

num_1 = int(input("please enter the first number"))
num_2 = int(input("please enter the second number"))

if choice=="a":
    print("result",add(num_1,num_2))
elif choice=="b":
    print("result",subtract(num_1,num_2))

elif choice=="c":
    print("result",myultiply(num_1,num_2))
elif choice=="b":
    print("result",divide(num_1,num_2))
