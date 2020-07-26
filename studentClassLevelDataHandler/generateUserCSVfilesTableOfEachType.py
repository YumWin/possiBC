# 生成 每个user每类题做的具体题目！！！
# 首先是遍历student
# 将json文件存放为一个map！！

#programTypeList=[]：存放所有的题目类型：
# for user in users
#     userTypeLevalProgramids={‘线性表’：[] }::分类整理用户做的题目！！！
#     遍历programclassTypes:从类型入手
#     for programType in programTypeList ：对应着i
#              遍历具体对应user的题目列表
#          for concreteProgram in userProgramLiat
#               if(concreteProgram.case == programcase)
#                  userTypeLevalProgramids[programcase].append[concreteProgram.programid]
#       下面就是生成对应文件的过程！！
import json
import os
programTypeList=["字符串","图算法","线性表"]

def getUserCSVfilesOfTypeLeval():
    #todo 有编码上的问题。。。。记得注意以上GBK
    # with open('D:\\chengxu\\SoftwareEngineering\\probabilityTheory2\\possiBC\\studentClassLevelDataHandler\\first.json','r',encoding='utf8')as f:

    with open('D:\\chengxu\\SoftwareEngineering\\probabilityTheory2\\possiBC\\dataProcess\\TopsisProcess.json','r',encoding='utf8')as f:
        usersMetaData = json.load(f)
        # 创建字典
        for userid in usersMetaData:
            # 用来存放user的各类题的题目id列表map
            userTypeLevalProgramIds = {}
            userProgramList=list(usersMetaData[userid])
            # print("user题目列表")
            # print(userProgramList)
            for programType in programTypeList:
                userThisTypeProgramList=[]
                for concreteProgram in userProgramList:
                    if(concreteProgram["case_type"]==programType):
                        userThisTypeProgramList.append(concreteProgram)
                userTypeLevalProgramIds[programType]=userThisTypeProgramList
            userHomePath="D:\\chengxu\\SoftwareEngineering\\probabilityTheory2\\userCSVFiles\\"+userid
            os.makedirs(userHomePath)
            print(userid)
            print(userTypeLevalProgramIds)
            for programType in userTypeLevalProgramIds:
                os.makedirs(userHomePath+'\\'+programType)
                info_json = json.dumps(userTypeLevalProgramIds[programType], sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False)
                fileName=userHomePath+'\\'+programType+"\\"+"table.json"
                f = open(fileName, 'w',encoding='utf8')
                f.write(info_json)
        # dumps 将数据转换成字符串
        # info_json = json.dumps(info_dict,sort_keys=False, indent=4, separators=(',', ': '),ensure_ascii=False)
        # 显示数据类型
        # print(type(info_json))
        # f = open('E:\\possiBC\\preData\\debug.json', 'w')
        # f.write(info_json)
if __name__ == '__main__':
    getUserCSVfilesOfTypeLeval()