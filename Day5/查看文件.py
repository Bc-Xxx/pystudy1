from pathlib import Path
from datetime import datetime

def create_test_folder():
    test_dir=Path('test_files')
    test_dir.mkdir(exist_ok=True)
    print(f"测试文件夹{test_dir}")

def list_files():
    test_dir=Path('test_files')
    print(f"当前{test_dir}文件夹里的所有文件:\n")
    for file in test_dir.iterdir():
        if file.is_file():
            print(f"名称:{file.name},大小:{file.stat().st_size} 字节")

if __name__ == '__main__':
    create_test_folder()
    list_files()






