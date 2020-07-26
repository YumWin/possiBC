
import time
import os
import json
# from guppy import hpy
from pathlib import Path
import psutil

# p0=time.perf_counter()
# path="D:\\chengxu\\SoftwareEngineering\\probabilityTheory\\possiBC\\tryOpenPY\\user1\\main.py"
# cmdstr=('python ')+path+(' < ')+('D:\\chengxu\\SoftwareEngineering\\probabilityTheory\\possiBC\\tryOpenPY\\user1\\input.txt')
# print(cmdstr)
# os.system(cmdstr)
# os.system('100')
# p1=time.perf_counter()
# spend=str(p1-p0)
# print('用时：：'+spend)
# 首先需要处理输入文件，在main的路径级下，创建一个叫input.txt的文件里面放入result目录下的case中第一个input，进行处理，
# 读入后，利用split /n 将每行分开然后写入到input.txt的文件中。
# 然后进行运行测试。。。。。。获取到运行时间


def getMainFileList(dir):
    Filelist = []
    for home, dirs, files in os.walk(dir):
        for filename in files:
            # 将所有的testcases路径获取出来
            if (filename == 'main.py'):
                output_file = Path(home + "\\output.txt")
                if (output_file.exists()):
                    print(home + filename + "执行过了")
                else:
                    Filelist.append(os.path.join(home, filename))
    return Filelist

def recordMainfileMetadata(file):
    pathlist=file.split('\\')
    # pathlist可以在做python文件用
    inputPath=('\\').join(pathlist[:len(pathlist)-1])+('\\input.txt')
    outputPath=('\\').join(pathlist[:len(pathlist)-1])+('\\output.txt')
    # 同时生
    # print(inputPath)

    cmdstr=('python ')+file+(' < ')+inputPath +  (' > ')+outputPath
    # TODO 做一个监控超过一段时间自动停止！！
    #  难以做到
    # 已经以绕过已经执行程序作为替代
    os.system(cmdstr)
    # try:
    #     process = psutil.Process(os.system(cmdstr))
    # except Exception as e:
    #     print('这个程序有问题。。。干')

    # print('内存占用：')
    # print(process.memory_info().rss)


if __name__ == '__main__':
    mainFilelist = getMainFileList('D:\\chengxu\\SoftwareEngineering\\probabilityTheory2\\Algorithm')
    for file in mainFilelist:
        print(file)
        recordMainfileMetadata(file)
