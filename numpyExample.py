import numpy as np

arrayEx = np.array([
    [1, 2, 3],
    [3, 4, 6]
])

print(arrayEx)
print('dim', arrayEx.ndim)  # 維度
print('shape', arrayEx.shape)   # 第一層兩個物件 第二層三個物件
print('size', arrayEx.size)    # 總共有幾個物件

array_a = np.arange(8).reshape(2, 4)
print('array_a = ', array_a)
array_b = array_a.T
print('array_b = ', array_b)  # 轉置矩陣
print(np.dot(array_a, array_b))  # 矩陣內積

array_c = np.array([1, 3, 6])
array_d = np.array([2, 46, 7])
print(np.hstack((array_c, array_d)))  # 合併

print(np.vsplit(array_a, 2))  # 矩陣切割
print(np.hsplit(array_a, 2))
