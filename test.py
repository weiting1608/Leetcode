from datetime import datetime, timedelta
start_date = datetime.now()
processid = start_date.strftime('%Y%m%d-%H%M%S-%f')
print(processid)
import numpy as np
a = np.zeros([3,2,5])
b = np.zeros([3,2,5])
for i in range(5):
    b[:,:,i] = i

print(a)
print(b)
# c = np.subtract(b-a)
print(np.subtract(b-a))