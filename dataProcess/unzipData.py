import os
import sys
import zipfile


def unzip(filename: str):
    try:
        file = zipfile.ZipFile(filename)
        dirname = filename.replace('.zip', '')
        # 如果存在与压缩包同名文件夹 提示信息并跳过
        if os.path.exists(dirname):
            print(f'{filename} dir has already existed')
            return
        else:
            # 创建文件夹，并解压
            os.mkdir(dirname)
            file.extractall(dirname)
            file.close()
            # 递归修复编码
            rename(dirname)
    except:
        print(f'{filename} unzip fail')


def rename(pwd: str, filename=''):
    """压缩包内部文件有中文名, 解压后出现乱码，进行恢复"""

    path = f'{pwd}/{filename}'
    if os.path.isdir(path):
        for i in os.scandir(path):
            rename(path, i.name)
    newname = filename.encode('cp437').decode('gbk')
    os.rename(path, f'{pwd}/{newname}')


def main():
    """如果指定文件，则解压目标文件，否则解压当前目录下所有文件"""

    if len(sys.argv) != 1:
        i: str
        for i in sys.argv:
            if i.endswith('.zip') and os.path.isfile(i):
                unzip(i)
    else:
        for file in os.scandir(os.getcwd()):
            if file.name.endswith('.zip') and file.is_file():
                unzip(file.name)


def get_filelist(dir):

    Filelist = []

    for home, dirs, files in os.walk(dir):

        for filename in files:

    # 文件名列表，包含完整路径

            Filelist.append(os.path.join(home, filename))

  # # 文件名列表，只包含文件名

  # Filelist.append( filename)

    return Filelist



if __name__ == '__main__':
    Filelist = get_filelist('D:\\chengxu\\SoftwareEngineering\\probabilityTheory2\\simpleFirstCode')

    print(len(Filelist))

    for file in Filelist:
        print(file)
        unzip(file)