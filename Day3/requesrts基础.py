# import requests
#
# # 最简单的GET请求
# response = requests.get("https://httpbin.org/get")
#
# print("请求成功！")
# print("状态码是：", response.status_code)

import requests

# params={
#     "name":"白菜",
#     "school":"广科",
#     "age":18
# }
# # 最简单的GET请求
# response = requests.get("https://httpbin.org/get",params=params)
#
# print("状态码是：", response.status_code)
# print("\n=== 返回的内容 ===")
# print(response.json())
# print(response.url)


# import requests
#
# print("=== 带参数的 GET 请求 ===")
#
# # 准备要发送的参数
# params = {
#     "name": "栗白菜",
#     "school": "广东科技学院",
#     "age": 20
# }
#
# # 发送带参数的请求
# response = requests.get("https://httpbin.org/get", params=params)
#
# print("状态码：", response.status_code)
# print("\n返回的内容：")
# print(response.json())





# import requests
# print("=== POST 请求提交数据 ===")
# data = {
#     "username": "栗白菜",
#     "school": "广东科技学院",
#     "status": "学习中",
#     "day": 3
# }
#
# # 发送 POST 请求
# response = requests.post("https://httpbin.org/post", json=data)
#
# print("状态码：", response.status_code)
# print("\n服务器返回的内容：")
# print(response.json())
# print(response.url)
#

#
# import requests
# print("=== GET vs POST 直观对比 ===")
# # GET - 查询
# r_get = requests.get("https://httpbin.org/get", params={"query": "今天天气"})
# print("GET 返回:", r_get.json()["args"])
#
# # POST - 提交
# r_post = requests.post("https://httpbin.org/post", json={"action": "提交学习记录", "day": 3})
# print("POST 返回:", r_post.json()["json"])
#
# print("\n✅ 理解 GET 和 POST 的区别了！")


#
# import requests
#
# print("=== GET 返回的完整结构 ===")
# r_get = requests.get("https://httpbin.org/get", params={"name": "栗白菜"})
# print(r_get.json())
#
# print("\n=== POST 返回的完整结构 ===")
# r_post = requests.post("https://httpbin.org/post", json={"name": "栗白菜"})
# print(r_post.json())



# import requests
# print("=== GET 和 POST 强化练习 ===")
# print("你的名字：栗白菜\n")
# # 1. GET 请求 - 查询
# print("1. GET 请求（查询）：")
# params = {
#     "name": "栗白菜",
#     "school": "广东科技学院",
#     "day": 3
# }
# r_get = requests.get("https://httpbin.org/get", params=params)
#
# print("状态码:", r_get.status_code)
# print("查询参数 args:", r_get.json()["args"])
# print("-" * 40)
#
# # 2. POST 请求 - 提交数据
# print("2. POST 请求（提交）：")
# data = {
#     "name": "栗白菜",
#     "action": "学习requests",
#     "progress": "第3天",
#     "feeling": "越来越懂了"
# }
# r_post = requests.post("https://httpbin.org/post", json=data)
#
# print("状态码:", r_post.status_code)
# print("提交的数据 json:", r_post.json()["json"])
# print("-" * 40)
# print("✅ 练习完成！")




import requests
print("=== 测试 POST 是否真正修改数据 ===")
data = {"name": "栗白菜", "time": "第一次提交"}
# 第1次 POST
r1 = requests.post("https://httpbin.org/post", json=data)
print("第一次提交后返回:", r1.json()["json"])

# 第2次 POST（换个内容）
data2 = {"name": "栗白菜", "time": "第二次提交"}
r2 = requests.post("https://httpbin.org/post", json=data2)
print("第二次提交后返回:", r2.json()["json"])

# 第3次再 GET 看看
r_get = requests.get("https://httpbin.org/get")
print("用 GET 查询时，有没有之前的提交记录？", r_get.json()["args"])






