num = input("please enter a numbers")
length = len(num)
if length>=4:
    mid1_length = length//2-1
    mid_2length = length//2

    mid1=int(num[mid1_length])
    mid=int(num[mid2_length])

    product = mid1*mid_2length
    print("product",product)
else:
    print("invalid input")