import json

info_dict={}
def debugJudge():
    todoList=[]
    with open('./preData/debug.json','r',encoding='gbk')as fp:
        json_data = json.load(fp)
        # info_dict = {}
        for key in json_data:
            caseList=list(json_data[key])
            addList=[]
            for case in caseList:
                tempDict={}
                tempDict['case_id']=case['case_id']
                tempDict['case_type'] = case['case_type']
                tempDict['upload_times']=case['upload_times']
                addList.append(tempDict)
            info_dict[key]=addList

        info_json = json.dumps(info_dict,sort_keys=False, indent=4, separators=(',', ': '),ensure_ascii=False)

        print(type(info_json))
        f = open('E:\\possiBC\\deepData\\TopsisProcess.json', 'w')
        f.write(info_json)

def positive(todoList,judgeList):
    i=0
    while(i<len(judgeList)):
        if(judgeList[i]==0):
            MAX=todoList[0][i]
            j=0
            while(j<len(todoList)):
                if(todoList[j][i]>MAX):
                    MAX=todoList[j][i]
                j+=1
            j=0
            while(j<len(todoList)):
                todoList[j][i]=MAX-todoList[j][i]
                j+=1
        i+=1
    return todoList

def standaradizing(todoList):
    i=0
    tempList=[]
    while(i<len(todoList[0])):
        SUM=0
        j=0
        while(j<len(todoList)):
            SUM+=pow(todoList[j][i],2)
            j+=1
        SUM=pow(SUM,0.5)
        tempList.append(SUM)
        i+=1
    i=0
    while(i<len(todoList)):
        j=0
        while(j<len(todoList[0])):
            todoList[i][j]/=tempList[j]
            todoList[i][j]=round(todoList[i][j],4)
            j+=1
        i+=1
    return todoList

# def getPureScore():

# print(positive([[1,2,3],[4,5,6],[7,8,9]],[0,0,1]))
# print(standaradizing([[89,1],[60,3],[74,2],[99,0]]))
