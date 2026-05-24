import pandas as pd

df = pd.read_excel("Day4_Excel//销售数据.xlsx")
# print("=== 前5行数据 ===")
# print(df.head())
print("\n=== 完整数据 ===")
print(df)
# print("\n=== 数据信息 ===")
# print(df.info())
print("\n=== 查找 ===")
# print(df["商品"])
# print(df["销量"])

# 2. 计算新的一列：总价 = 销量 * 单价
df['总价']=df["销量"]*df["单价"]
print("\n添加总价后：")
print(df)

# 3. 筛选：只保留销量大于50的数据
df_filtered=df[df["销量"]>30]
print("\n筛选后（销量>30）：")
print(df_filtered)

# 4. 按总价从高到低排序
df_sorted = df_filtered.sort_values(by='总价', ascending=False)
print("\n按总价降序排序后：")
print(df_sorted)

# 5. 保存到新的 Excel 文件
df_sorted.to_excel('Day4_Excel/处理后的销售数据.xlsx',sheet_name='销售总价排名', index=False)
# print("\n✅ 处理完成！已保存为：Day4_Excel/处理后的销售数据.xlsx")
# ================== 小练习 ==================
# 1. 只保存筛选后的数据
df_filtered.to_excel('Day4_Excel/只筛选销量大于50.xlsx', index=False)

# 2. 保存时带上日期
import datetime
today = datetime.date.today().strftime('%Y-%m-%d')
df_sorted.to_excel(f'Day4_Excel/销售报告_{today}.xlsx', index=False)

print("✅ 额外保存了2个文件！")

# ================== 第五步：美化 Excel ==================
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment












