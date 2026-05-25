import pytest
import os
from pathlib import Path

# @pytest.fixture
# def temp_file():
#     file_path=Path("temp_test.txt")
#     file_path.write_text("Hello World", encoding="utf-8")
#
#     yield file_path
#     if file_path.exists():
#         file_path.unlink()

@pytest.fixture(scope="module")
def temp_txt_file():
    path=Path("temp_test.txt")
    path.write_text("hello world beautiful\n这是第二行内容\n第三行测试数据", encoding="utf-8")
    print(f"临时测试文件{path.name}已创建")

    yield path

    if path.is_file():
        path.unlink()
        print(f"临时测试文件{path.name}已清理")


@pytest.fixture()
def text_user_data():
    data = {
        "username": "testuser",
        "age": 25,
        "email": "test@example.com",
        "tags": ["python", "pytest"]
    }
    print("✅ 用户测试数据已准备")
    return data

@pytest.fixture(params=["txt","json","csv"])
def temp_file_by_type(request):
    file_type=request.param
    path=Path(f"temp_test. {file_type}")

    if file_type=="json":
        import json
        data={"name": "pytest", "version": "进阶测试"}
        path.write_text(json.dumps(data,ensure_ascii=False,indent=2), encoding="utf-8")
    else:
        path.write_text(f"这是{file_type}测试文件", encoding="utf-8")

    yield path
    if path.exists():
        path.unlink()
