# import numpy as np

# s = "hello world"
# ascii = np.fromstring(s, dtype=np.uint8)
# tol = []
# for i in range(len(ascii)):
#     num = abs(ascii[i]-ascii[i+1])
#     tol.append(num)
# return tol

import numpy as np
tol = []
s = "hello world"
i = 0
class Solution:
    def scoreOfString(self, s: str) -> int:     
       ascii = np.fromstring(s, dtype=np.uint8)
        
        for i in range(len(ascii)):
            num = abs(ascii[i]-ascii[i+1])
            tol.append(num)
        return tol
