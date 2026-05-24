import requests

url="https://httpbin.org/"
# ==================== 练习 1：GET + params ====================
params={
    "name": "栗白菜",
    "school": "广东科技学院",
    "progress": "Day 3"
}
r1=requests.get(url+"get",params=params)
print("状态码:", r1.status_code)
print(r1.json()["args"])

# ==================== 练习 2：POST + headers ====================
data={
    "action": "提交学习记录",
    "day": 3,
    "feeling": "越来越熟悉了"
}
headers={
    "User-Agent": "Python-Student-Learning",
    "Authorization": "Bearer student-2026-token",
    "X-Request-Source": "Day3-Practice"
}
r2=requests.post(url+"post",headers=headers,json=data)
print("状态码:", r2.status_code)
print(r2.json()["json"])
print(r2.json()["headers"].get("Authorization"))

# ==================== 练习 3：使用 Session ====================
session=requests.Session()
session.headers.update({
    "User-Agent": "Session-Test",
    "Authorization": "Bearer session-token-abc"
})
data1={
    "test": "session练习"
}
r3=session.get(url+"get")
r4=session.post(url+"post",json=data1)
print("Session GET 状态码:", r3.status_code)
print("Session POST 返回 json:", r4.json()["json"])

# ==================== 练习 4：综合小任务（自己改） ====================
print("练习 4：综合练习（请修改下面内容）")
your_session = requests.Session()
your_session.headers.update({
    "User-Agent": "mypretect",
    "X-Student": "gk"
})
your_data = {
    "name": "栗白菜",
    "task": "完成Day3练习",
    "time": "现在"
}
r=your_session.get(url+"get")
print(r.status_code)
print(r.json())
rr=your_session.post(url+"post",json=your_data)
print(rr.status_code)
print(rr.json()["json"])





