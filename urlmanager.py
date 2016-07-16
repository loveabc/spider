#url管理器
class UrlManager():
    def __init__(self):
        self.__newurls=set()
        self.__oldurls=set()
    def __addurl(self,url):
        if url is None or url in self.__newurls or url in self.__oldurls:
            return None
        self.__newurls.add('http://baike.baidu.com'+url)
    def hasurl(self):
        return len(self.__newurls)
    def addurls(self,urls):
        if urls is None or len(urls)<=0:
            return None
        for url in urls:
            self.__addurl(url)
    def geturl(self):
        url=self.__newurls.pop()
        self.__oldurls.add(url)
        return url