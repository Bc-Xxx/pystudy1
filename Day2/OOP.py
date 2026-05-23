# class Student:
#     def __init__(self, name, age, score):
#         self._name = name
#         self._age = age
#         self._score = score
#
#     @property
#     def name(self):
#         print(f"我叫{self._name}")
#
#     @property
#     def age(self):
#         print(f"我{self._age}岁")
#
#
# s=Student("白菜",23,40)
# print(s.name,s.age)

# class BankAccount:
#     def __init__(self, name, account_number, balance=0):
#         self._name = name
#         self._account_number = account_number
#         self._balance = balance
#
#     def a(self):
#         # return f"账户持有人:{self._name},账号:{self._account_number}"
#         print(f"账户持有人:{self._name},账号:{self._account_number}")
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"存款成功,当前余额：{self._balance}")
#         else:
#             print("存入的钱必须大于0")
#
#     def withdraw(self, amount):
#         if amount > 0 and self._balance >= amount:
#             self._balance -= amount
#             print(f"取款成功,当前余额：{self._balance}")
#         else:
#             print("取出的钱必须大于0且不能比存款多")
#
#
# b = BankAccount("张三", "ACC-123456", 1500.00)
# b.a()
# b.deposit(100)


class Book:
    total_books=0
    def __init__(self, title, author, isbn,status="可借"):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._status = status
        Book.total_books+=1

    def borrow(self):
        if self._status=="可借":
            self._status="已借出"
            return f"借出成功"
        else:
            print("已借出")

    def return_book(self):
        if self._status=="已借出":
            self._status="可借"
            return f"归还成功"
        else:
            print("无需归还")

    @property
    def info(self):
        return f"《{self._title}》 -  作者：{self._author} | ISBN:{self._isbn} | 状态: {self._status}"

    def __str__(self):
        return f"《{self._title}》 -  作者：{self._author} | ISBN:{self._isbn} | 状态: {self._status}"


b=Book("xxx","xxx","xxx","可借")
print(b)
print(b.info)
print(b.borrow())
print(b.borrow())
print(b.return_book())
print("当前图书总数：", Book.total_books)