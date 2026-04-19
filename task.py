import pandas as pd
data = pd.read_csv('random_walk.csv')
distance=round((data['x']**2+data['y']**2)**0.5,1)
data['distance']=distance
print(data)
print("max distance",max(data['distance']))
average=round(sum(data['distance'])/len(data['distance']),3)
print("average distance",average)
print("avarage <",data[(data['distance']>average)])
