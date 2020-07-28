import numpy as np
import matplotlib.pyplot as plt


def getrsr(x1, x2, x3):
    return (0.4 * x1 + 0.4 * x2 + 0.2 * x3) / 30.0


plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
lables = np.array(['算法构建能力', 'debug能力', '第一次构建能力'])
nAttr = 3
data = np.array([0.4076586028929737 * 10, 0.6129143396525072 * 10, 0.4365073604228698 * 10])
angles = np.linspace(0, 2 * np.pi, nAttr, endpoint=False)
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))
fig = plt.figure(facecolor="white")
plt.subplot(111, polar=True)
plt.plot(angles, data, 'bo-', color='b', linewidth=1)
plt.fill(angles, data, facecolor='g', alpha=0.25)
# print(angles * 180 / np.pi)
plt.thetagrids([0., 120., 240.], lables)
plt.figtext(0.52, 0.95, '三项能力值雷达图(49823)', ha='center')
plt.grid(True)
plt.savefig('user49823’.jpg')
plt.show()
