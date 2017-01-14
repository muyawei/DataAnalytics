scrapy 是 一个爬虫框架

start_urls 是一个url数组，相当于requests会请求里面所有url发送http请求
parser 是一个回调函数，每次完成一个请求之后都会返回调用一下该函数

scrapy runspider first_scrapy.py
运行一个scrapy项目


scrapy  startproject myproject 开始创建一个scrapy项目
默认有scrapy.cfg 和 myproject
cd myproject

__init__.py	middlewares.py	settings.py
items.py	pipelines.py	spiders

将所有的spider放入spiders，

scrapy crawl name

将实体放入items.py中
将数据的持久化放在pipelines.py中
=================================
scrapy 日志的5个等级
一般来说：
critical ：致命的。只能退出或者崩溃
error：错误 比warning严重，一般是程序不可自动恢复的错误
warning：程序出现错误的时候打印的日志（反应出的错误是比较小的错误，一般可以自动恢复）
info：程序运行时程序员关心的行为（提示一些信息）
debug：调试程序的日志（编写它进程序的调试）

scrapy crawl name --loglevel info logfile station.log

===========================
myproject 返回json数据
station   返回html页面
train     动态start_urls
===========================
scrapy  ---自动去重，根据url（相当于获取人的指纹）
        有些情况下不能正常工作
        程序需求不同
        wd=3&s=3 1)只求wd相同即去重
                 2）日期不同，把包括在URL中，被去重

        自定义去重

        ----断点续传    又一个文件记录请求到哪里

　