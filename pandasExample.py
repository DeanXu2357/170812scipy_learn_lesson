# numpy 是基於array 沒有欄位名稱&標籤
# pandas 則是基於numpy建構 有列表的標籤
# pandas兩個主要數據結構 Series & DataFrame
import pandas as pd
import numpy as np

v_s = pd.Series([1, "dsafds", "6", np.nan, 55, 2])

print(v_s)

df = pd.DataFrame(np.arange(44, 128).reshape(12, 7))
print(df)

dates = pd.date_range('20180901', periods=7)
print('Dates : ', dates)
weeks = ['w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7']
print('weeks : ', weeks)
timeSection = ['早', '中', '晚']

# pd.DataFrame 表格 參數一 array內容
#                   參數二 array 一列的目錄
#                   參數三 array 的項目
df1 = pd.DataFrame(np.random.randn(7, 7), index=dates,
                   columns=weeks)
df2 = pd.DataFrame(np.random.randn(7, 3), index=dates,
                   columns=['早', '中', '晚'])

# DataFrame 另一種生成方式
dict1 = {'Alice': ['2341', '1', '156'], 'Beth': [
    '9102', '0', '177'], 'Cecil': ['3258', '1', '165']}
print(pd.DataFrame(dict1))  # 直接顯示表格數據
print(pd.DataFrame(dict1, index=['age', 'sex', 'hight']))  # 為表格數據加上index

df3 = pd.DataFrame({
    '小數': pd.Series(1, index=list(range(4)),
                    dtype='float32'),
    '整數': np.array([3] * 4, dtype='int32'),
    '時間': pd.Timestamp('20170812'),
    '類別': pd.Categorical(["test", "train", "test", "train"])
})
print(df3)
# 數據表格的各式function
print('dtypes : ', df3.dtypes)
print('index : ', df3.index)
print('columns : ', df3.columns)
print('values : ', df3.values)
print('describe : ', df3.describe)

print('transpose matrix')
print(df3.T)

print(df3.sort_index(axis=1, ascending=False))
print(df3.sort_values(by='類別'))

print('"晚"的資料')
print(df2['晚'])
print('用[]抓資料項')
print(df2[0:3])

# select by label
print('select by label')
print(df2.loc['2018-09-03'])
print(df2.loc[:, ['早', '中']])

# select by position
print('select by position')
print(df2.iloc[3, 1])
print(df2.iloc[3:5, 1:3])

# select by ix
print('select by ix')
print(df2.ix[:3, ['中', '晚']])

# 加入判斷
print('判斷資料吐出')
print(df2[df2.中 < 0.02])

# 處理遺漏值
print('處理遺漏值')
df5 = pd.DataFrame(
    np.arange(21).reshape((7, 3)),
    index=dates,
    columns=timeSection
)
df5.iloc[0, 1] = np.nan
df5.iloc[1, 2] = np.nan

df51 = df5.dropna(
    axis=0,  # 0 : 對行進行操作 ,  1 : 對列進行操作
    how='any'  # 'any':存在NaN就Drop掉，'all':全部都是NaN才Drop掉
)

df52 = df5.fillna(value='000')  # NaN值用'nan'取代

if_df5 = df5.isnull()  # 判斷是否有缺失項目

# Imputer 記得補這個方法的範例
print(if_df5)
