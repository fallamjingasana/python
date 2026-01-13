actualcost = float(input("please enter the actual cost"))

salescost = float(input("please input the sales cost"))
if(salescost>actualcost):
    amount = salescost-actualcost
    print("total profit",amount)
else:
    print("no profit")