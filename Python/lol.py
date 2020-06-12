import os
import urllib.request as ul
command = 'clip < lol.txt'
while(True):
     f1 = open('lol.txt','a+')
     site = input('Enter website:\n')
     resp = ul.urlopen(site)
     data = resp.read()
     html = data.decode('utf-8')
     l = html.split('\n')
     for i in l:
          if i.find('.mp4') >= 0:
               url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', i) 
     for i in url:
          print(i,file = f1)
     f1.close()
#os.popen(command)
