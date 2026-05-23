import time


# ==================== 装饰器 ====================
def log(func):
    def wrapper(*args, **kwargs):
        print(f"【日志】正在执行: {func.__name__}()")
        result = func(*args, **kwargs)
        print(f"【日志】{func.__name__}() 执行完毕")
        return result

    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"【计时】{func.__name__}() 耗时: {end - start:.4f} 秒")
        return result

    return wrapper


# ==================== 核心类 ====================
class BankAccount:
    def __init__(self, owner, account_number):
        self.owner = owner
        self.account_number = account_number
        self.__balance = 0.0

    @property
    def balance(self):
        """当前余额（只读属性）"""
        return self.__balance

    @log
    @timer
    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self.__balance += amount
            print(f"✅ 存款 {amount} 元成功！当前余额: {self.balance} 元")
        else:
            print("❌ 存款金额必须大于 0")

    @log
    @timer
    def withdraw(self, amount):
        """取款"""
        if amount <= 0:
            print("❌ 取款金额必须大于 0")
        elif amount > self.__balance:
            print(f"❌ 余额不足！当前余额: {self.balance} 元")
        else:
            self.__balance -= amount
            print(f"✅ 取款 {amount} 元成功！当前余额: {self.balance} 元")


# ==================== 测试 ====================
if __name__ == '__main__':
    b = BankAccount("白菜", "ACC-2026001")

    print(f"账户持有人: {b.owner}")
    b.deposit(1000)
    b.withdraw(300)
    b.withdraw(800)
    print(f"最终余额: {b.balance} 元")