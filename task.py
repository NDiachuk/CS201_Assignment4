import pandas as pd
data = pd.read_csv('random_walk.csv')
distance=round((data['x']**2+data['y']**2)**0.5,1)
data['distance']=distance
print(data)