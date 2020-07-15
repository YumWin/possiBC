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


# print(getcount('E:\\learning.py'))
def getDebugJson():
    with open('./source_file/sample.json','r',encoding='utf8')as fp:
        json_data = json.load(fp)
        # 创建字典
        info_dict = {}
        for key in json_data:
            caseList=list(json_data[key]['cases'])
            addList=[]
            for case in caseList:
                tempDict={}
                tempDict['case_id']=case['case_id']
                tempDict['case_type'] = case['case_type']
                tempDict['upload_times']=len(case['upload_records'])
                # tempList=[]
                # tempD={}
                # for record in case['upload_records']:
                #     tempD['upload_time']=record['upload_time']
                #     tempD['score'] = record['score']
                #     tempList.append(tempD)

                # tempDict['upload_records']=tempList
                tempDict['deltaScore']=case['upload_records'][len(case['upload_records'])-1]['score']-case['upload_records'][0]['score']
                tempDict['deltaTime']=case['upload_records'][len(case['upload_records'])-1]['upload_time']-case['upload_records'][0]['upload_time']
                addList.append(tempDict)
            info_dict[key]=addList
        # dumps 将数据转换成字符串
        info_json = json.dumps(info_dict,sort_keys=False, indent=4, separators=(',', ': '),ensure_ascii=False)
        # 显示数据类型
        print(type(info_json))
        f = open('E:\\possiBC\\preData\\debug.json', 'w')
        f.write(info_json)

def get_filelist(dir):

    Filelist = []

    for home, dirs, files in os.walk(dir):

        for filename in files:

    # 文件名列表，包含完整路径

            Filelist.append(os.path.join(home, filename))

  # # 文件名列表，只包含文件名

  # Filelist.append( filename)

    return Filelist

def getFirstConstructionJson():
    with open('./source_file/sample.json','r',encoding='utf8')as fp:
        json_data = json.load(fp)
        # 创建字典
        info_dict = {}
        for key in json_data:
            caseList = list(json_data[key]['cases'])
            addList = []
            for case in caseList:
                tempDict={}
                tempDict['case_id']=case['case_id']
                tempDict['case_type'] = case['case_type']
                firstUpload=case['upload_records'][0]
                tempDict['firstTime']=firstUpload['upload_time']
                tempDict['firstScore'] = firstUpload['score']
                url=firstUpload['code_url']
                fileName=''
                i=len(url)-1
                while(i>=0):
                    if(url[i]!='/'):
                        fileName+=url[i]
                    else:
                        break
                    i-=1
                fileName=fileName[::-1]
                dirname = fileName.replace('.zip', '')
                dir='E:\\Sample\\'+key+'\\'+case['case_type']+'\\'+case['case_id']+'\\'+dirname
                fileList=get_filelist(dir)
                fileDir=''
                for file in fileList:
                    if(file.endswith('main.py')):
                        fileDir=file+''
                        break
                tempDict['firstLines']=getcount(fileDir)
                addList.append(tempDict)
            info_dict[key] = addList
        # dumps 将数据转换成字符串
        info_json = json.dumps(info_dict,sort_keys=False, indent=4, separators=(',', ': '),ensure_ascii=False)
        # 显示数据类型
        print(type(info_json))
        f = open('E:\\possiBC\\preData\\firstConstruction.json', 'w')
        f.write(info_json)

getDebugJson()
getFirstConstructionJson()