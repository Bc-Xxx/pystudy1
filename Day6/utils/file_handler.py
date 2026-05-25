from pathlib import Path
from typing import List


def create_test_files(count: int = 3) -> List[str]:
    # 1. 创建测试文件夹
    test_dir = Path('test_files')
    test_dir.mkdir(exist_ok=True)
    create_files = []
    # 2. 循环创建多个测试文件
    for i in range(count):  # count默认等于3，循环执行3次
        file_path = test_dir / f'{i}.txt'
        # 3. 写入内容到文件
        content = f"这是第{i}个测试文件的内容。\n这是第二行数据。\n文件编号:{i}"
        file_path.write_text(content, encoding='utf-8')
        create_files.append(file_path)
    print(f"成功创建{count}个测试文件,保存在{test_dir}文件夹中")
    return create_files


def read_text_file(file_path: str) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"文件不存在:{file_path}")
    return path.read_text(encoding='utf-8')


def count_files_in_dir(directory: str = "test_files", suffix: str = ".txt") -> int:
    path = Path(directory)
    if not path.exists():
        return 0
    files = list(path.glob(f"*{suffix}"))
    return len(files)
