import requests
import json


def send_dingding_message(webhook, content):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
    "msgtype": "link",
    "link": {
        "text": "测试在编程中，我们往往会遇到需要通过外部参数来控制脚本运行模式的情况，在通用的框架类代码中，这种情况尤为明显，因此，这里，我们来考察一下如何将参数传入到脚本文件中，而不是作为固定参数写死在脚本当中。",
        "title": "Python笔记：外部参数传入考察（一）argparse库",
        "picUrl": "",
        "messageUrl": "https://blog.csdn.net/codename_cys/article/details/107505718"
    }
}

    response = requests.post(webhook, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print('消息发送成功')
    else:
        print('消息发送失败')



# 替换为你自己的Webhook地址
webhook_url = 'https://oapi.dingtalk.com/robot/send?access_token=7d827cc4ff23dbe82b5af664a434aec175b8ea872b26d414de9daa028b4f783f'
# 替换为你想要发送的消息内容
message_content = 'c测试这是一条来自Python的钉钉机器人消息1111111'

send_dingding_message(webhook_url, message_content)