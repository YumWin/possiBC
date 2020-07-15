# -*- coding: utf-8 -*-
"""
目标：提供一个函数能够从网上下载资源
输入：
    url列表
    保存路径
输出：
    保存到指定路径中的文件
要求：
    能够实现下载过程，即从0%到100%可视化
"""
# =====================================================

from six.moves import urllib
import os
from urllib.parse import quote
import string

import sys
import json


def download_and_extract(Fileinfo, save_dir):
    """根据给定的URL地址下载文件
    Parameter:
        filepath: list 文件的URL路径地址
        save_dir: str  保存路径
    Return:
        None
    """
    temp_dir = save_dir + ''
    for fileinfo in Fileinfo:
        filepath = []
        j = 3
        while (j < len(fileinfo)):
            filepath.append(fileinfo[j])
            j += 1
        save_dir = temp_dir + '\\' + fileinfo[0] + '\\' + fileinfo[2]
        try:
            os.makedirs(save_dir + '\\' + fileinfo[1])
        except Exception as e:
            print("User" + fileinfo[0] + ' already has the case ' + fileinfo[1])
        save_dir = save_dir + '\\' + fileinfo[1]
        for url, index in zip(filepath, range(len(filepath))):
            filename = url.split('/')[-1]
            save_path = os.path.join(save_dir, filename)
            # url = urllib.parse.quote_plus(url)
            url = quote(url, safe=string.printable)

            urllib.request.urlretrieve(url, save_path)

            sys.stdout.write('\r>> Downloading %.1f%%' % (float(index + 1) / float(len(filepath)) * 100.0))
            sys.stdout.flush()
        print('\nSuccessfully downloaded')


Fileinfo=[]
# filePath=[]
# userId=[]
i = 0
with open('D:\\chengxu\\SoftwareEngineering\\probabilityTheory\\possiBC\\source_file\\sample.json', 'r', encoding='utf8')as fp:
    json_data = json.load(fp)
    for key in json_data:
        caseList = list(json_data[key]['cases'])
        # userId.append(str(json_data['user_id']))
        os.makedirs('D:\\chengxu\\SoftwareEngineering\\probabilityTheory\\Algorithm\\' + str(json_data[key]['user_id']))
        os.makedirs(
            'D:\\chengxu\\SoftwareEngineering\\probabilityTheory\\Algorithm\\' + str(json_data[key]['user_id']) + '\\字符串')
        os.makedirs(
            'D:\\chengxu\\SoftwareEngineering\\probabilityTheory\\Algorithm\\' + str(json_data[key]['user_id']) + '\\线性表')
        os.makedirs(
            'D:\\chengxu\\SoftwareEngineering\\probabilityTheory\\Algorithm\\' + str(json_data[key]['user_id']) + '\\数组')
        os.makedirs(
            'D:\\chengxu\\SoftwareEngineering\\probabilityTheory\\Algorithm\\' + str(json_data[key]['user_id']) + '\\查找算法')
        os.makedirs(
            'D:\\chengxu\\SoftwareEngineering\\probabilityTheory\\Algorithm\\' + str(json_data[key]['user_id']) + '\\排序算法')
        os.makedirs(
            'D:\\chengxu\\SoftwareEngineering\\probabilityTheory\\Algorithm\\' + str(json_data[key]['user_id']) + '\\数字操作')
        os.makedirs(
            'D:\\chengxu\\SoftwareEngineering\\probabilityTheory\\Algorithm\\' + str(json_data[key]['user_id']) + '\\树结构')
        os.makedirs(
            'D:\\chengxu\\SoftwareEngineering\\probabilityTheory\\Algorithm\\' + str(json_data[key]['user_id']) + '\\图结构')
        for case in caseList:
            Fileinfo.append([])
            Fileinfo[i].append(str(json_data[key]['user_id']))
            Fileinfo[i].append(str(case['case_id']))
            Fileinfo[i].append(str(case['case_type']))
            endIndex= len(case['upload_records'])-1
            Fileinfo[i].append(str(case['upload_records'][endIndex]['code_url']))
            i += 1

        # print(key+':'+str(json_data[key]))

# os.makedirs('E:\\SampleTest\\可')
download_and_extract(Fileinfo, 'D:\\chengxu\\SoftwareEngineering\\probabilityTheory\\Algorithm')
