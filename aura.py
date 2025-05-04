import matplotlib.pyplot as plt
from datetime import datetime

city=['New Delhi','Bengaluru','Pune','Darjeeling','Kolkata', 'Chennai']
temp=[53,89,23,43,54,32]
colors=['green','red','blue','magenta','orange','yellow']
plt.bar(city,temp,color=colors)
plt.xlabel('City Names')
plt.ylabel('Temperature')

x=datetime.now().date()
plt.title('City Wise Temp.' + str(x) )
plt.savefig('D://city.pdf')
plt.show()
