
# encoding: utf-8
import requests
import json

def ding_push_message():
    # 构建请求头部
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
 
    # 构建请求数据
    message = {
        "msgtype": "text",
        "text": {
            "content": msg
        },
        "at": {
            "isAtAll": False
        }
    }
 
    # 对请求的数据进行json封装
    message_json = json.dumps(message)
    # 发送请求
    info = requests.post(url=web_url, data=message_json, headers=header)
    # 打印返回的结果
 
if __name__ == "__main__":
    # 请求的URL，WebHook地址
    web_url = "https://oapi.dingtalk.com/robot/send?access_token=6fd9c129a0c441ce6752db5ae10340f0cbd8f60a86d823f7fa553f41c1ecdc27"
    # 构建请求数据
    msg = "消息：吃饭啦"
 
    ding_push_message()
