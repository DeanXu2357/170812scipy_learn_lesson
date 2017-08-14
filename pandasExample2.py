import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 讀取csv
data_fromcsv = pd.read_csv('ToDoList.xlsx - admin.csv')

dataD = data_fromcsv.dropna(axis=0, how='all')
# print(data_fromcsv)
# 轉檔
data_fromcsv.to_pickle('todolist.pickle')
data_fromcsv.to_json('todolist.json')

# 合併 Concat
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])
# 進行縱向合併
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
# print(res)

# TODO 回頭補上 JOIN合併 merge合併

# 隨機生成數據
data1 = pd.Series(np.random.randn(100), index=np.arange(100))
# pandas 可視化
data1.plot()
plt.show()
# print(data1)

# 監督式學習    你拿到的資料是你有標準答案的 有標籤的
# 非監督式學習  你沒有標準答案的 你定義分群  相較於監督式更複雜
# 半監督學習    有標籤或標準答案可以輔助
#
