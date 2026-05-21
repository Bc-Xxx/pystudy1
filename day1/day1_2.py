import json

data = {
    "name": "白菜",
    "时间": "第一天",
    "内容": ["基础语法", "函数", "列表推导式"]
}

# with open("learning.json","w",encoding="utf-8") as f:
#     json.dump(data,f,ensure_ascii=False,indent=4)

with open("learning.json", "r", encoding="utf-8") as f:
    loaded=json.load(f)

print(loaded["内容"])
print(loaded)
