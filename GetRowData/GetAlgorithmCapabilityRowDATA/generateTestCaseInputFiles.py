import time
import os
import json



# 现在开始准备在json上一级创建一个txt输入文件！
def getCaseFileList(dir):
    Filelist = []
    for home, dirs, files in os.walk(dir):
        for filename in files:
            # 将所有的testcases路径获取出来
            if(filename=='testCases.json'):
                Filelist.append(os.path.join(home, filename))
    return Filelist


def makeInputFile(file):
    with open(file, 'r', encoding='utf8')as casepath:
        json_data = json.load(casepath)
        inputline=str(json_data[0]['input'])
        # print('用例行')
        # print(inputline)
        inputlinelist=inputline.split('\n')
        # inputlinelist=inputlinelist[:len(inputlinelist)-1]
        # print(inputlinelist)
#
        # print('路径名')
        filenamelist=file.split('\\')
        num=len(filenamelist)-2
        inputFileNameList=filenamelist[:num]
        inputFilePath='\\'.join(inputFileNameList)+'\\input.txt'
        with open(inputFilePath, 'a', encoding='utf8')as f:
            for line in inputlinelist:
                f.write(line+'\n')
        # print(inputFilePath)


if __name__ == '__main__':
    caseFilelist = getCaseFileList('D:\\chengxu\\SoftwareEngineering\\probabilityTheory2\\Algorithm')
    for case in caseFilelist:
        print(case)
        makeInputFile(case)