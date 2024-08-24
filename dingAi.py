import requests
import re
import json
import html
from bs4 import BeautifulSoup

def send_dingding_message(webhook, content, at_mobiles,person):
    headers = {
        'Content-Type': 'application/json'
    }

    at_text = ' '.join([f'@{mobile}' for mobile in at_mobiles])

    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": f"📢 新任务通知: {content}",
            "text": (
                f"### 📋 Hi {person} 您有一个马帮付款单待审核\n"
                f"**任务内容:**\n"
                f">#### {content} \n\n"
                f"**分配给:**\n"
                f"{at_text}\n\n"
                f"**请尽快处理!谢谢**\n"
                f"---\n"
                f"*来自系统自动通知*"
            ),
        },
        "at": {
            "atMobiles": at_mobiles,
            "isAtAll": False
        }
    }

    response = requests.post(webhook, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print('消息发送成功')
    else:
        print(f'消息发送失败，状态码: {response.status_code}')

webhook_url = 'https://oapi.dingtalk.com/robot/send?access_token=7d827cc4ff23dbe82b5af664a434aec175b8ea872b26d414de9daa028b4f783f'
url = "https://aamz.mabangerp.com/index.php?mod=finance.financenewsearch"
headers ={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
     'Cookie':'__bid_n=1917899898d1328afdb6cd; Hm_lvt_b888e3a9116ee926400397d5e2c3792b=1724305213,1724375603; HMACCOUNT=A1F0D42491118662; CRAWL_KANDENG_KEY=pgOdV0w3NJK88BQ6f4SoKxrYuH6n4HRDx3rCwbjzMwjIUzRw9Rc0j%2FdTqx2wzrZI0HZvHbMsPqNhkFE8eGukmA%3D%3D; MULTI_LANGUAGE_TYPE=%2BYjZ6oacL7xJ%2FKOcmBg9Z7cTOqi7UgOUgujRs4KQ4Ms%3D; lang=cn; signed=519679_79d58d7ab7e5c144e7d66069e08bf248; route=d53c39b2374e36594f1d99d6c3e32922; paymentrowsPerPage_519679=1000; PHPSESSID=3enceppgrlepkhn77cggu87mk2; Hm_lpvt_b888e3a9116ee926400397d5e2c3792b=1724461380; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221917899899b1bcb-0a6be0d10394f7-26001a51-3686400-1917899899c1125%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkxNzg5OTg5OWIxYmNiLTBhNmJlMGQxMDM5NGY3LTI2MDAxYTUxLTM2ODY0MDAtMTkxNzg5OTg5OWMxMTI1In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221917899899b1bcb-0a6be0d10394f7-26001a51-3686400-1917899899c1125%22%7D; MABANG_ERP_PRO_UNIQUE_ID=eyJlbXBsb3llZUlkIjoiNTE5Njc5Iiwic2VydmVyTmFtZSI6Ind3dy5tYWJhbmdlcnAuY29tIn0%3D; MABANG_ERP_PRO_MEMBERINFO_LOGIN_COOKIE=afcfa36e7d78f4c4736fa73207aac4b3; MABANG_ERP_PRO_MEMBERINFO_LOGIN_PLUS=lJQy55LJ7wfeXG61dhbSsSbXU5M0Kop%2FTuOU%2B63lxv5ody6EdXpuHjPppbcnOkli909%2FqszZSmnlaFIT81hpzJ3d3CVgoOMgIUKJXTUSoYI%3D'
}

response = requests.get(url, headers=headers)
data1 = response.content.decode()
data_dict = json.loads(data1)
text = data_dict['html']
soup = BeautifulSoup(text, 'html.parser')
getcheckFinLogList = "https://aamz.mabangerp.com/index.php?mod=finance.getcheckFinLogList"
Headers ={
    "Accept": "application/json, text/javascript, */*; q=0.01",
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Cookie':'__bid_n=1917899898d1328afdb6cd; Hm_lvt_b888e3a9116ee926400397d5e2c3792b=1724305213,1724375603; Hm_lpvt_b888e3a9116ee926400397d5e2c3792b=1724375603; HMACCOUNT=A1F0D42491118662; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221917899899b1bcb-0a6be0d10394f7-26001a51-3686400-1917899899c1125%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkxNzg5OTg5OWIxYmNiLTBhNmJlMGQxMDM5NGY3LTI2MDAxYTUxLTM2ODY0MDAtMTkxNzg5OTg5OWMxMTI1In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221917899899b1bcb-0a6be0d10394f7-26001a51-3686400-1917899899c1125%22%7D; MABANG_ERP_PRO_UNIQUE_ID=eyJlbXBsb3llZUlkIjoiNTE5Njc5Iiwic2VydmVyTmFtZSI6Ind3dy5tYWJhbmdlcnAuY29tIn0%3D; CRAWL_KANDENG_KEY=pgOdV0w3NJK88BQ6f4SoKxrYuH6n4HRDx3rCwbjzMwjIUzRw9Rc0j%2FdTqx2wzrZI0HZvHbMsPqNhkFE8eGukmA%3D%3D; MULTI_LANGUAGE_TYPE=%2BYjZ6oacL7xJ%2FKOcmBg9Z7cTOqi7UgOUgujRs4KQ4Ms%3D; lang=cn; PHPSESSID=k3gsv6l5vsblmenbp6qlh158m7; signed=519679_79d58d7ab7e5c144e7d66069e08bf248; MABANG_ERP_PRO_MEMBERINFO_LOGIN_COOKIE=afcfa36e7d78f4c4736fa73207aac4b3; MABANG_ERP_PRO_MEMBERINFO_LOGIN_PLUS=lJQy55LJ7wfeXG61dhbSsSbXU5M0Kop%2FTuOU%2B63lxv5ody6EdXpuHjPppbcnOkli909%2FqszZSmnlaFIT81hpzJ3d3CVgoOMgIUKJXTUSoYI%3D; route=d53c39b2374e36594f1d99d6c3e32922; paymentrowsPerPage_519679=10',
    "X-Requested-With": "XMLHttpRequest"
}

items_ul = soup.select('.li_content ul ')
# amount_money = soup.select('.Amount-money')
# print(amount_money)
# 发起 POST 请求
# 统计每个处理人的订单数量
order_counts = {
    "TankZhang": {"count": 0, "orders": [], "phone": "18734857039"},
    "VincenYang": {"count": 0, "orders": [], "phone": "15889953080"},
    "TieliangWang": {"count": 0, "orders": [], "phone": "13333575161"},
    "MichaelWong":{"count": 0, "orders": [], "phone": "18664719900"}
}

next_person = {
    "TankZhang": "VincenYang",
    "VincenYang": "TieliangWang",
    "TieliangWang": "MichaelWong",
    "AotyZhao": "TankZhang",
    "PallenCheng": "TankZhang"
}

for ul in items_ul:
    first_input = ul.select('li')[1]
    first_input = first_input.select_one('a span').text
    first_input = json.loads(first_input)

    if first_input["status"] == 1 and not first_input["orderNum"].startswith("FY"):
        id = first_input["id"]
        order_num = first_input["orderNum"]
        total_amount = first_input["totalAmount"]

        data = {
            "id": id
        }
        response = requests.post(getcheckFinLogList, headers=Headers, data=data)
        data = response.content.decode() 
        data = json.loads(data)
        
        if data["success"] == True:
            soup = BeautifulSoup(data["html"], 'html.parser')
            match = re.search(r'<td class="text-center" width="15%">(.*?)</td>', html.unescape(data.get("html", "")))
            
            if match:
                result = match.group(1).strip()
                # print(result)

                # 规则：如果配对到 TieliangWang 并且 totalAmount 大于 1000，增加 MichaelWong 的订单数量
                if result == "TieliangWang" and total_amount > 1000:
                    order_counts["MichaelWong"]["count"] += 1
                    order_counts["MichaelWong"]["orders"].append(order_num)
                elif result in next_person:
                    next_person_key = next_person[result]
                    order_counts[next_person_key]["count"] += 1
                    order_counts[next_person_key]["orders"].append(order_num)

# 输出结果并发送消息
for person, details in order_counts.items():
    if details["count"] > 0:
        orders = ', '.join(details["orders"])
        message = f"{person} 你有 {details['count']} 笔财务-付款单（待审核），订单编号：{orders}"
        print(message)
        send_dingding_message(webhook_url, message, [details["phone"]], person)
    else:
        print(f"{person} 0 笔订单需要处理")