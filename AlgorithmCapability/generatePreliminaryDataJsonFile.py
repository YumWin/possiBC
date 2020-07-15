# D:\chengxu\SoftwareEngineering\probabilityTheory\Algorithm\48117\排序算法\2396\%E6%8E%92%E5%BA%8F%E6%9C%BA%E6%A2%B0%E8%87%82_1583287008549\result1583287008545\main.py
# 首先是获取到Algorithm的位置，+1是用户编号 +2是 "case_type" +3是"case_id" 从而构建json数据
#然后是直接从main.py中
#文件定位：：父文件夹(Algorithm)+userid+case_type+ case_id+filename（那一串乱码改zip为空）是文件夹dir的地址，然后找到main.py的路径！！
# 即可定位到main.py
import json
import os


def getcount(filepath):
    count = 0
    #判断给定的路径是否是.py文件
    if filepath.endswith('.py'):
        #打开文件
        f = open(filepath,'r',encoding='utf-8')
        #先读取一行
        content = f.readline()
        #当读取的代码行不是空的时候进入while循环
        while content != '':
            #判断代码行不是换行符\n时进入,代码行数加1
            if content != '\n' and '#' not in content :
                count += 1
                #接着读取下一行
            content = f.readline()
        f.close()
    return count

def get_mainFilePath(dir):

    mainFilePath = ""

    for home, dirs, files in os.walk(dir):

        for filename in files:
            if (filename=='main.py'):
                mainFilePath=os.path.join(home, filename)
                break


    return mainFilePath

def getDirFilename(path):
    pathlist=str(path).split('/')
    zipfilename=pathlist[len(pathlist)-1]
    dirname = zipfilename.replace('.zip', '')
    return dirname


def getmetadata(filePath):
    # todo 因为中间会报错中断，这些会有数据不完全，因此，sizelist的size为0或者timelist为0均全部置0！
    print('文件路径')
    print(filePath)
    sizelist=[]
    timelist=[]
    with open(filePath,"r",encoding='utf8') as f:
        for line in f.readlines():  # 逐行读取数据
            line = line.strip()  # 去掉每行头尾空白
            if (not len(line) or line.startswith('#')):  # 判断是否是空行或注释行
                continue  # 是的话，跳过不处理
            # print(line)
            sizesignstr="Total size ="
            timesignstr="run spend times:"
            if(line.find(sizesignstr)!=-1):
                linelist=line.split(' ')
                sizelist.append(linelist[len(linelist)-2])
            if(line.find(timesignstr)!=-1):
                linelist = line.split(':')
                timelist.append(linelist[1])
    if(len(sizelist)==2):
        memsize=int(sizelist[1])-int(sizelist[0])
    else:
        memsize=0
    metadata=[]
    metadata.append(memsize)
    if(len(timelist)==1):
        metadata.append(timelist[0])
    else:
        metadata.append(0)
    return metadata

     # 保存入结果文件




def createAlgorithmCapabilityJson():
    # TODO 这一行下面的路径要改！！
    with open('D:\\chengxu\\SoftwareEngineering\\probabilityTheory\\possiBC\\source_file\\sample.json','r',encoding='utf8')as f:
        json_data = json.load(f)
        # 创建字典
        info_dict = {}
        for key in json_data:
            caseList = list(json_data[key]['cases'])
            afterProcessedCaseList = []
            for case in caseList:
                specificCaseDict={}
                specificCaseDict['case_id']=case['case_id']
                specificCaseDict['case_type'] = case['case_type']
                endIndex = len(case['upload_records']) - 1
                finalUpload=case['upload_records'][endIndex]
                specificCaseDict['final_score'] = case['final_score']
                url=finalUpload['code_url']

                dirfilename=getDirFilename(url)
# TODO 这一行下面的路径要改！！
                dir='D:\\chengxu\\SoftwareEngineering\\probabilityTheory\\Algorithm\\'+key+'\\'+case['case_type']+'\\'+case['case_id']+'\\'+dirfilename
                mainfilepath=get_mainFilePath(dir)
                specificCaseDict['programLines']=getcount(mainfilepath)

                # 下面应该是从output.txt中
                # 获取运行时间  和  占用内存！！

                mainfilepathlist=mainfilepath.split('\\')
                endIndex=len(mainfilepathlist)-1

                mainfilepathlist[endIndex]="output.txt"

                outputFilePath=('\\').join(mainfilepathlist)
                # datalist[0]为运行时间
                # datalist[1]为运行占用内存
                datalist=getmetadata(outputFilePath)
                specificCaseDict['timecost']=datalist[1]
                specificCaseDict['memorycost']=datalist[0]

                afterProcessedCaseList.append(specificCaseDict)
            #这里填充user：
            info_dict[key] = afterProcessedCaseList
        # dumps 将数据转换成字符串
        info_json = json.dumps(info_dict,sort_keys=False, indent=4, separators=(',', ': '),ensure_ascii=False)
        # 显示数据类型
        print(type(info_json))
        f = open('D:\\chengxu\\SoftwareEngineering\\probabilityTheory\\possiBC\\preData\\studentAlgorthmCapabilityData.json', 'w')
        f.write(info_json)
createAlgorithmCapabilityJson()