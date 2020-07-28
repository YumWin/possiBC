import json
import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy.stats import norm


def rank(data, frame):
    # 对原始数据按照整秩法编秩
    for i, X in enumerate(data.columns):
        frame[f'X{str(i + 1)}：{X}'] = data.iloc[:, i]
        frame[f'R{str(i + 1)}：{X}'] = data.iloc[:, i].rank(method="dense")
    return frame


def comRSR(frame, n, p):
    # 计算RSR
    weight = 1 / p
    frame['RSR'] = (frame.iloc[:, 1::2] * weight).sum(axis=1) / n
    frame['RSR_Rank'] = frame['RSR'].rank(ascending=False)
    return frame


def drawRSR(RSR, n):
    # 绘制RSR分布表
    RSR_RANK_DICT = dict(zip(RSR.values, RSR.rank().values))
    dist = pd.DataFrame(index=sorted(RSR.unique()))
    dist['f'] = RSR.value_counts().sort_index()
    dist['Σ f'] = dist['f'].cumsum()
    dist['平均秩次'] = [RSR_RANK_DICT[i] for i in dist.index]
    dist['累积频率'] = dist['平均秩次'] / n
    dist.iat[-1, -1] = 1 - 1 / (4 * n)
    dist['Probit'] = 5 - norm.isf(dist.iloc[:, -1])
    return dist


def cre(dist):
    # 计算回归方程
    r0 = np.polyfit(dist['Probit'], dist.index, deg=1)
    # print(sm.OLS(Distribution.index, sm.add_constant(Distribution['Probit'])).fit().summary())
    if r0[1] > 0:
        print(f"\n回归直线方程为：y = {r0[0]} Probit + {r0[1]}")
    else:
        print(f"\n回归直线方程为：y = {r0[0]} Probit - {abs(r0[1])}")
    return r0


def useCRE(frame, dist, r0):
    # 代入回归方程
    frame['Probit'] = frame['RSR'].apply(lambda item: dist.at[item, 'Probit'])
    frame['RSR Regression'] = np.polyval(r0, frame['Probit'])
    return frame


def rsr(data):
    n, p = data.shape
    frame = pd.DataFrame()
    frame = rank(data, frame)
    frame = comRSR(frame, n, p)
    distribution = drawRSR(frame['RSR'], n)
    r0 = cre(distribution)
    frame = useCRE(frame, distribution, r0)
    return frame, distribution


def rsrToExcel(data, file_name):
    frame, distribution = rsr(data)
    excel_writer = pd.ExcelWriter(file_name)
    #frame.sort_values(by='RSR Regression', ascending=False,inplace=True)
    frame.to_excel(excel_writer, '排序结果')
    distribution.to_excel(excel_writer, 'RSR分布表')
    excel_writer.save()
    return frame, distribution


if __name__ == '__main__':
    with open('UserAbilityTypeLevel.json', 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
        userlist = []
        usercase = []
        casetype = []
        AlgorthmScore = []
        DebugScore = []
        FirstConscore = []
        temp1 = []
        temp2 = []
        temp3 = []
        for user in json_data:
            userlist.append(user)
            usercase.append(json_data[user])
        numOfUser = len(userlist)
        numOfProtype = len(usercase[0])
        for a in range(0, numOfProtype):
            casetype.append(usercase[0][a]['case_type'])
        print(usercase)
        for b in range(0, numOfProtype):
            for a in range(0, numOfUser):
                temp1.append(usercase[a][b]['algorthmScore'])
                temp2.append(usercase[a][b]['debugScore'])
                temp3.append(usercase[a][b]['firstConsScore'])
            AlgorthmScore.append(temp1[:])
            temp1.clear()
            DebugScore.append(temp2[:])
            temp2.clear()
            FirstConscore.append(temp3[:])
            temp3.clear()
        data0 = pd.DataFrame({casetype[0]: DebugScore[0],
                             casetype[1]: DebugScore[1],
                             casetype[2]: DebugScore[2],
                             casetype[3]: DebugScore[3],
                             casetype[4]: DebugScore[4],
                             casetype[5]: DebugScore[5],
                             casetype[6]: DebugScore[6],
                             casetype[7]: DebugScore[7]},
                            index=userlist, columns=casetype)
        rsrToExcel(data0, 'RSR DebugScore0.xlsx')
        data1 = pd.DataFrame({casetype[0]: AlgorthmScore[0],
                             casetype[1]: AlgorthmScore[1],
                             casetype[2]: AlgorthmScore[2],
                             casetype[3]: AlgorthmScore[3],
                             casetype[4]: AlgorthmScore[4],
                             casetype[5]: AlgorthmScore[5],
                             casetype[6]: AlgorthmScore[6],
                             casetype[7]: AlgorthmScore[7]},
                            index=userlist, columns=casetype)
        rsrToExcel(data1, 'RSR AlgorithmScore0.xlsx')
        data2 = pd.DataFrame({casetype[0]: FirstConscore[0],
                             casetype[1]: FirstConscore[1],
                             casetype[2]: FirstConscore[2],
                             casetype[3]: FirstConscore[3],
                             casetype[4]: FirstConscore[4],
                             casetype[5]: FirstConscore[5],
                             casetype[6]: FirstConscore[6],
                             casetype[7]: FirstConscore[7]},
                            index=userlist, columns=casetype)
        rsrToExcel(data2, 'RSR FirstConscore0.xlsx')