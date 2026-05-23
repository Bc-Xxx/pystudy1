# def decorator(f):      # f是旧函数
#     def new():         # new是新函数
#         print("附加")  # 加东西
#         f()            # 用旧函数
#     return new         # 返回新函数
#
# @decorator
# def hello():
#     print("世界")
#
# hello()

# def timer(func):           # func 就是下面被装饰的 slow_add
#     def wrapper(a, b):     # wrapper 接收调用时的参数
#         print("开始计时...")
#         result = func(a, b)   # ← 这里真正调用 slow_add(a, b)
#         print("计时结束")
#         return result
#     return wrapper
#
#
# @timer
# def slow_add(x, y):
#     return x + y
#
# #
# slow_add(3, 5)   # 执行时，实际是调用 wrapper(3,5)

# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"【日志】开始调用 → {func.__name__}()")
#         result = func(*args, **kwargs)
#         print(f"【日志】调用结束 ← {func.__name__}(), 返回值: {result}")
#         return result
#     return wrapper
#
#
# @log
# def say_hello(name):
#     # print(f'Hello {name}')
#     return
#
#
# say_hello("张三")

import time
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         run=end-start
#         print(f"函数 {func.__name__}() 执行完成")
#         print(f"耗时: {run:.4f} 秒")
#         return result
#     return wrapper
# @timer
# def test(a):
#     print("测试函数开始执行")
#     time.sleep(a)
#     print("测试函数执行完毕")
#
# if __name__ == '__main__':
#     test(1)

def repeat(times=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result=None
            for i in range(times):
                print(f"第{i+1}/{times}次执行{func.__name__}()")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello {name}")
    return f"问候完成 {name}"

if __name__ == "__main__":
    greet("白菜")


