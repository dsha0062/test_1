import json
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import by
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
import time
import test_m3u8
caps = {
    "browserName": "chrome",
    'goog:loggingPrefs': {'performance': 'ALL'}  # 开启日志性能监听
}

options = Options()
# options.add_experimental_option("detach", True)
options.add_argument('-ignore-certificate-errors')
options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
options.add_argument('-ignore -ssl-errors')
# options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
# options.add_experimental_option("excludeSwitches", ['enable-automation'])
# options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")  # 指定端口为9527
browser = webdriver.Chrome(desired_capabilities=caps, options=options)  # 启动浏览器
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """})
str_url=input("input url:")
browser.get(str_url)  # 访问该url
time.sleep(10)
browser.find_element(by.By.XPATH,"//div[@class='play-btn flex justify-center align-center']").click()
# //div[@class='title-views flex column']//h1[@class='tv-title']
    # 'application/javascript', 'application/x-javascript', 'text/css', 'webp', 'image/png', 'image/gif',
        # 'image/jpeg', 'image/x-icon', 'application/octet-stream'
# def filter_type(_type: str):
#     types = [
    

#     ]
#     if _type not in types:
#         return True
#     return False
message_list=[]
time.sleep(20)
performance_log = browser.get_log('performance')  # 获取名称为 performance 的日志

print("loading")
for packet in performance_log:
    
    message = json.loads(packet.get('message')).get('message') 
    # 获取message的数据
    
    # if message.get('method') != 'Network.responseReceived':  # 如果method 不是 responseReceived 类型就不往下执行
    #     continue
    # packet_type = message.get('params').get('response').get('mimeType')  # 获取该请求返回的type
    # # if not filter_type(_type=packet_type):  # 过滤type
    # # if packet_type!='XHR':
    # #     continue
    bigtype= message.get('params').get('type')
    if bigtype!='XHR':
            continue
    requestId = message.get('params').get('requestId')  # 唯一的请求标识符。相当于该请求的身份证
    # url = message.get('params').get('response').get('url')  # 获取 该请求  url
    try:
        resp = browser.execute_cdp_cmd('Network.getResponseBody', {'requestId': requestId})  # selenium调用 cdp
        # response_body = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': requestId}
        print(f'type: {bigtype}') 
        message_list.append(message) 
        # )url: {url} /n')
        # print(f'response: {resp}/n')
        # print()
    except WebDriverException:  # 忽略异常
        pass
with open('Request_h.json','w') as fp:
        json.dump(message_list,fp,ensure_ascii=False)
        fp.close()
print("delete or not y/n")
y_n=input("please input:")
try:
    if(y_n=="y"or y_n=="Y"):
        with open('Request_h.json','w') as fp:
            fp.write(" ")
            fp.close()
            print("Already delete")
    elif(y_n=="n" or y_n=="N" ):
        print("saved")
except IOError:
    print("error:please input y or n")
m3u8_url=[]
m3u8_url=test_m3u8.search_m3u8()
# print(m3u8_url[-1])
print(m3u8_url)
header={
'authority': 'm3u8s.highwinds-cdn.com',
# 'method' : 'GET'
# 'path': /api/v9/m3u8s/pc06vt4dcxx5n4tr7clxy0k8wqZflnx4c3949nyjh4gxmnggm7nzq.m3u8
# :scheme: https
# accept: */*



'origin': 'https://player.hanime.tv',



'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'cross-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'

}
x=browser.get(m3u8_url[-1],header=header).text()
print(x)

