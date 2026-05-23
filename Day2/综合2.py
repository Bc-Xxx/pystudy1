import time

def log(func):
    def wrapper(*args, **kwargs):
        print(f"正在打开{func.__name__}")
        result = func(*args, **kwargs)
        print(f"执行{func.__name__}完毕")
        return result
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"时间{func.__name__},总耗时{end - start:0.4f}s")
        return result
    return wrapper

class BankAccount:
    def __init__(self, owner, account_number):
        self.owner = owner
        self.account_number = account_number
        self.__balance = 0.0

    @property
    def balance(self):
        return self.__balance

    @log
    @timer
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"存款{amount}成功,当前余额{self.__balance}")
        else:
            print("存款金额必须大于0")

    @log
    @timer
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"取款{amount}成功,当前余额{self.__balance}")
        else:
            print("余额不足")

class VIPBankAccount(BankAccount):
    def __init__(self, owner, account_number,vip_level=0):
        super().__init__(owner, account_number)
        self.vip_level = vip_level
        self.__bonus_points = 0
    def deposit(self, amount):
        # if amount > 0:
        #     self.__balance += amount
        #     if amount>=100:
        #         bonus_points=10*(amount/100)
        #     print(f"存款{amount}成功,当前余额{self.__balance},积分{bonus_points}")
        #     self.__bonus_points=bonus_points
        # else:
        #     print("存款金额必须大于0")
        super().deposit(amount)
        bonus_points = (amount/100)*10
        self.__bonus_points += bonus_points
        print(f"获得积分{bonus_points},当前积分{self.__bonus_points}")
    def use_bonus(self, points):
        if self.__bonus_points > 0:
            if points <= self.__bonus_points and points>0:
                vip_level = int(0+points/10)
                print(f"使用了{points}分，当前的VIP等级是{vip_level}")
                self.vip_level=int(vip_level)
            else:
                print("积分不足")
        else:
            print("当前没有积分")
    @property
    def show_vip_info(self):
        return self.vip_level


if __name__ == '__main__':
    # b = BankAccount("白菜","xxxx")
    # b.deposit(100)
    # b.withdraw(50)
    # b.withdraw(500)
    # print(f"当前余额{b.balance}")
    v=VIPBankAccount("白菜","xxxx")
    v.deposit(500)
    v.withdraw(50)
    v.use_bonus(30)

    print(f"当前的VIP等级是{v.show_vip_info}")
