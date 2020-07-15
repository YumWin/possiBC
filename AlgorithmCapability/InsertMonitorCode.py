
import os


def getMainFileList(dir):
    Filelist = []
    for home, dirs, files in os.walk(dir):
        for filename in files:
            # 将所有的testcases路径获取出来
            if (filename == 'main.py'):
                Filelist.append(os.path.join(home, filename))
    return Filelist


def insertMonitorCodeBeg(file):
    with open(file, 'r+',encoding='utf8') as f:
        content = f.read()
        f.seek(0, 0)
        f.write('''import time
from guppy import hpy
hp = hpy()
print('before run:')
print(hp.heap())
myteststarttime = time.perf_counter()
''' + content)
# 为了应对不规范变量命名比如time和str。。。
def insertMonitorCodeEnd(file):
    with open(file,encoding="utf-8",mode="a") as f:
        f.write('''
import time
mytestendtime = time.perf_counter()
print('end run:')
print(hp.heap())
spend=repr(mytestendtime-myteststarttime)
print('run spend times:'+spend)''')

if __name__ == '__main__':
    mainFilelist = getMainFileList('D:\\chengxu\\SoftwareEngineering\\probabilityTheory\\Algorithm')
    for file in mainFilelist:
        print(file)
        insertMonitorCodeBeg(file)
        insertMonitorCodeEnd(file)