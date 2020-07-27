import json
with open('group_results.json', 'r', encoding='utf8')as fp:
    json_data = json.load(fp)
    userlist=[]
    for user in json_data:
        if(json_data[user]=='g3'):
            userlist.append(user)
group3_dict = {}
with open('test_data.json', 'r', encoding='utf8')as fp2:
    json_data = json.load(fp2)
    for alluser in json_data:
        if(alluser in userlist):
            group3_dict[alluser]=json_data[alluser]
json_str = json.dumps(group3_dict,indent=4)
with open('group3_data.json', 'w') as json_file:
        json_file.write(json_str)
