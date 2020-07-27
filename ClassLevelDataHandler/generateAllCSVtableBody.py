# 首先获取所有的table的全路径：：已经ok
# 然后main里面一个for：（理论上每个文件都要打开一次first.json）


import os
import json
import numpy as np
import csv
def getTableFileList(dir):
    Filelist = []
    for home, dirs, files in os.walk(dir):
        for filename in files:
            # 将所有的testcases路径获取出来
            if (filename == 'table.json'):
                Filelist.append(os.path.join(home, filename))
    return Filelist
# def（table.json的path，指标 如：topsisDebugScore）
# 首先把路径裂开。从而将生成文件的路径确定下来！！！
#  打开对应的table （可以另起一个函数）从而把需要找的 题目列表出来，生成一个programlist
# 遍历programlist，理论上遍历一次即可
# ！！！！目标应该是
# {
#   ’2920‘：[80,40,20,10],
#   ’2921‘：[80,40,20,10],
#   ’2922‘：[80,40,20,10],
#   ’2923‘：[80,40,20,10],
#
# }


def get_programIdList(path):
    with open(path,'r', encoding='utf8')as f:
        tableData = json.load(f)
        programIdList=[]
        for programcase in tableData:
            programIdList.append(programcase['case_id'])
        return programIdList
# 然后打开first 并读取为map（obj） 对象
# 然后无视user，直接遍历userprogramList
# 然后 for concreteProgram in userProgramLiat
#  开始遍历table的key！！
#   if有key==concreteProgram["case_id"]
#       table[key].append(对应的指标！！)
#         break
# 最后应该可以生成目标数组：
# 然后生成csv文件即可！！路径上面给了！！

def fillTypeLevelCSVfile(path, target):
    tableFilePathList = file.split('\\')
    # print("path")
    # print(path)
    programIdList=get_programIdList(path)
    if(programIdList==[]):
        return
    # print(programIdList)
    # 首先初始化结果集
    resultCSVdata={}
    for needProgramId in programIdList:
        resultCSVdata[needProgramId]=[]
    # print('result init')
    # print(resultCSVdata)
    with open('D:\\chengxu\\SoftwareEngineering\\probabilityTheory2\\possiBC\\getAllCases\\TopsisProcess.json','r',encoding='utf8')as f:
        usersMetaData = json.load(f)
        for user in usersMetaData:
            for metaProgramCase in usersMetaData[user]:
               for needProgramId in programIdList:
                   if(needProgramId==metaProgramCase['case_id']):
                       resultCSVdata[needProgramId].append(metaProgramCase[target])
                       break
        rows=[]
        headers=[]
        for programid in resultCSVdata:
            headers.append(programid)
            rows.append(resultCSVdata[programid])
        minnum=100
        for thisrow in rows:
            rownum=len(thisrow)
            if(rownum<minnum):
                minnum=rownum
        rows=[rows[i][0:minnum] for i in range(0,len(rows))]
        # 下面因为元素不匹配，因为无法转成二维array
        rowsnp=np.array(rows)
        rowsTrueData=rowsnp.T.tolist()
        resultCSVfileName=target+'.csv'
        CSVFilePath = ('\\').join( tableFilePathList[:len( tableFilePathList) - 1]) + ('\\')+resultCSVfileName
        print(CSVFilePath)
        with open(CSVFilePath, "w", newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(headers)  # headers为表头属性名组成的数组
            f_csv.writerows(rowsTrueData)
    # print('转置后')
        # print(rowsTrueData)
if __name__ == '__main__':
    tableFilelist = getTableFileList('D:\\chengxu\\SoftwareEngineering\\probabilityTheory2\\userCSVFiles')
    targetList=['debugScore','firstConsScore','algorthmScore']
    for file in tableFilelist:
        for target in targetList:
            fillTypeLevelCSVfile(file,target)