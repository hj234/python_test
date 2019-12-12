'''
瞎搞

'''

import matplotlib.pyplot as plt
lables = 'frogs','hogs','dogs', 'logs'
sizes = 15, 20, 45, 10
colors = 'yellowgreen', 'gold', 'lightskyblue', 'lightcoral'
explode = 0, 0.1, 0, 0
plt.pie(sizes, explode = explode, labels = lables, colors = colors, autopct='%1.1f%%',shadow=True,startangle=50)

plt.axis('equal')
plt.show()