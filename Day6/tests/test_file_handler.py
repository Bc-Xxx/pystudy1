import pytest
import sys
from pathlib import Path

from utils.file_handler import create_test_files, read_text_file, count_files_in_dir


def test_create_test_files():
    files = create_test_files(count=3)
    assert len(files) == 3, f"应该创建3个文件，但实际返回{len(files)}个"
    for file_path in files:
        assert file_path.exists(), f"文件{file_path}已存在"
        assert file_path.suffix == ".txt"
    print("create_test_files测试已通过")


def test_read_text_file():
    # 创建测试文件
    files = create_test_files(count=2)
    # 测试正常读取
    content = read_text_file(str(files[0]))
    assert "这是第0个测试文件的内容" in content
    assert "第二行数据" in content
    # 测试文件不存在的情况
    with pytest.raises(FileNotFoundError):
        read_text_file("不存在的文件路径.txt")
    print("read_text_file 测试通过！")


def test_count_files_in_dir():
    # 先创建测试文件
    files = create_test_files(count=5)
    # 用创建文件所在目录来统计
    test_dir = str(files[0].parent)
    count = count_files_in_dir(test_dir, ".txt")
    assert count == 5, f"应该有5个文件，但统计到{count}个"
    # 测试目录不存在的情况
    count_not_exist = count_files_in_dir("不存在文件夹")
    assert count_not_exist == 0, "不存在的目录应该返回0"
    print("✅ count_files_in_dir 测试通过！")
