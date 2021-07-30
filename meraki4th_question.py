import json
dict1={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
sorted_value=sorted(dict1.values())
empty_dict={}
for i in sorted_value:
    for k in dict1.keys():
        if dict1[k]==i:
            empty_dict[k]=dict1[k]
print(empty_dict)
json_object=json.dumps(empty_dict)
print(json_object)