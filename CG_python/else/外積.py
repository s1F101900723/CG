# Numpy_Vector_Cross

# In[1]

import numpy as np
from scipy.linalg import norm
import matplotlib.pyplot as plt

# ここにcoordinate_3d()を実装
# ここにvisual_vector_3d()を実装

# FigureとAxes
fig = plt.figure(figsize = (6, 6))
ax = fig.add_subplot(111, projection='3d')

# 始点を設定
loc = [0, 0, 0]

# ベクトルu,vを定義
u = [1,2,3]
v = [0,1,0]

# uとvのベクトル積w
w = np.cross(u, v)

# wの大きさ（ノルム）を計算
w_norm = norm(w)

print("w = {}".format(w))
print("|w| = {:.3f}".format(w_norm))