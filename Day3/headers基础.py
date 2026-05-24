# import requests
#
# print("=== Headers 请求头练习 ===")
#
# # 自定义请求头
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",  # 伪装浏览器
#     "Accept": "application/json",
#     "Authorization": "Bearer your-token-here"   # 后面会经常用到
# }
#
# # 发送带 headers 的 GET 请求
# response = requests.get("https://httpbin.org/headers", headers=headers)
#
# print("状态码:", response.status_code)
# print("\n服务器收到的 Headers:")
# print(response.json()["headers"])


# import requests
#
# print("=== 带 Headers 的 POST 请求 ===")
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Python Learning)",
#     "Authorization": "Bearer my-test-token-123",
#     "Content-Type": "application/json"
# }
#
# data = {
#     "name": "栗白菜",
#     "action": "提交带headers的POST"
# }
#
# response = requests.post(
#     "https://httpbin.org/post",
#     headers=headers,
#     json=data
# )
#
# print("状态码:", response.status_code)
# print("\n服务器收到的 Headers:")
# print(response.json()["headers"])
#
# print("\n服务器收到的数据:")
# print(response.json()["json"])


# 模拟登录（最重要的一种用法）
# import requests
# print("=== 示例2：模拟带 Token 的登录请求 ===")
# headers = {
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.fake-token-123456",  # 模拟登录令牌
#     "User-Agent": "Python-Requests-Learning"
# }
#
# data = {"action": "提交测试报告", "result": "通过"}
#
# response = requests.post(
#     "https://httpbin.org/post",
#     headers=headers,
#     json=data
# )
#
# print("状态码:", response.status_code)
# print("\nAuthorization 是否成功发送:")
# print("Authorization:", response.json()["headers"].get("Authorization"))


# 多个 Headers 一起用（完整版）
import requests
print("=== 示例3：完整 Headers POST ===")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json",
    "Authorization": "Bearer student-token-2026",
    "X-Student-ID": "2023001",          # 自定义 Header
    "Content-Type": "application/json"
}
payload = {
    "name": "栗白菜",
    "progress": "正在学习 requests",
    "day": 3,
    "feeling": "慢慢理解了"
}
r = requests.post("https://httpbin.org/post", headers=headers, json=payload)

print("✅ 请求成功！状态码:", r.status_code)
print("\n部分 Headers 返回:")
print("User-Agent:", r.json()["headers"].get("User-Agent"))
print("Authorization:", r.json()["headers"].get("Authorization"))