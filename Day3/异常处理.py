# import requests
# from requests.exceptions import Timeout, ConnectionError, RequestException
#
# print("=== 异常处理 + 超时设置 ===")
#
# # 推荐写法：带超时 + 异常处理
# url = "https://httpbin.org/get"
#
# try:
#     # timeout=5 表示最多等5秒
#     response = requests.get(url, params={"name": "栗白菜"}, timeout=5)
#
#     # 检查状态码
#     response.raise_for_status()  # 如果不是 2xx 状态码就抛异常
#
#     print("请求成功！状态码:", response.status_code)
#     print("返回数据:", response.json()["args"])
#
# except Timeout:
#     print("❌ 请求超时了！")
# except ConnectionError:
#     print("❌ 网络连接失败！")
# except RequestException as e:
#     print("❌ 请求出错:", e)
# except Exception as e:
#     print("❌ 其他错误:", e)



import requests
from requests.exceptions import Timeout, ConnectionError,RequestException

# 练习 1：正常请求 + 超时设置
# try:
#     r = requests.get('http://www.baidu.com',params={"name":"白菜"},timeout=5)
#     r.raise_for_status()
#     print("状态码：",r.status_code)
# except Exception as e:
#     print("出错了",e)
#
# # 练习 2：故意超时（测试异常捕捉）
# try:
#     r1 = requests.get('https://httpbin.org/delay/3',timeout=1)
#     r1.raise_for_status()
#     print("状态码：",r1.status_code)
# except Timeout:
#     print("超时异常")
# except Exception as e:
#     print("其他异常",e)

# 练习 3：综合练习（推荐重点练这个）
def safe_request(url,params=None,headers=None,timeout=5):
    try:
        r2 = requests.get(url,params=params,timeout=timeout)
        r2.raise_for_status()
        print("状态码:",r2.status_code)
        print(f"✅ 请求成功！返回 args:{r2.json()["args"]}")
        return r2.json()
    except Timeout:
        print("请求超时")
    except ConnectionError:
        print("网络链接失败")
    except RequestException as e:
        print("请求异常",e)
    except Exception as e:
        print("未知错误:",e)
    return None

if __name__ == '__main__':
    s=safe_request("https://httpbin.org/get", {"test": "综合练习"},{"Content-Type": "application/json"},timeout=5)
    s=safe_request("https://httpbin.org/delay/3", {"test": "综合练习"},timeout=1)



