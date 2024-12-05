class computer:
    def __init__(self):
        self._maxprice = 9112
    def sell(self):
        print("The selling price is",self._maxprice)
    def setmaxprice(self,price):
        self._maxprice = price

c = computer()
c.sell()

c._maxprice = 9120
c.sell()

c.setmaxprice(9120)
c.sell()