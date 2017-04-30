#-*- coding:utf-8 -*-

import urllib2,re

class BDTB: baseurl = 'https://tieba.baidu.com/p/5090251246?see_lz=1' filename = 'guigushi'

def getpage(self):
    try:
        url = self.baseurl
        req = urllib2.Request(url)
        response = urllib2.urlopen(req).read()
        #print response
        return response
    except Exception,e:
        print e
    
def gettitle(self):
    html = self.getpage()
    reg = re.compile(r'title: "(.*?)"')
    f = open(self.filename + '.txt','w')
    #f.write(html)  #test
    for i in re.findall(reg,html):
        f.write(i + '\n')
    f.close
    
def getcontent(self):
    html = self.getpage()
    reg = re.compile(r'class="d_post_content j_d_post_content ">(.*?)</div>')
    f = open(self.filename + '.txt','a')
    for i in re.findall(reg,html) :
        fliter_a = re.compile(r'<a.*?>|</a>')
        fliter_img = re.compile('<img.*?>')
        i = re.sub(fliter_a,"",i)
        i = re.sub(fliter_img,"",i)
        i = re.sub('<br>',"\n",i)
        f.write(i)
    f.close            
bdtb1 = BDTB() 
print '开始爬取！' 
bdtb1.gettitle() 
bdtb1.getcontent() 
print '爬取完成！'
