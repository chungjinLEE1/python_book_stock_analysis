import matplotlib.pyplot as plt

# plt.plot([1, 2, 3, 4])
# plt.show()
##########################

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.show()
##########################

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# plt.axis([0, 6, 0, 20]) # [xmin, xman, ymin, ymax]
# plt.show()
##########################
import numpy as np

# 여러개 그래프 그리기
# 200ms 간격으로 균일하게 샘플된 시간
t = np.arange(0., 5., 0.2)

# 빨간 대쉬, 파란 사각형, 녹색 삼각형
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

###########################

