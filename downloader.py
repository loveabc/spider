#下载器,根据url下载网页内容
import urllib.request
class Downloader():
    def __init__(self):
        pass
    def download(self,url):
        response=urllib.request.urlopen(url)
        if response.getcode()!=200:
            return
        con=response.read().decode('utf8')
        response.close()
        return con
