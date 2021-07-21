import urllib.request as req
import bs4
def getData(url) :
    # url = "https://www.ptt.cc/bbs/Headphone/index3480.html"
    request = req.Request(url , headers={
        "cookie" : "over18=1", #自動加上cookies
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }) #要把網頁中 request headers 內的 user-agent 貼進來 
    #如此才可以裝成人類去連線
    with req.urlopen(request) as response : 
        data = response.read().decode("utf-8")
        # print(data)
    

    #data 就是取到的網頁原始碼
    root = bs4.BeautifulSoup(data , "html.parser") #beautifulSoup as html解析器的角色
    titles = root.find_all("div" , class_= "title") #找出所有是div標籤 且 class = "title"
    #注意是 class_ = "title" 不是 class_= "title"
    for title in titles :
        if title.a != None : #若標題內含a 表沒被刪除 要印出來
            print(title.a.string) #取title 內有 a 標籤的 string 部分
    
    next_URL = root.find("a" , string = "‹ 上頁" ) 
    # <a class="btn wide" href="/bbs/Headphone/index3480.html">‹ 上頁</a>
    complete_URL = 'https://www.ptt.cc' + next_URL["href"] #只取得 超連結的網址部分
    return complete_URL


#main
pageUrl = "https://www.ptt.cc/bbs/Headphone/index3480.html"
for i in range(3) :
#by recursive 持續傳入下一頁的URL
    print("page" + str(i+1) + "\n\n")
    pageUrl = getData(pageUrl)
