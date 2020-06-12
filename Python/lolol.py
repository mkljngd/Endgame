import urllib.request as ul
import re
while(True):
    site = input('Enter website:\n')
    resp = ul.urlopen(site)
    data = resp.read()
    html = data.decode('utf-8')
    l = html.split('\n')
    for i in l:
        if i.find('.mp4') >= 0:
            url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', i) 
            print(url)
