import pathlib
import pandas as pd

def 批量处理_excel(文件夹路径):
    """批量处理文件夹内所有 Excel 文件"""
    folder = pathlib.Path(文件夹路径)

    # 查找所有 .xlsx 文件
    excel_files = list(folder.glob('*.xlsx'))

    print(f"找到 {len(excel_files)} 个 Excel 文件，开始处理...\n")

    for file in excel_files:
        if file.name.startswith('~$'):  # 跳过 Excel 临时文件
            continue

        print(f"正在处理: {file.name}")

        # 读取文件
        df = pd.read_excel(file)

        # 处理数据
        df['总价'] = df['销量'] * df['单价']
        df = df[df['销量'] > 50]  # 筛选
        df = df.sort_values(by='总价', ascending=False)

        # 生成新文件名
        new_filename = f"处理后_{file.name}"
        output_path = folder / new_filename

        # 保存
        df.to_excel(output_path, index=False)

        # 美化
        # 美化_excel(str(output_path))

        print(f"✅ 处理完成: {new_filename}\n")


# 使用批量处理函数
批量处理_excel('Day4_Excel')  # '.' 表示当前文件夹