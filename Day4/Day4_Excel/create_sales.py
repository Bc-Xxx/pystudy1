from openpyxl import Workbook
import random
from datetime import date, timedelta

wb = Workbook()
ws = wb.active
ws.title = "销售数据"

# 表头
ws.append(["商品", "销量", "单价", "日期"])

# 随机商品数据
products = [
    ("苹果", 5, 8),
    ("香蕉", 3, 12),
    ("牛奶", 6.5, 45),
    ("面包", 8, 23),
    ("鸡蛋", 1.2, 18),
    ("洗衣液", 25, 31),
]

base_date = date(2026, 5, 20)
for i, (name, price, qty) in enumerate(products):
    d = base_date + timedelta(days=i)
    sales = round(price * qty, 2)
    ws.append([name, qty, price, d.strftime("%Y-%m-%d")])

wb.save("销售数据.xlsx")
print("销售数据.xlsx 生成成功！")
