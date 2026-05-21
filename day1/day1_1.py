# def print_info(name, age=18, **kwargs):
#     print(f"姓名：{name}，年龄：{age}")
#     for k, v in kwargs.items():
#         print(f"{k}：{v}")
#
# print_info("小明", 20, 学校="广东科技学院", 专业="软件工程")

# def xinxi(name,age,*kwargs):
#     print(f"姓名:{name}，年龄:{age}")
#     print(kwargs)
#
#
# xinxi("小明",20,"身高1米八")
#
# def test(**kwargs):
#     print(kwargs)   # 先看看它长什么样
#
# test(名字="张三", 年龄=20, 城市="广州")
# 列表
# scores = [85, 92, 78, 65, 88]

# 字典
# student = {
#     "name": "栗白菜",
#     "age": 21,
#     "school": "广东科技学院",
#     "major": "软件工程"
# }
#
# print(student["name"])
# print(student.get("score", "暂无"))  # 安全获取方式

# a=[1,2,3,4,5]
# b=[s for s in a if s>2]
# print(b)
# scores = [85, 92, 78, 65, 88, 95, 72, 60]
# a=[s for s in scores if s>80 and s<95]
# print(a)
# names = ["alice", "bob", "charlie"]
# upper_names = [name.upper() for name in names]
# print(upper_names)  # ['ALICE', 'BOB', 'CHARLIE']

# names = ["ALICE", "BOB", "CHARLIE", "DAVID"]
# # 请将所有名字转成小写
# name1=[name.lower() for name in names]
# print(name1)
# squares = [x**3 for x in range(3)]
# print(squares)
# a=[i for i in range(1,20) if i%2==0]
# print(a)
# numbers = [2, 3, 4, 5, 6]
# # 请计算每个数的立方（x³）
# a=[i**3 for i in numbers]
# print(a)

# with open("day1.txt","w") as f:
#     f.write("你好")
#     f.close()
# with open("day1.txt","r") as f:
#     print(f.read())
# 写入文件
# with open("my_info.txt", "w", encoding="utf-8") as f:
#     f.write("姓名：栗白菜\n")
#     f.write("学校：广东科技学院\n")
#     f.write("当前进度：学到函数\n")

# with open("my_info.txt", "r", encoding="utf-8") as f:
#     # line1 = f.readline()  # 读第一行
#     line2 = f.readline()  # 读第二行
#     # print(line1, end="")
#     print(line2)
# with open("my_info.txt", "r", encoding="utf-8") as f:
#     for line in f:  # 逐行遍历
#         print(line, end="")  # end="" 避免多一个空行
with open("my_info.txt", "w", encoding="utf-8") as f:
    f.write("我比吴彦祖帅")