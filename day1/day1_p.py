# import json
#
# def save_student_info(name,age,school,major):
#     student_data={
#         "name":name,
#         "age":age,
#         "school":school,
#         "major":major
#     }
#     with open("student.json","w",encoding="utf-8") as f:
#         json.dump(student_data,f,ensure_ascii=False,indent=4)
#
#     with open("student.json","r",encoding="utf-8") as f:
#         data=json.load(f)
#
#     print(data)
#
# save_student_info("白菜",19,"广科","python")
import json


def save_student_info(name, age, school, major):
    """保存学生信息到 JSON 文件"""
    student_data = {
        "name": name,
        "age": age,
        "school": school,
        "major": major
    }

    # 写入文件
    with open("student.json", "w", encoding="utf-8") as f:
        json.dump(student_data, f, ensure_ascii=False, indent=4)

    print("✅ 学生信息已保存到 student.json")


# 调用
save_student_info("白菜", 19, "广科", "软件工程")