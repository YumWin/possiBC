import json
from collections import Counter

class Elorating:
    ELO_RESULT_WIN = 1
    ELO_RESULT_LOSS = -1
    ELO_RESULT_TIE = 0

    ELO_RATING_DEFAULT = 1500

    ratingA = 0
    ratingB = 0

    def __init__(self, ratingA=ELO_RATING_DEFAULT, ratingB=ELO_RATING_DEFAULT):
        self.ratingA = ratingA
        self.ratingB = ratingB

    def setResult(self, result):
        scoreAwin = self.computeScore(self.ratingB, self.ratingA)
        scoreBwin = self.computeScore(self.ratingA, self.ratingB)

        # print(scoreAwin)
        # print(scoreBwin)
        return scoreAwin
        # score_adjust = 0
        # if result == self.ELO_RESULT_WIN:
        #     score_adjust = 1
        # elif result == self.ELO_RESULT_LOSS:
        #     score_adjust = 0
        # else:
        #     score_adjust = 0.5
        #
        # self.ratingA = self.ratingA + self.computeK(self.ratingA) * (score_adjust - scoreAwin)
        # self.ratingB = self.ratingB + self.computeK(self.ratingB) * (score_adjust - scoreBwin)

    def computeK(self, rating):
        if rating >= 2400:
            return 16
        elif rating >= 2100:
            return 24
        else:
            return 36

    def computeScore(self, rating1, rating2):
        return 1 / (1 + pow(10, (rating1 - rating2) / 400))

    pass

def rateCalcu(rateA,rateB):
    eloating=Elorating(rateA,rateB)
    return abs(2*eloating.setResult(-1)-1)

def userCalcuList(listA,listB):
    delta=0
    tempDict={}
    for caseA in listA:
        for caseB in listB:
            if(caseB["case_type"]==caseA["case_type"]):
                delta+=rateCalcu(caseA["Score"],caseB["Score"])
                tempDict[caseB["case_type"]]=rateCalcu(caseA["Score"],caseB["Score"])
    tempDict["delta"]=delta
    return tempDict

def userCalcu(listA,listB):
    delta=0
    for caseA in listA:
        for caseB in listB:
            if(caseB["case_type"]==caseA["case_type"]):
                delta+=rateCalcu(caseA["Score"],caseB["Score"])
    return delta

def caseTypeRecFunc():
    with open('./realData/UserAbilityTypeLevel.json', 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
        # 创建字典
        info_dict={}
        for key in json_data:
            userList=[]
            for user_case in json_data[key]:
                temp_dict={}
                temp_dict["case_type"]=user_case["case_type"]
                temp_dict["Score"]=0.4*user_case["algorthmScore"]+0.4*user_case["debugScore"]+0.2*user_case["firstConsScore"]
                userList.append(temp_dict)
            info_dict[key]=userList
        # print(info_dict)
        # print(rateCalcu(1500,1600))
        result_dict={}
        for keyA in info_dict:
            temp_dict={}
            list_dict={}
            for keyB in info_dict:
                if(keyA!=keyB):
                    temp_dict[keyB]=userCalcu(info_dict[keyA],info_dict[keyB])
                    list_dict[keyB]=userCalcuList(info_dict[keyA],info_dict[keyB])
            end_dict={}
            temp_list = sorted(temp_dict, key=temp_dict.__getitem__)
            temp_list.reverse()
            temp_list=temp_list[0:5]
            for element in temp_list:
                end_dict[element]=list_dict[element]
            result_dict[keyA]=end_dict
        # dumps 将数据转换成字符串
        info_json = json.dumps(result_dict, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False)
        # 显示数据类型
        print(type(info_json))
        f = open('./realData/caseTypeRec.json', 'w', encoding='utf8')
        f.write(info_json)

def userAbilityCalcu(dictA,dictB):
    delta=0

    for keyA in dictA:
        for keyB in dictB:
            if(keyA==keyB):
                delta+=1-rateCalcu(dictA[keyA]*1000,dictB[keyB]*1000)
    return delta

def userAbilityCalcuList(dictA,dictB):
    delta=0
    tempDict={}
    for keyA in dictA:
        for keyB in dictB:
            if(keyA==keyB):
                delta+=1-rateCalcu(dictA[keyA]*1000,dictB[keyB]*1000)
                tempDict[keyB] = 1-rateCalcu(dictA[keyA]*1000,dictB[keyB]*1000)
    tempDict["delta"] = delta
    return tempDict

def abilityRecFunc():
    with open('./realData/UserAbilityLevel.json', 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
        # 创建字典
        info_dict={}
        for keyA in json_data:
            temp_dict={}
            list_dict={}
            for keyB in json_data:
                if(keyA!=keyB):
                    temp_dict[keyB]=userAbilityCalcu(json_data[keyA],json_data[keyB])
                    list_dict[keyB]=userAbilityCalcuList(json_data[keyA],json_data[keyB])
            end_dict={}
            temp_list = sorted(temp_dict, key=temp_dict.__getitem__)
            temp_list.reverse()
            temp_list=temp_list[0:5]
            for element in temp_list:
                end_dict[element]=list_dict[element]
            info_dict[keyA]=end_dict
    # dumps 将数据转换成字符串
    info_json = json.dumps(info_dict, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False)
    # 显示数据类型
    print(type(info_json))
    f = open('./realData/abilityRec.json', 'w', encoding='utf8')
    f.write(info_json)


# caseTypeRecFunc()
abilityRecFunc()