# import requests
#
# params={
#     "_limit":3
# }
#
# r=requests.get("https://jsonplaceholder.typicode.com/posts",params=params)
#
# print("状态码：",r.status_code)
# print(r.json())
# print(r.url)
import json

# import requests
#
# data={
#     "title":"我的第一篇博客",
#     "内容":"今天学习了 GET 和 POST 的区别",
#     "UserID":99
# }
# r = requests.post("https://jsonplaceholder.typicode.com/posts",json=data)
# print("状态码：",r.status_code)
# print(r.json())
#


# import requests
#
# headers={
#     "fake_token" : "github_pat_faje_token"
# }
#
# params={
#     "user":"白菜"
# }
#
# r=requests.get('https://api.github.com/user',headers=headers,params=params)
# print("状态码：",r.status_code)
# print(r.json())




# import requests
# headers={
#     "Content-Type": "application/json"
# }
# data={
#     "name": "张三",
#     "age": 25
# }
# r = requests.post('https://httpbin.org/post',headers=headers,json=data)
# print("状态码：",r.status_code)
# print(r.json()["json"])


# import requests
# headers={
#     "fake_token" : "github_pat_faje_token",
#     "Content-Type": "application/json"
# }
# params={
#     "q":"python"
# }
# r = requests.get('https://api.github.com/search/repositories',headers=headers,params=params)
# print("状态码：",r.status_code)
# print(r.json()["items"][0]["full_name"])
# data = r.json()  # 将返回的 JSON 数据保存到变量 data 中
# first_repo = data["items"][0]  # 从 items 列表中取出第一个仓库（索引为 0）
#
# # 然后按要求打印
# print("第一个仓库的全名:", first_repo["full_name"])
# print("第一个仓库的URL:", first_repo["html_url"])




import requests
print("=== Session vs 普通 requests 真实区别对比 ===\n")
# ==================== 1. 不用 Session ====================
print("1. 不使用 Session（每次都是独立的）：")
response1 = requests.get("https://httpbin.org/cookies")
print("第一次请求 cookies:", response1.json()["cookies"])

# 第二次请求（不会记住任何状态）
response2 = requests.get("https://httpbin.org/cookies")
print("第二次请求 cookies:", response2.json()["cookies"])

print("-" * 50)

# ==================== 2. 使用 Session ====================
print("2. 使用 Session（会记住状态）：")
session = requests.Session()

# 第一次请求时设置一个 cookie
session.get("https://httpbin.org/cookies/set?student=栗白菜&day=3")

# 第二次请求（Session 会自动带上刚才的 cookie）
r = session.get("https://httpbin.org/cookies")
print("使用 Session 后的 cookies:", r.json()["cookies"])

print("\n✅ 看到了吗？Session 能自动记住 cookie！")
