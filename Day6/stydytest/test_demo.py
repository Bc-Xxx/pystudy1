import pytest

# def add(a,b):
#     return a+b
# # def test_add_positive():
# #     assert add(1,2) == 3
# # def test_add_negative():
# #     assert add(-1,-2) == -3
# # def test_add_zero():
# #     assert add(0,0) == 0
# @pytest.mark.parametrize("a,b,expected",[
#     (1,2,3),
#     (-1, 5, 4),
#     (0, 0, 0),
#     (100, -50, 50),
# ])
# def test_add_param(a,b,expected):
#     assert expected == a + b


# def string_processor(text, operation):
#     if operation == 'upper':
#         q=text.upper()
#         return q
#     elif operation == 'lower':
#         q=text.lower()
#         return q
#     elif operation == 'reverse':
#         q=text[::-1]
#         return q
#     elif operation == 'strip':
#         q=text.strip()
#         return q
#     else:
#         raise ValueError("请输入正确的操作类型")
#
# # 你的参数化测试
# @pytest.mark.parametrize("test,operation,expected",[
#     ("hello", "upper", "HELLO"),  # 输入hello，upper后应为HELLO
#     ("WORLD", "lower", "world"),  # 输入WORLD，lower后应为world
#     ("abc", "reverse", "cba"),  # 输入abc，reverse后应为cba
#     ("  hi  ", "strip", "hi"),  # 输入"  hi  "，strip后应为"hi"
#     ("", "upper", ""),  # 边界：空字符串
#     ("   ", "strip", ""),  # 边界：纯空格
# ])
# def test_string_processor(test,operation,expected):
#     assert string_processor(test,operation)==expected
#
# # 异常测试（额外挑战）
# def test_string_processor_invalid_operation():
#     with pytest.raises(ValueError):  # 期望抛出ValueError
#         string_processor("test", "invalid_op")