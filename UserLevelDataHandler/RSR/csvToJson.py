import xlrd
import json

def excel(filename):
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_name('排序结果')
    user = []
    RSR = []
    for a in range(sheet.nrows):
        cells = sheet.row_values(a)
        data0 = cells[0]
        data1 = cells[20]
        user.append(data0)
        RSR.append(data1)
    return user, RSR


if __name__ == '__main__':
    user0, ARSR = excel('RSR AlgorithmScore0.xlsx')
    user1, DRSR = excel('RSR DebugScore0.xlsx')
    user2, FRSR = excel('RSR FirstConscore0.xlsx')
    dict = {}
    for a in range(1, len(user0)):
        tdict = {}
        tdict['debugRSR'] = DRSR[a]
        tdict['firstConstructionRSR'] = FRSR[a]
        tdict['algorithmRSR'] = ARSR[a]
        dict[user0[a]] = tdict
    json_str = json.dumps(dict, indent=4)
    with open('userAbilityRSR.json', 'w') as json_file:
        json_file.write(json_str)
