class computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("selling price",self.__maxprice)
    def selfprice(self,price):
        self.__maxprice = price
c = computer()
c.sell()
c.__maxprice=1000
c.sell()
c.selfprice(1000)
c.sell()