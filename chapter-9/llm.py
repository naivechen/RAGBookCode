# 代码 9-5

import requests
import json
from similarity import get_top_k

#修改成自己的api key和secret key
API_KEY = "<YOUR_API_KEY>"
SECRET_KEY = "<YOUR_SECRET_KEY>"
 
 
def get_response(context_str, query):

    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/llama_3_8b?access_token=" + get_access_token()
#注意message必须是奇数条
    
    message  = f"""
        基于以下已知信息，简洁和专业的来回答用户的问题。
        如果无法从中得到答案，请说 "根据已知信息无法回答该问题" 或 "没有提供足够的相关信息"，不允许在答案中添加编造成分，答案请使用中文。

        已知内容:
        {context_str}

        问题:
        {query}"""
    
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content":  message
                
            }
            #,
            #{
            #    "role": "assistant",
            #    "content": "你好，有什么我可以帮助你的吗？"
            #}
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
 
    response = requests.request("POST", url, headers=headers, data=payload)
    # print(response.text)
    response = json.loads( response.text)['result']
    print("response: ", response)


 
 
def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))
 

# 读取所有的 chunk 数据
page_len = 15
data = []
for i in range(page_len):
    with open(f"chunk/{i}.txt", "r", encoding="utf-8") as fr:
        readlines = fr.readlines()
        for line in readlines:
            data.append(line)
# query
query = "现金流量为净流入是多少？"
ret = get_top_k(K=3, data=data, query=query)
print(ret)
context_str = ""
for item in ret:
    context_str += item['text']
print("text: ", context_str)
get_response(context_str, query)

