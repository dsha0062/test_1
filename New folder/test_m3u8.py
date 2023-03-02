# python zhengze
import re
import json
# demo正则表达式
# line="{'method': 'Network.requestWillBeSent', 'params': {'documentURL': 'https://player.hanime.tv/?&', 'frameId': '848001D62A3EF237981578FB3691D9A0', 'hasUserGesture': False, 'initiator': {'stack': {'callFrames': [{'columnNumber': 2580, 'functionName': 'ii', 'lineNumber': 19, 'scriptId': '103', 'url': 'https://cdnjs.cloudflare.com/ajax/libs/video.js/7.20.2/alt/video.novtt.min.js'}, {'columnNumber': 391, 'functionName': 'ti', 'lineNumber': 19, 'scriptId': '103', 'url': 'https://cdnjs.cloudflare.com/ajax/libs/video.js/7.20.2/alt/video.novtt.min.js'}, {'columnNumber': 84467, 'functionName': 'a', 'lineNumber': 20, 'scriptId': '103', 'url': 'https://cdnjs.cloudflare.com/ajax/libs/video.js/7.20.2/alt/video.novtt.min.js'}, {'columnNumber': 119685, 'functionName': 't.start', 'lineNumber': 20, 'scriptId': '103', 'url': 'https://cdnjs.cloudflare.com/ajax/libs/video.js/7.20.2/alt/video.novtt.min.js'}, {'columnNumber': 119088, 'functionName': 't.load', 'lineNumber': 20, 'scriptId': '103', 'url': 'https://cdnjs.cloudflare.com/ajax/libs/video.js/7.20.2/alt/video.novtt.min.js'}, {'columnNumber': 9573, 'functionName': 'e', 'lineNumber': 24, 'scriptId': '103', 'url': 'https://cdnjs.cloudflare.com/ajax/libs/video.js/7.20.2/alt/video.novtt.min.js'}, {'columnNumber': 50858, 'functionName': 't.src', 'lineNumber': 24, 'scriptId': '103', 'url': 'https://cdnjs.cloudflare.com/ajax/libs/video.js/7.20.2/alt/video.novtt.min.js'}, {'columnNumber': 60325, 'functionName': 'handleSource', 'lineNumber': 24, 'scriptId': '103', 'url': 'https://cdnjs.cloudflare.com/ajax/libs/video.js/7.20.2/alt/video.novtt.min.js'}, {'columnNumber': 18228, 'functionName': 'r.setSource', 'lineNumber': 19, 'scriptId': '103', 'url': 'https://cdnjs.cloudflare.com/ajax/libs/video.js/7.20.2/alt/video.novtt.min.js'}, {'columnNumber': 139741, 'functionName': '', 'lineNumber': 19, 'scriptId': '103', 'url': 'https://cdnjs.cloudflare.com/ajax/libs/video.js/7.20.2/alt/video.novtt.min.js'}, {'columnNumber': 27217, 'functionName': 'e.ready', 'lineNumber': 11, 'scriptId': '103', 'url': 'https://cdnjs.cloudflare.com/ajax/libs/video.js/7.20.2/alt/video.novtt.min.js'}, {'columnNumber': 139551, 'functionName': 'e.techCall_', 'lineNumber': 19, 'scriptId': '103', 'url': 'https://cdnjs.cloudflare.com/ajax/libs/video.js/7.20.2/alt/video.novtt.min.js'}, {'columnNumber': 149811, 'functionName': '', 'lineNumber': 19, 'scriptId': '103', 'url': 'https://cdnjs.cloudflare.com/ajax/libs/video.js/7.20.2/alt/video.novtt.min.js'}, {'columnNumber': 27217, 'functionName': 'e.ready', 'lineNumber': 11, 'scriptId': '103', 'url': 'https://cdnjs.cloudflare.com/ajax/libs/video.js/7.20.2/alt/video.novtt.min.js'}, {'columnNumber': 149728, 'functionName': 'e.src_', 'lineNumber': 19, 'scriptId': '103', 'url': 'https://cdnjs.cloudflare.com/ajax/libs/video.js/7.20.2/alt/video.novtt.min.js'}, {'columnNumber': 148870, 'functionName': '', 'lineNumber': 19, 'scriptId': '103', 'url': 'https://cdnjs.cloudflare.com/ajax/libs/video.js/7.20.2/alt/video.novtt.min.js'}, {'columnNumber': 19124, 'functionName': 'i', 'lineNumber': 19, 'scriptId': '103', 'url': 'https://cdnjs.cloudflare.com/ajax/libs/video.js/7.20.2/alt/video.novtt.min.js'}, {'columnNumber': 19131, 'functionName': 'i', 'lineNumber': 19, 'scriptId': '103', 'url': 'https://cdnjs.cloudflare.com/ajax/libs/video.js/7.20.2/alt/video.novtt.min.js'}, {'columnNumber': 19153, 'functionName': '', 'lineNumber': 19, 'scriptId': '103', 'url': 'https://cdnjs.cloudflare.com/ajax/libs/video.js/7.20.2/alt/video.novtt.min.js'}, {'columnNumber': 30473, 'functionName': '', 'lineNumber': 11, 'scriptId': '103', 'url': 'https://cdnjs.cloudflare.com/ajax/libs/video.js/7.20.2/alt/video.novtt.min.js'}]}, 'type': 'script'}, 'loaderId': '5608E1BDE442F634CC1C74A462CA5D38', 'redirectHasExtraInfo': False, 'request': {'headers': {'Referer': '', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"'}, 'initialPriority': 'High', 'isSameSite': False, 'method': 'GET', 'mixedContentType': 'none', 'referrerPolicy': 'no-referrer', 'url': 'https://m3u8s.highwinds-cdn.com/api/v9/m3u8s/y3ngjplq4p5kkz32x0f5gccc42Zw9yd26d300A4mAvtfn51n3m1b1.m3u8'}, 'requestId': '3720.160', 'timestamp': 256020.903735, 'type': 'XHR', 'wallTime': 1676030989.182306}}"
def clean_url(line):
    
    line_s=line.split(',')
    for line_1 in line_s:
        pattern=re.compile(r'.*m3u8.*')
        result=pattern.search(line_1,re.I)
       
        if result:
            result_url=re.sub(r'[^a-zA-Z0-9/.:]','', result.group())
            result_url=result_url.replace('url:','')
            print(result_url)
            
            return result_url
        else:
            pass
   



def search_m3u8():
    m3u8line=[]
    with open('Request_h.json','r') as fp:
        lines=fp.read()
    lines=json.loads(lines)
    for line in lines:
        str_line=str(line)
        matchObj = re.search( r'M3u8', str_line, re.M|re.I)
        if matchObj:
            
            # print(line)
            m3u8_url=clean_url(str_line)
            # m3u8_url_1=str(m3u8_url)
            m3u8line.append(m3u8_url)
            
          
           
        else:
            print ("No match!!")
    
    print(m3u8line)
    return m3u8line
    

search_m3u8()