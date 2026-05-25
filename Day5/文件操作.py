from pathlib import Path
from datetime import datetime

# def create_test_folder():
#     test_dir=Path("test_files")
#     test_dir.mkdir(exist_ok=True)
#     print(f"文件创建成功:{test_dir}")
#
#     for i in range(1,6):
#         file_path=test_dir/f"{i}.txt"
#         file_path.write_text(f"这是第{i}个测试文件的内容\n创建时间: {datetime.now()}",encoding="utf-8")
#         print(f"   创建文件：{file_path.name}")
#
# if __name__ == "__main__":
#     create_test_folder()
#     print("\n🎉 第一段代码运行完成！")


def create_fill():
    test_file=Path("test_files")
    test_file.mkdir(exist_ok=True)
    print(f"文件夹{test_file}创建成功")

    file_create=[
        ("报告1.pdf", "这是第一份PDF报告的内容"),
        ("报告2.pdf", "这是第二份PDF报告的内容"),
        ("照片1.jpg", "模拟图片数据：照片1"),
        ("照片2.jpg", "模拟图片数据：照片2"),
        ("笔记.txt", "这是文本笔记内容\n记录一些重要事项"),
        ("代码练习.py", "print('Hello, Python!')\n\n# 这是一个Python练习文件"),
        ("数据1.csv", "name,age,city\n张三,25,北京\n李四,30,上海"),
        ("数据2.xlsx", "模拟Excel数据（实际是文本）"),
        ("合同.doc", "这是合同文档的内容\n甲方：XXX\n乙方：XXX"),
        ("图片备份.png", "模拟图片数据：备份图片")
    ]
    # 创建文件
    for filename,contect in file_create:
        file_path=test_file/filename
        file_path.write_text(contect,encoding="utf-8")
        print(f"文件{filename}创建成功")
    # 创建文件夹
    # categories = ["文档类", "图片类", "数据类"]
    # for category in categories:
    #     create_dir=test_file/category
    #     create_dir.mkdir(exist_ok=True)
    #     print(f"创建文件夹{category}成功")

if __name__ == "__main__":
    create_fill()











