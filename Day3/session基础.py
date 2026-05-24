import requests

print("=== Session vs 普通 requests 对比 ===\n")

url_get = "https://httpbin.org/get"
url_cookies = "https://httpbin.org/cookies"

# ============================================================
#  没有 Session：每次都是陌生人
# ============================================================
print("=" * 50)
print("【没有 Session】每次都要自己带东西")
print("=" * 50)

# 第1次请求：要自己带 headers
r1 = requests.get(url_get, headers={"X-Token": "my_token_123", "User-Agent": "MyApp/1.0"})
print("第1次请求 headers:", r1.json()["headers"]["X-Token"])

# 第2次请求：headers 还要再写一遍（requests 不会帮你记住）
r2 = requests.get(url_get, headers={"X-Token": "my_token_123", "User-Agent": "MyApp/1.0"})
print("第2次请求 headers:", r2.json()["headers"]["X-Token"])
print("→ 每次都要重复写 headers，麻烦！\n")

# Cookie 的问题：第1次拿到 Cookie，第2次带不上去
r3 = requests.get(url_cookies + "?name=baicai")
print("第1次服务器设置的 Cookie:", r3.json())
r4 = requests.get(url_cookies)
print("第2次带过去的 Cookie:", r4.json())
print("→ Cookie 没记住，第2次是空的！\n")

# ============================================================
#  有 Session：自动记住一切
# ============================================================
print("=" * 50)
print("【有 Session】设一次，后面自动带上")
print("=" * 50)

session = requests.Session()

# 设置一次默认 headers，后面所有请求都自动带上
session.headers.update({
    "X-Token": "my_token_123",
    "User-Agent": "MyApp/1.0"
})

# 第1次请求：不用写 headers，自动带上
r5 = session.get(url_get)
print("第1次请求 headers:", r5.json()["headers"]["X-Token"])

# 第2次请求：还是不用写，自动带上
r6 = session.get(url_get)
print("第2次请求 headers:", r6.json()["headers"]["X-Token"])
print("→ 不用重复写 headers，省事！\n")

# Cookie：Session 自动记住
r7 = session.get(url_cookies + "?name=baicai")
print("第1次服务器设置的 Cookie:", r7.json())
r8 = session.get(url_cookies)
print("第2次带过去的 Cookie:", r8.json())
print("→ Cookie 自动记住了！\n")

# ============================================================
#  总结
# ============================================================
print("=" * 50)
print("总结对比")
print("=" * 50)
print("""
|          | 没 Session（每次新请求） | 有 Session（会话保持） |
|----------|------------------------|----------------------|
| Headers  | 每次手动写             | 设一次，自动带上      |
| Cookie   | 不会记住，下次丢失     | 自动记住，自动传递    |
| 连接     | 每次重新建立           | 复用连接，更快        |
| 适用场景 | 简单的单次请求         | 登录、连续操作        |
""")
