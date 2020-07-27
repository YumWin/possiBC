import json
with open('group3_data.json', 'r', encoding='utf8')as fp:
    json_data = json.load(fp)
    userlist=[]
    for user in json_data:
        userlist.append(user)
    print(userlist)
    print(len(userlist))