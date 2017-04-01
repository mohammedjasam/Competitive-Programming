# import sys
#
# for line in sys.stdin:
#     if line[:-1]=='0':
#         break
#     else:
#         s,l=line.split()
#         c=0
#         print(l.find(s))
#             # c+=
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)

print(x)
plt.plot(x, x)
plt.plot(x, 2 * x)
plt.plot(x, 3 * x)
plt.plot(x, 4 * x)
plt.show()
# print(a1)
