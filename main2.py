s1 = [2,3,3]
s2 = {'a','b','c'}
s3= list(zip(s1,s2))
print(s3)
list1= [10,20,30,40]
list2=[100,200,300,400]
for x ,y in zip(list1,list2[::-1]):
    print(x,y)
stocks = ["apple","microsoft",'tcs']
prices= [2175,1123,768]
new_dict= {stocks: prices
for stocks,prices in zip(stocks,prices)}
print(new_dict)