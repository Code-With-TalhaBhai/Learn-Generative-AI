
# Actually its a docString
'''
    # This is markdown
'''

x = 100

'x: ',x


import numpy as np
import matplotlib.pyplot as plt

arr = np.random.normal(1,1,size=100)
fig,ax = plt.subplots()
ax.hist(arr,bins=20);

fig; # Draw matplotlib chart