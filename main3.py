import array  as arr
arr_num = arr.array('i',[1,2,3,4,3,5,3])
print("original array", str(arr_num))
print("number of times occurence of the number 3 in the said array",str(arr_num.count(3)))
arr_num.reverse()
print("Reverse the order of the items:")
print(str(arr_num))