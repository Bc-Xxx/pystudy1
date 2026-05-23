class Person:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def introduce(self):
        print(f"我叫{self._name},{self._age}岁")

class Student(Person):
    def __init__(self,name,age,student_id,school):
        super().__init__(name,age)
        self._student_id=student_id
        self._school=school
    def introduce(self):
        super().introduce()
        print(f"我的学号是{self._student_id},来自{self._school}")
    def study(self,course):
        print(f"{self._name}正在学习{course}")

if __name__ == "__main__":
    p = Person("张三", 45)
    p.introduce()
    print(p)
    print("-" * 40)

    # 测试 Student
    s = Student("李四", 20,  "S2023001", "广东科技学院")
    s.introduce()
    s.study("Python 编程")
    print(s)
    print("-" * 40)