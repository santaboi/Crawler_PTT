import urllib.request as req
url = "https://www.kkday.com/zh-tw/home/ajax_get_homepage_setting?csrf_token_name=3920adad9bbb6cc6e18f56b721b1de77"
request = req.Request(url , headers={
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}) #要把網頁中 request headers 內的 user-agent 貼進來 
#如此才可以裝成人類去連線
with req.urlopen(request) as response : 
    data = response.read().decode("utf-8")
    # print(data)  此時是取得的是JSON 的資料

import json
#不用data.replace() kkday 沒有怪格式
data = json.loads(data) #注意是loads 不是 load
homepage_product = data["data"]["homepage_product_group"] #JSON dict 的格式 用key 去access 得到product_dict 的 list
product_list2 = data["data"]["top_products"]["prod_list"] 

print("homepage product:")
for key in homepage_product : #key 是dict
    print(key["title"])
print("\n")

print("product list:")
for key in product_list2 :
    print(key["name"])