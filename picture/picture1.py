import numpy as np
import matplotlib.pyplot as plt


def getrsr(x1, x2, x3):
    return (0.4 * x1 + 0.4 * x2 + 0.2 * x3) / 30.0


plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
lables = np.array(['查找算法', '排序算法', '树结构', '数字操作', '数组', '图结构', '线性表', '字符串'])
nAttr = 8
data = np.array([getrsr(234.8785317352681, 319.99504802754655, 211.4628228646248),
                 getrsr(274.4375825834956, 430.18565746895456, 260.71252816399806),
                 getrsr(253.0781729934846, 278.0895107579895, 167.4751304818027),
                 getrsr(275.9241742209988, 306.6459105668957, 234.05743064924715),
                 getrsr(250.177204156439, 193.0810938975884, 157.7242012487926),
                 getrsr(239.71326425818452, 275.46388971831186, 235.96362690214892),
                 getrsr(251.74271582577097, 278.39941102547346, 181.1483751175285),
                 getrsr(213.70544631243826, 323.2956824038571, 182.98785226908083)])
angles = np.linspace(0, 2 * np.pi, nAttr, endpoint=False)
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))
fig = plt.figure(facecolor="white")
plt.subplot(111, polar=True)
plt.plot(angles, data, 'bo-', color='b', linewidth=2)
plt.fill(angles, data, facecolor='g', alpha=0.25)
# print(angles * 180 / np.pi)
plt.thetagrids([0., 45., 90., 135., 180., 225., 270., 315.], lables)
plt.figtext(0.52, 0.95, '各类题型能力值雷达图(49823)', ha='center')
plt.grid(True)
plt.savefig('user49823.jpg')
plt.show()
