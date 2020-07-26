import json
import os
import numpy as np
# 传入 父类文件夹
# 首先遍历学生：userid
# 然后是自定义一个题目类别list
# 遍历自定义的学生题目类别，加上userid得到了文件所在父级路径！！
#得到所有的weight.josn  file：：另起一个函数

programTypeList = ["字符串", "图算法"]


def get_allWeightFile(dir):
    Filelist = []
    for home, dirs, files in os.walk(dir):
        for filename in files:
            # 将所有的testcases路径获取出来
            if (filename.endswith("Weight.json")):
                Filelist.append(os.path.join(home, filename))
    return Filelist


def get_targetScorelist(tableFilePath, weightTargetName):
    with open(tableFilePath, 'r', encoding='utf8')as f:
        tableData = json.load(f)
        targetScorelist= []
        for programcase in tableData:
            targetScorelist.append(programcase[weightTargetName])
        return targetScorelist


def get_usersMetaData():
    with open(
            'D:\\chengxu\\SoftwareEngineering\\probabilityTheory2\\possiBC\\studentClassLevelDataHandler\\first.json',
            'r', encoding='utf8')as f:
        usersMetaData = json.load(f)
        return usersMetaData
# 遍历得到的weightfilelist
# 消除尾部得到标准名！！！
# 然后通过得到的父级路径得到table文件路径
# 另起一个函数：打开table文件并依次取出对应的题目的对应的结果 返回一个scorelist
# 然后打开对应的weight文件读出一个list
# 累加计算结果，
#  学生 类级别的 {} 【对应seore】=计算出结果
def get_userAbliltyTypeLevelJSONfile(dir):
    usersMetaData = get_usersMetaData()
    # 创建字典
    userAbliltyInfo = {}
    for userid in usersMetaData:
        userIdTypeAbilityList=[]
        for programType in programTypeList:
            userProgramTypeInfo={}
            userProgramTypeInfo['case_type']=programType

            tableFileDir=dir+('\\')+userid+('\\')+programType
            weightFileList=get_allWeightFile(tableFileDir)

            for weightFilePath in weightFileList:
                weightFilePathlist=weightFilePath.split("\\")
                weightTargetName=weightFilePathlist[len(weightFilePathlist)-1].replace("Weight.json","")
                tableFilePath=tableFileDir+('\\')+"table.json"
                targetScorelist=get_targetScorelist(tableFilePath,weightTargetName)
                with open(weightFilePath, 'r', encoding='utf8')as f:
                    weightList = json.load(f)
                    multiplyresult = np.multiply(np.array(weightList), np.array(targetScorelist))
                    sumScore=multiplyresult.sum()
                    userProgramTypeInfo[weightTargetName]=sumScore
            userIdTypeAbilityList.append(userProgramTypeInfo)
        userAbliltyInfo[userid]=userIdTypeAbilityList
    info_json = json.dumps(userAbliltyInfo, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False)
    f = open('D:\\chengxu\\SoftwareEngineering\\probabilityTheory2\\possiBC\\studentClassLevelDataHandler\\second.json', 'w',encoding='utf8')
    f.write(info_json)


if __name__ == '__main__':
    get_userAbliltyTypeLevelJSONfile('D:\\chengxu\\SoftwareEngineering\\probabilityTheory2\\userCSVFiles')
    # List1 = [1, 2, 3]
    # List2 = [5, 6, 7]
    # List3 = np.multiply(np.array(List1), np.array(List2))
    # print(List3.tolist())
    # print(List3.sum())
