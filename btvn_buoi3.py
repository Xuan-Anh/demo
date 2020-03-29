# -*- coding:utf-8 -*-
dic =  {
        1: {'name': 'a', 'age': '18', 'id':1},
        2: {'name': 'b', 'age': '19', 'id':2}, 
        3: {'name': 'c', 'age': '20', 'id':1},
        4: {'name': 'd', 'age': '21', 'id':3},
       }
mylist = []
i = 1
max1 = max(dic)
while i <= max1 :
    if dic[i]['id'] in mylist:
        del dic[i]
    else:
        mylist.append(dic[i]['id']) 
    i+=1

# aaa
print(dic)