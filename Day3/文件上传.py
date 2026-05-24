# import requests
# from pathlib import Path
#
# # 1. 先创建一个测试文件
# Path("test_data").mkdir(exist_ok=True)
#
# with open("test_data/upload_test.txt", "w",encoding="utf-8") as f:
#     f.write("这是栗白菜在 Day 3 练习上传的文件内容\n")
#     f.write("今天正在学习 requests 文件上传！")
#     print("test_data/upload_test.txt文件创建成功")
#
# # 2. 文件上传
# files={
#     'file': open("test_data/upload_test.txt",'rb')
# }
# response = requests.post("https://httpbin.org/post",files=files)
# print("\n状态码:", response.status_code)
# print("文件上传成功：",response.json()["files"].get("file")[:100]+"....")
#
# # 3. 关闭文件
# files["file"].close()


# import requests
# from pathlib import Path

# ==================== 练习 1：基础文件上传 ====================
# Path("test_data").mkdir(parents=True, exist_ok=True)
# with open("test_data/test1.txt", "w",encoding="utf-8") as f:
#     f.write("学生：栗白菜\n")
#     f.write("学校：广东科技学院\n")
#     f.write("日期：Day 3\n")
#     f.write("任务：requests 文件上传练习\n")
#
# files={
#     'file': open("test_data/test1.txt",'rb')
# }
# r=requests.post("https://httpbin.org/post",files=files)
# print("状态码：",r.status_code)
# print("文件上传成功，文件名:",list(r.json()["files"].keys())[0])
# files["file"].close()

# ==================== 练习 2：带 headers + json 数据 + 文件一起上传 ====================
# headers = {
#     "User-Agent": "BC-File-Upload-Test",
#     "Authorization": "Bearer student-upload-token"
# }
# data = {
#     "name": "栗白菜",
#     "task": "Day3练习",
#     "description": "同时上传文件和数据"
# }
# files2={
#     'file': open("test_data/test1.txt",'rb'),
#     'screenshot':('test.png', '这是模拟的图片内容', 'image/png')
# }
# r2=requests.post("https://httpbin.org/post",files=files2,headers=headers,data=data)
# print("状态码:", r2.status_code)
# print("服务器收到的数据:", r2.json()["form"])
# print("服务器收到的文件:", list(r2.json()["files"].keys()))
# files2['file'].close()

# ==================== 练习 3：封装成函数（推荐） ====================
import requests
from pathlib import Path

Path("test_data").mkdir(parents=True, exist_ok=True)
def upload_file(file_path,extra_data=None,timeout=10):
    try:
        if not Path(file_path).exists():
            with open(file_path, 'w',encoding="utf-8") as f:
                f.write("hello world beautiful today")
        with open(file_path,'rb') as f:
            files = {'file': f}
            response = requests.post(
                "https://httpbin.org/post",
                files=files,
                data=extra_data,
                timeout=timeout
            )
            response.raise_for_status()
            print("状态码:",response.status_code)
            print(f"文件{file_path}上传成功")
            print(response.json()["files"].get("file"))
            return response.json()
    except Exception as e:
        print("上传失败",e)
        return None

if __name__ == '__main__':
    upload_file("test_data/report.txt",{"student": "栗白菜", "day": 3},timeout=10)















