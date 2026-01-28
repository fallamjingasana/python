string = input("please enter your string")
char = input("enter your character")
I = 0
count = 0
while(I< len(string)):
    if(string[I]==char):
        count= count + 1
    I = I+1
print(count)

