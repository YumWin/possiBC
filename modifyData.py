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


print(getcount('E:\\learning.py'))