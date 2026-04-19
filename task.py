import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('random_walk.csv')
distance=round((data['x']**2+data['y']**2)**0.5,1)
data['distance']=distance
print(data)
print("max distance",max(data['distance']))
average=round(sum(data['distance'])/len(data['distance']),3)
print("average distance",average)

filtered_walk=data[data['distance']>average]
print("avarage <",filtered_walk)
filtered_walk.to_json('filtered_walk.json')
plt.scatter(data['x'],data['y'],color='green')
plt.title('random walk')
plt.xlabel('x',fontsize=20)
plt.ylabel('y',fontsize=20)
plt.legend(['trajectory'] ,fontsize=10,loc='lower right')
plt.scatter([0,-2], [0,-8], color='blue', s=80)
plt.show()

