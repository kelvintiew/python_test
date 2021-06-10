# -*- coding: utf-8 -*-
# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
# --結束--批改評分使用，請勿變動

# 載入 matplotlib.pyplot 並縮寫為 plt
import matplotlib.pyplot as plt

data1 = [1, 4, 9, 16, 25, 36, 49, 64]
data2 = [1, 2, 3, 6, 9, 15, 24, 39]
seq = [1, 2, 3, 4, 5, 6, 7, 8]

# 數據及線條設定
plt.plot(seq, seq, "r--", seq, seq**2,'bs', seq,seq**3,'g^')
# 軸刻度
plt.axis('0,0','8,70')
# 圖表標題
plt.title("x_tick")
# X軸標題
plt.xlabel("y-Value")
# Y軸標題
plt.ylabel("x-Value")

# 輸出圖片檔案
plt.savefig('chart.png')
plt.show()
