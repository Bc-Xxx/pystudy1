import pytest

@pytest.mark.skip(reason="当前功能还未开发完成")
def test_future_feature():
    """这个测试会被跳过"""
    assert False

def test_temp_file(temp_txt_file):
    assert temp_txt_file.exists(), f"文件应该存在，但路径是: {temp_txt_file}"
    content = temp_txt_file.read_text(encoding="utf-8")
    print(f"\n文件内容是：{content}\n")
    assert "hello world beautiful" in content
    assert len(content)>10
    print("✅ 所有测试断言都通过！")

def test_use_temp_file_again(temp_txt_file):
    assert temp_txt_file.exists()
    content = temp_txt_file.read_text(encoding="utf-8")
    print(f"\n文件内容是：{content}\n")
    assert "hello world beautiful" in content
    assert "第二行" in content
    print("✅ 第二个测试通过！")

def test_user_data(text_user_data):
    assert text_user_data["username"] == "testuser"
    assert text_user_data["age"]>18
    assert "python" in text_user_data["tags"]
    print("用户数据内容：", text_user_data)
    print("✅ 用户数据测试通过！")


@pytest.mark.parametrize("a,b,expectde",[
    (1, 2, 3),
    (0, 0, 0),
    (-5, 3, -2),
    (100, -50, 50),
    (2.5, 3.5, 6.0),
],ids=["正数相加", "零相加", "正负相加", "大数相加", "小数相加"])
def test_add(a,b,expectde):
    assert a + b == expectde
    print(f"✅ {a} + {b} = {a+b}")

@pytest.mark.smoke
def test_different_file_types(temp_file_by_type):
    assert temp_file_by_type.exists()
    content = temp_file_by_type.read_text(encoding="utf-8")
    print(f"文件类型测试内容: {content[:50]}...")
    assert len(content)>5










