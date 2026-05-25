# from pathlib import Path
# from datetime import datetime
#
# def create_test_files:
#     test_dir=Path("test_files")
#     test_dir.mkdir(exist_ok=True)
#     print(f"文件夹{test_dir}存在")
#
#     files=[
#         "报告.pdf", "照片1.jpg", "笔记.txt", "代码.py",
#         "合同.docx", "风景.png", "数据.xlsx", "脚本2.py"
#     ]
#     for filename in files:
#         file_path=test_dir/filename
#         file_path.write_text(f"这是{filename}文件，创建时间是{datetime.now()}")
#         print(f"已创建文件{filename}")
#
# def organize_by_type():
#     test_dir=Path("test_files")
#     if not test_dir.exists():
#         print("文件不存在")
#         return
#     print("\n开始整理文件")
#
#     # 创建分类文件夹
#     categories={
#         '文档': ['.pdf', '.docx', '.txt', '.md', '.xlsx'],
#         '图片': ['.jpg', '.jpeg', '.png', '.gif'],
#         '代码': ['.py', '.js', '.java', '.html']
#     }
#     for catname in categories.keys():
#         (test_dir/catname).mkdir(exist_ok=True)
#
#     # 移动文件
#     for file in test_dir.iterdir():
#         if file.is_dir():
#             moved=False
#             suffix=file.suffix.lower()  # 获取后缀，如 .pdf
#
#             for catname,exts in categories.items():   # .items是返回字典的所有键值对
#                 if exts in exts:
#                     target_folder=test_dir/catname
#                     target_path=target_folder/file.name
#
#                     # 如果目标位置已有同名文件，添加数字后缀
#                     if target_path.exists():
#                         stem = file.stem
#                         new_name = f"{stem}_1{file.suffix}"
#                         target_path = target_folder / new_name
#
#                     file.rename(target_path)
#                     print(f"   📁 移动 {file.name} → {cat_name}/")
#                     moved = True
#                     break
#
#                 if not moved:
#                     print(f"   ❓ 未分类: {file.name}")
#
#                 def show_structure():
#                     """显示整理后的文件夹结构"""
#                     print("\n📊 整理后的文件夹结构：")
#                     for item in Path("test_files").iterdir():
#                         if item.is_dir():
#                             print(f"📁 {item.name}/")
#                             for f in item.iterdir():
#                                 print(f"   └─ {f.name}")
#
# if __name__ == "__main__":
#     create_test_files()
#     organize_by_type()
#     show_structure()
#     print("\n🎉 第四步完成！你已经学会了批量整理文件！")
#
#
#
# day5_test.py
# 第5天：文件操作 - 第四步 按类型整理

from pathlib import Path
from datetime import datetime


def create_test_files():
    """创建不同类型的测试文件"""
    test_dir = Path("test_files")
    test_dir.mkdir(exist_ok=True)

    # 不同类型的文件
    files = [
        "报告.pdf", "照片1.jpg", "笔记.txt", "代码.py",
        "合同.docx", "风景.png", "数据.xlsx", "脚本2.py"
    ]

    for filename in files:
        file_path = test_dir / filename
        file_path.write_text(f"这是 {filename} 的测试内容\n创建时间: {datetime.now()}")
        print(f"✅ 创建文件: {filename}")


def organize_by_type():
    """按文件类型整理"""
    source = Path("test_files")
    if not source.exists():
        print("❌ 测试文件夹不存在")
        return

    print("\n🚀 开始按类型整理文件...")

    # 1. 创建分类文件夹
    categories = {
        '文档': ['.pdf', '.docx', '.txt', '.md', '.xlsx'],
        '图片': ['.jpg', '.jpeg', '.png', '.gif'],
        '代码': ['.py', '.js', '.java', '.html']
    }

    for cat_name in categories.keys():
        (source / cat_name).mkdir(exist_ok=True)

    # 2. 移动文件
    for file in source.iterdir():
        if file.is_file():  # 只处理文件
            moved = False
            suffix = file.suffix.lower()  # 获取后缀，如 .pdf

            for cat_name, exts in categories.items():
                if suffix in exts:
                    target_folder = source / cat_name
                    target_path = target_folder / file.name

                    # 如果目标位置已有同名文件，添加数字后缀
                    if target_path.exists():
                        stem = file.stem
                        new_name = f"{stem}_1{file.suffix}"
                        target_path = target_folder / new_name

                    file.rename(target_path)
                    print(f"   📁 移动 {file.name} → {cat_name}/")
                    moved = True
                    break

            if not moved:
                print(f"   ❓ 未分类: {file.name}")


def show_structure():
    """显示整理后的文件夹结构"""
    print("\n📊 整理后的文件夹结构：")
    for item in Path("test_files").iterdir():
        if item.is_dir():
            print(f"📁 {item.name}/")
            for f in item.iterdir():
                print(f"   └─ {f.name}")


if __name__ == "__main__":
    create_test_files()
    organize_by_type()
    show_structure()
    print("\n🎉 第四步完成！你已经学会了批量整理文件！")