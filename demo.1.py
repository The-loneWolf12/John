#导入必要的库
import requests
import time
from bs4 import BeautifulSoup

#语言状态码0是中文1是英文
languages_Statuscode = 0
#用来存储命令提示符
command_prompt = ">>>"
header = ""

if languages_Statuscode == 0:
    print("警告!用户不得使用本项目的爬虫功能进行违法操作！！！")
else:
    print("Warn! Users are not allowed to use the crawler function of this project to perform illegal operations!!")
#定义函数crawler()实现爬虫(功能未实现)(处理user-agent成功！！！)
def crawler():
    url = input("输入网页链接：")
    time.sleep(3)
    headers = {
        'user-agent': header
    }
    
    try:
        resp = requests.get(url, headers=headers, timeout=10)  # 设置超时时间
        resp.raise_for_status()  # 检查HTTP状态码，如果不是200，抛出HTTPError
        resp.encoding = 'utf-8'
        soup = BeautifulSoup(resp.text, "html.parser")
        print(soup)
        print('finish!!!')
    except requests.exceptions.RequestException as e:
        if languages_Statuscode == 0:
            print(f"网络请求失败：{e}")
        else:
            print(f"Request failed: {e}")
#定义函数AS()实现高级搜索(问题未解决)
def AS():
    user_need = input("高级搜索：")
    print("当看见'finish'后可打开当前目录下的html文件")
    url = f'https://www.baidu.com/s?q1={user_need}q2=&q3=&q4=&rn=10&lm=0&ct=0&ft=&q5=&q6=&tn=baiduadv'
    headers = {
        'user-agent':header
    }
    try:
        resp = requests.get(url,headers=headers,timeout=10) 
        resp.raise_for_status()
        resp.encoding = 'utf-8'
        file = open ('AS.html',mode='w',encoding='utf-8')
        file.write(resp.text)
        file.close()
        print("finish!")
    except:
        print("Error")
#程序主题主循环
while True:
    #命令提示符的传参
    user_input = input(command_prompt)
    #允许用户以exit指令退出程序
    if user_input == "":
        continue
    if user_input == "exit":
        break
    #允许用户以languages指令设置语言(中/英)文
    if user_input == "languages":
        languages = input("English/中文:")
        if languages == "English":
            languages_Statuscode = 1
            print("The programme language has been changed to English!!!")
            continue
        if languages == "中文":
            languages_Statuscode = 0
            print("程序以设置成中文语言")
            continue
    #允许用户以set up指令来设置命令提示符
    if user_input == "set up":
        if languages_Statuscode == 1:
            command_prompt = input("What do you want to set >>> to:")
            continue
        else:
            command_prompt = input("你想要将>>>设置成:")
            continue
    #允许用户使用crawler指令爬取网页源代码
    if user_input == "crawler":
        crawler()
        continue
    #允许用户以help指令查看所有功能
    if user_input == "help":
        if languages_Statuscode == 1:
            print("languages:You can set the language you want\nset up:You can set the command prompt\nexit:You can exit this program\nAS:You can use advanced search\ncrawler:You can use this feature to crawl page source code\nset up the user-agent\n" \
            "user-agent:Check after setting user-agent")
            continue
        else:
            print("languages:你可以设置你想要的语言\nset up:你可以设置命令提示符\nexit:你可以退出此程序\nAS:你可以使用高级搜索\ncrawler:你可以用这个功能来实现爬取页面源代码\nuser_A:设置user-agent\n" \
                  "user-agent:查看设置后的user-agent")
            continue
    #允许用户以AS指令进行系统内的高级搜索
    if user_input == "AS":
        if languages_Statuscode == 1:
            AS()
            print("Please open the html file in the current directory")
            continue
        else:
            AS()
            print("请打开当前目录下的html文件")
            continue
    #允许用户以user_A指令设置爬虫功能的反反爬
    if user_input == "user_A":
        user_agent =input("user-agent == ")
        header = user_agent
        continue
    #允许用户以user-agent指令来查看user-agent
    if user_input == "user-agent":
        print(header)
                                         
    #允许用户输错指令后可以从新输入
    else:
        if languages_Statuscode == 1:
            print("The instruction is invalid.")
        else:
            print("指令无效")