# -*- coding: utf8 -*-
import requests, time
import random
cookie='这里替换为自己的ck'
mHeader={
    'User-Agent':'Mozilla/5.0 (Linux; Android 10; Redmi K20 Pro Premium Edition Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/045811 Mobile Safari/537.36 MMWEBID/2118 MicroMessenger/8.0.15.2020(0x28000F31) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
    'Referer':'https://txwk.10010.com/',
    'Cookie':cookie
}

def complite(mission_id):
    url=f'https://kapi.10010.com/kcard-5th-anniversary/outer/mission/complete?mission_id={mission_id}'
    res=requests.get(url,headers=mHeader).json()
    return res['message']

def task():
    url='https://kapi.10010.com/kcard-5th-anniversary/outer/mission/query-mission-info'
    res=requests.get(url,headers=mHeader).json()
    print(res['message'])
    if res['code']=='0000':
        for info in res['data']['mission_info']:
            if info['status']==3:
                print(f'{info["mission_name"]}:此任务已完成')
            else:
                print(f'{info["mission_name"]}:{complite(info["mission_id"])}')
                delay=random.randint(5,15)            
                time.sleep(delay)

task()
