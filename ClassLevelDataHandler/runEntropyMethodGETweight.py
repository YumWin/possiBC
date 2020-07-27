import json

import pandas as pd
import numpy as np
import math
from numpy import array
import os
# 首先根据trarget获得所有同名的csv文件。。然后遍历，分别处理得到结果。。写成json数组！！
# 进行标准化

def get_TargetCSVFileList(dir,target):
    Filelist = []
    for home, dirs, files in os.walk(dir):
        for filename in files:
            # 将所有的testcases路径获取出来
            if (filename == target):
                Filelist.append(os.path.join(home, filename))
    return Filelist



# ·························································································································
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
    # weights = pd.DataFrame(weights)
    return weights
# ····························································································································
#将原始csv数据读入：第一行为指标姓名，下面每行为每个学生的对应指标的结果

# 需要整合...........................
# metadata = pd.read_csv('D:\\chengxu\\SoftwareEngineering\\probabilityTheory2\\possiBC\\theEntropyMethod\\test2.csv', encoding='utf8')
# #去除空值的记录
# metadata.dropna()
# 需要整合...........................
def generateWeightJSONfile(filepath,targetfile):
    filePathList = filepath.split('\\')
    print(filepath)
    metadata = pd.read_csv(filepath, encoding='utf8')
    metadata.dropna()
    weights = centropyWeightMethodCalculateWeight(metadata)  # 调用cal_weight
    print('得到结果::')
    # weights.columns = ['weight']
    print(weights)
    info_json = json.dumps(weights, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False)
    # 显示数据类型
    weightFileName = targetfile.replace('.csv', '') + 'Weight.json'
    weightFilePath = ('\\').join( filePathList[:len( filePathList) - 1]) + ('\\') + weightFileName
    f = open(weightFilePath,'w')
    f.write(info_json)


if __name__ == '__main__':
    dir="D:\\chengxu\\SoftwareEngineering\\probabilityTheory2\\userCSVFiles"
    targetFileList = ['debugScore.csv', 'firstConsScore.csv', 'algorthmScore.csv']
    # 一共有三种targetfile topsisDebugScore.csv  topsisFirstConscore.csv topsisAlgorthmScore.csv
    for targetfile in targetFileList:
        targetCSVFileList= get_TargetCSVFileList(dir,targetfile)
        for csvfile in targetCSVFileList:
            generateWeightJSONfile(csvfile,targetfile)
    # .......................需要整合
    # 得到各数据的权重
    # metadata = pd.read_csv("D:\\chengxu\\SoftwareEngineering\\probabilityTheory2\\possiBC\\theEntropyMethod\\test2.csv", encoding='utf8')
    # print("元数据")
    # print(metadata)
    # metadata.dropna()
    #
    # weights = centropyWeightMethodCalculateWeight(metadata)  # 调用cal_weight
    # weights.index = metadata.columns
    # print('得到结果::')
    # weights.columns = ['weight']
    # print(weights)
#.......................................
