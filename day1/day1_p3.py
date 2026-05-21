# import json
# def save_multiple_students(students_list):
#     with open('students.json', 'w', encoding='utf-8') as f:
#         json.dump(students_list, f, ensure_ascii=False, indent=4)
#
#     with open('students.json', 'r', encoding='utf-8') as f:
#         # data=json.load(f)
#         # print(data)
#         print(json.load(f))
#
#     print("已保存", len(students_list),"名学生信息")
#
# students = [
#     {"name": "白菜", "age": 19, "major": "软件工程"},
#     {"name": "小明", "age": 20, "major": "计算机"},
#     {"name": "小红", "age": 19, "major": "软件工程"}
# ]
# print(save_multiple_students(students))

import json
from pathlib import Path


def manage_student_records(operation, data=None):
    file_path = Path("students_records.json")

    if operation == "save":
        if data is None:
            print("❌ 没有提供要保存的数据")
            return

        with open("students_records.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"✅ 已成功保存 {len(data)} 名学生信息")

    elif operation == "load":
        try:
            with open("students_records.json", "r", encoding="utf-8") as f:
                loaded = json.load(f)
            print(f"✅ 成功加载 {len(loaded)} 名学生")
            return loaded

        except FileNotFoundError:
            print("⚠️ 文件不存在，返回空列表")
            return []
        except Exception as e:
            print("读取错误:", e)
            return []

    else:
        print("❌ 错误操作，请使用 'save' 或 'load'")
        return None


# ==================== 测试 ====================
students = [
    {"name": "白菜", "age": 19, "grade": "大三", "major": "软件工程"},
    {"name": "小红", "age": 20, "grade": "大三", "major": "软件工程"}
]

print("=== 第1次测试 ===")
manage_student_records("save", students)

print("\n=== 第2次测试 ===")
loaded = manage_student_records("load")
print(loaded)