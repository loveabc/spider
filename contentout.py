#内容输出器
class Outputer():
    def __init__(self):
        pass
    def output(self,con,part):
        file=open(r'd:\html\baike_'+str(part)+'.html','w',encoding='utf8')
        file.write('<html><body><head><meta charset="utf8"></meta><title>百度百科</title></head><table>')
        for c in con:
            file.write('<tr>')
            file.write('<td>'+c[0]+'</td>')
            file.write('<td>'+c[1]+'</td>')
            file.write('<td>'+c[2]+'</td>')
            file.write('</tr>')
        file.write('</table></body></html>')
        file.close()