import re
pattern=r'[A-Z]'
res=re.match(pattern,"Hello World")
print(res.group() if res else "No Match") #Hello

#Search is used to search the entire string
import re
pattern=r'[aeiou]'
res=re.search(pattern,"YFYUHello World")
print(res.group() if res else "No Match") #e

#Findall is used to find all the elements and return output in list fiormat
import re
pattern=r'[aeiou]'
res=re.findall(pattern,"YFYUHello World")
print(res) #['e', 'o', 'o']

#find all example
import re
pattern=r'\d{4}|\d{2}'
res=re.findall(pattern,"pfs-31 2025 pfs-20 2020 pfs-13 2030")
print(res) #['2025', '2020', '2030']
# ['31', '2025', '20', '2020', '13', '2030']

#Find iter
'''import re
pattern=r'\d{4}|\d{2}'
res=re.findall(pattern,'pfs-31 2025 pfs-20 2020 pfs-13 2030')
for i in res:
    print(i.group(),i.start())
    '''

#Full match
import re
pattern=r'\d{4}'
res=re.fullmatch(pattern, '1234')
print(res.group() if res else "No Match") 
#1234

#Replace Anything in regular expression
import re
pattern=r'[aeior]'
res=re.sub(pattern,'@' ,'python programming language')
print(res) #pyth@n p@@g@@mm@ng l@ngu@g@

#Split in regular expression
import re
pattern=r'[:,*]'
res=re.split(pattern,'pyth:on,programming*lang,uage')
print(res) #['pyth', 'on', 'programming', 'lang', 'uage']




