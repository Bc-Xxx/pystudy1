# def filter_students(students):
#     d3_students=[s for s in students if s.get("grade")=="大三"]
#     return d3_students
#
# all_students = [
#     {"name": "白菜", "grade": "大三", "major": "软件工程"},
#     {"name": "小明", "grade": "大二", "major": "计算机"},
#     {"name": "小红", "grade": "大三", "major": "软件工程"},
#     {"name": "小刚", "grade": "大一", "major": "网络工程"}
# ]
#
# print(filter_students(all_students))

# def a_score(scores):
#     avg=sum(scores)/len(scores)
#     max_score=max(scores)
#     return avg,max_score
#
# score=[1,2,3,4,5,6,7,8,9]
# avg,max_score=a_score(score)
# print(avg,max_score)

# numbers = [1, 5, 8, -3, 10, -7, 12]
# z_numbers=[n for n in numbers if n>0]
# print(z_numbers)
# x_numbers=[n**2 for n in numbers if n>0]
# print(x_numbers)
# c_numbers=[n for n in numbers if n%2==0]
# print(c_numbers)
# modified = [x if x % 2 == 0 else -1 for x in numbers]
# print(modified)

# def process_scores(students):
#     for s in students:
#         name = s['name']
#         avg=sum(s['scores'])/len(s['scores'])
#     passed=[s for s in students if s['score']>=60]
#
#
#
#
# data = [
#     {"name": "白菜", "scores": [85, 78, 92]},
#     {"name": "小明", "scores": [55, 65, 48]},
#     {"name": "小红", "scores": [90, 95, 88]}
# ]
# print(process_scores(data))

def analyze_class_scores(class_data):
    student_b = [b for b in class_data if b["grade"] == "大三"]

    average_scores = []
    total_d3_students = 0
    excellent_count = 0
    for c in student_b:
        name = c["name"]
        avg = sum(c["scores"]) / len(c["scores"])
        average_scores.append({
            "name": name,
            "avg": avg
        })

        total_d3_students += 1

        if avg >= 80:
            excellent_count += 1

    return {
        "total_d3_students": total_d3_students,
        "excellent_count": excellent_count,
        "average_scores":average_scores
    }


class_data = [
    {"name": "白菜", "scores": [85, 78, 92, 65], "grade": "大三"},
    {"name": "小明", "scores": [70, 75, 68, 72], "grade": "大二"},
    {"name": "小红", "scores": [90, 88, 95, 85], "grade": "大三"},
    {"name": "小刚", "scores": [60, 55, 65, 58], "grade": "大三"},
    {"name": "小美", "scores": [82, 87, 80, 84], "grade": "大三"}
]

print(analyze_class_scores(class_data))
