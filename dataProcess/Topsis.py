import json
import numpy as np
import pandas as pd
from numpy import array
import math

# 进行标准化
def metadataStandardize(data):
    return data.apply(lambda x: ((x - np.min(x)) / (np.max(x) - np.min(x))))

def get_informationEntropy(standardData,rows,cols,lnf,k):

    # 矩阵计算并得到信息熵
    standardData = array(standardData)
    lnf = [[None] * cols for i in range(rows)]
    lnf = array(lnf)
    for i in range(0, rows):
        for j in range(0, cols):
            if standardData[i][j] == 0:
                lnfij = 0.0
            else:
                p = standardData[i][j] / standardData.sum(axis=0)[j]
                lnfij = math.log(p) * p * (-k)
            lnf[i][j] = lnfij
    lnf = pd.DataFrame(lnf)
    return lnf

def centropyWeightMethodCalculateWeight(metadata):

    standardData = metadataStandardize(metadata)
    # 计算出k值
    rows = standardData.index.size
    cols = standardData.columns.size
    if(math.log(rows)==0):
        k=1
    else:
        k = 1.0 / math.log(rows)
    lnf = [[None] * cols for i in range(rows)]
    # 计算并得到信息熵
    informationEntropy = get_informationEntropy(standardData,rows,cols,lnf,k)
    # 计算出冗余度
    redundancy = 1 - informationEntropy.sum(axis=0)
    # 计算各指标的权重
    weights = [[None] * 1 for i in range(cols)]
    for j in range(0, cols):
        colweight= redundancy[j] / sum(redundancy)
        weights[j] = colweight
    # 计算各样本的综合得分并得到标准权重！！
    weights = pd.DataFrame(weights)
    return weights



def dataPre():
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
                addList.append(tempDict)
            info_dict[key]=addList

        # info_json = json.dumps(info_dict,sort_keys=False, indent=4, separators=(',', ': '),ensure_ascii=False)
        #
        # print(type(info_json))
        # f = open('E:\\possiBC\\deepData\\TopsisProcess.json', 'w')
        # f.write(info_json)

def findCase(dir,case_id):
    with open(dir,'r',encoding='gbk')as fp:
        findList=[]
        json_data = json.load(fp)
        for key in json_data:
            for case in json_data[key]:
                if(case['case_id']==case_id):
                    case['user_id']=key
                    findList.append(case)
        return findList


def debugJudge():
    with open('./preData/debug.json','r',encoding='gbk')as fp:
        readyList=[]
        json_data = json.load(fp)
        for key in info_dict:
            caseList=list(info_dict[key])
            for case in caseList:
                if(case['case_id'] not in readyList):
                    readyList.append(case['case_id'])
                    findList=findCase('./preData/debug.json',case['case_id'])
                    todoList=[]
                    for element in findList:
                        tempList=[]
                        tempList.append(element['upload_times'])
                        tempList.append(element['deltaScore'])
                        tempList.append(element['deltaTime'])
                        todoList.append(tempList)
                    tempScoreList=standaradizing(positive(todoList,[0,1,0]))
                    ScoreList=getScore(tempScoreList,getWeight(tempScoreList))
                    i=0
                    while(i<len(ScoreList)):
                        writeInDict(findList[i]['user_id'],findList[i]['case_id'],'debugScore',ScoreList[i])
                        i+=1
        # info_json = json.dumps(info_dict,sort_keys=False, indent=4, separators=(',', ': '),ensure_ascii=False)
        #
        # print(type(info_json))
        # f = open('E:\\possiBC\\deepData\\TopsisProcess.json', 'w')
        # f.write(info_json)

def firstConsJudge():
    with open('./preData/firstConstruction.json','r',encoding='gbk')as fp:
        readyList=[]
        json_data = json.load(fp)
        for key in info_dict:
            caseList=list(info_dict[key])
            for case in caseList:
                if(case['case_id'] not in readyList):
                    readyList.append(case['case_id'])
                    findList=findCase('./preData/firstConstruction.json',case['case_id'])
                    todoList=[]
                    for element in findList:
                        tempList=[]
                        tempList.append(element['firstTime'])
                        tempList.append(element['firstScore'])
                        tempList.append(element['firstLines'])
                        todoList.append(tempList)
                    tempScoreList=standaradizing(positive(todoList,[0,1,0]))
                    ScoreList=getScore(tempScoreList,getWeight(tempScoreList))
                    i=0
                    while(i<len(ScoreList)):
                        writeInDict(findList[i]['user_id'],findList[i]['case_id'],'firstConsScore',ScoreList[i])
                        i+=1
        # info_json = json.dumps(info_dict,sort_keys=False, indent=4, separators=(',', ': '),ensure_ascii=False)
        #
        # print(type(info_json))
        # f = open('E:\\possiBC\\deepData\\TopsisProcess.json', 'w')
        # f.write(info_json)

def algorthmJudge():
    with open('./preData/studentAlgorthmCapabilityData.json','r',encoding='gbk')as fp:
        readyList=[]
        json_data = json.load(fp)
        for key in info_dict:
            caseList=list(info_dict[key])
            for case in caseList:
                if(case['case_id'] not in readyList):
                    readyList.append(case['case_id'])
                    findList=findCase('./preData/studentAlgorthmCapabilityData.json',case['case_id'])
                    todoList=[]
                    for element in findList:
                        tempList=[]
                        tempList.append(element['final_score'])
                        tempList.append(element['programLines'])
                        tempList.append(float(element['timecost'])*10000000)
                        tempList.append(element['memorycost'])
                        todoList.append(tempList)
                    tempScoreList=standaradizing(positive(todoList,[1,0,0,0]))
                    ScoreList=getScore(tempScoreList,getWeight(tempScoreList))
                    i=0
                    while(i<len(ScoreList)):
                        writeInDict(findList[i]['user_id'],findList[i]['case_id'],'algorthmScore',ScoreList[i])
                        i+=1
        info_json = json.dumps(info_dict,sort_keys=False, indent=4, separators=(',', ': '),ensure_ascii=False)

        print(type(info_json))
        f = open('D:\\chengxu\\SoftwareEngineering\\probabilityTheory2\\possiBC\\dataProcess\\TopsisProcess.json', 'w',encoding='utf8')
        f.write(info_json)

def writeInDict(user_id,case_id,name,Score):
    for key in info_dict:
        if(key==user_id):
            for case in info_dict[key]:
                if(case['case_id']==case_id):
                    case[name]=Score

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
            if(tempList[j]==0):
                todoList[i][j]=0
            else:
                todoList[i][j]/=tempList[j]
                todoList[i][j]=round(todoList[i][j],4)
            j+=1
        i+=1
    return todoList

def getScore(todoList,weightList):
    i=0
    MAXlist=[]
    MINlist=[]
    while(i<len(todoList[0])):
        j=0
        MAX=todoList[0][i]
        MIN=todoList[0][i]
        while(j<len(todoList)):
            if(todoList[j][i]>MAX):
                MAX=todoList[j][i]
            if(todoList[j][i]<MIN):
                MIN=todoList[j][i]
            j+=1
        MAXlist.append(MAX)
        MINlist.append(MIN)
        i+=1
    DplusList=[]
    DminusList=[]
    i=0
    while(i<len(todoList)):
        j=0
        SUMplus=0
        SUMminus=0
        while(j<len(todoList[0])):
            SUMplus+=pow(MAXlist[j]-todoList[i][j],2)*weightList[j]
            SUMminus+=pow(MINlist[j]-todoList[i][j],2)*weightList[j]
            j+=1
        SUMplus=pow(SUMplus,0.5)
        SUMminus =pow(SUMminus, 0.5)
        DplusList.append(SUMplus)
        DminusList.append(SUMminus)
        i+=1

    pureScoreList=[]
    j=0
    while(j<len(DplusList)):
        if((DplusList[j]+DminusList[j])!=0):
            pureScoreList.append(round(DminusList[j]/(DplusList[j]+DminusList[j]),4))
        else:
            pureScoreList.append(0)
        j+=1
    ScoreList=[]
    j=0
    while(j<len(pureScoreList)):
        if(sum(pureScoreList)!=0):
            ScoreList.append(round(round(pureScoreList[j]/sum(pureScoreList),4)*100,2))
        else:
            ScoreList.append(0)
        j+=1
    return ScoreList

def getWeight(todoList):
    metadata={}
    i=0
    while(i<len(todoList[0])):
        j=0
        metadata[chr(ord('a')+i)]=[]
        while(j<len(todoList)):
            metadata[chr(ord('a') + i)].append(todoList[j][i])
            j+=1
        i+=1
    # metadata = {'a': [0, 2, 3, 4, 5], 'b': [1, 2, 3, 1, 5], 'c': [2, 3, 2, 5, 2]}
    metadata = pd.DataFrame(metadata)
    # metadata={}
    # 去除空值的记录
    metadata.dropna()
    weights = centropyWeightMethodCalculateWeight(metadata)  # 调用cal_weight
    weights.index = metadata.columns
    weights.columns = ['weight']
    # print(weights.to_dict('list')['weight'])
    return weights.to_dict('list')['weight']

info_dict={}
dataPre()
debugJudge()
firstConsJudge()
algorthmJudge()


# tempAns=positive([[89,2],[60,0],[74,1],[99,3]],[1,0])
# print(tempAns)
# tempAns=standaradizing(tempAns)
# print(tempAns)
# tempAns=getScore(tempAns,getWeight(tempAns))
# print(tempAns)


