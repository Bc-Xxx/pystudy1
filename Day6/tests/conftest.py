import sys
from pathlib import Path

# 把 Day6 目录加入 sys.path，让 utils.* 能正常导入
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

