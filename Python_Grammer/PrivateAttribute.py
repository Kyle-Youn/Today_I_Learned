class PayGildong:
    def __init__(self):
        self.day =25
        self.__money = 100000
        
    def changeMoney(self, money):
        self.__money = money

    def getMoney(self):
        return self.__money
    

gildong = PayGildong()
# print(gildong.__money)    # 오류
print(gildong.getMoney())
