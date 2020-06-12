import re

search_term = '\S+?@\S+'
text = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

print(re.findall(search_term,text))