#爬取百度百科
#这是一个调度器
from com.imooc.baike.urlmanager import UrlManager
from com.imooc.baike.parser import Parser
from com.imooc.baike.downloader import Downloader
from com.imooc.baike.contentout import Outputer
import time
class Spider():
    def __init__(self):
        self.data=[]
        self.urlmanager=UrlManager()
        self.parser=Parser()
        self.downloader=Downloader()
        self.outputer=Outputer()
        self.__count=1
        self.__part=1
    def caw(self,urls):
        startTime=time.time()
        self.urlmanager.addurls(urls)
        while self.urlmanager.hasurl():
            try:
                print(self.__count)
                url=self.urlmanager.geturl()
                content=self.downloader.download(url)#爬取内容
                title,text,urls=self.parser.parse(content)#解析内容
                self.data.append((title,url,text))
                self.urlmanager.addurls(urls)
                if self.__count%25==0:#没获得25条数据,就往硬盘中写入一批,避免数据量太大,耗尽内存
                    self.outputer.output(self.data,self.__part)
                    self.data=[]
                    self.__part+=1
                if self.__count==500:#总共盘区500条数据
                    break
                self.__count+=1
            except:
                print('fail')
        endTime=time.time()
        print('爬取'+str(self.__count)+'条百度百科共耗时'+str(endTime-startTime)+'秒')
if __name__=='__main__':
    spider=Spider()
    spider.caw(['/view/21087.htm'])
    
    
    
    
