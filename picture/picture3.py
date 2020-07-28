import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
radar_labels = np.array(['debug能力', '第一次构建能力', '算法构建能力'])
nAttr = 3
data = np.array([[0.6129143396525072 * 10, 0.4242713767910857 * 10, 0.8066622893344955 * 10],
                 [0.4076586028929737 * 10, 0.3636751771958072 * 10, 0.3786750564816787 * 10],
                 [0.4365073604228698 * 10, 0.4136438123460278 * 10, 0.5086348434501778 * 10]])
data_labels = ('user49823', 'user60778(推荐位第一)', 'user60670(推荐位第五)')
angles = np.linspace(0, 2 * np.pi, nAttr, endpoint=False)
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))
fig = plt.figure(facecolor="white")
plt.subplot(111, polar=True)
plt.plot(angles, data, 'o-', linewidth=1, alpha=0.2)
plt.fill(angles, data, alpha=0.25)
# print(angles * 180 / np.pi)
plt.thetagrids([0., 120., 240], radar_labels)
plt.figtext(0.52, 0.95, '相似型匹配雷达图(49823)', ha='center', size=20)
legend = plt.legend(data_labels, loc=(0.94, 0.80), labelspacing=0.1)
plt.setp(legend.get_texts(), fontsize='large')
plt.grid(True)
plt.savefig('相似型匹配(49823).jpg')
plt.show()
