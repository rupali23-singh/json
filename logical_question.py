list1=[{1:20,2:30}]
list2=[{2:40,5:50}]
dic3={}
for d in (list1,list2):dic3.update(d)
print(sum(dic3.values()))