import numpy as np
data = np.genfromtxt('day1.txt', delimiter='/n')
advent = []

for x in range(0,len(data)):
    y=int(data[x])
    advent.append(y)

for i in range(0,200):
    for j in range(0,199):
        if i!=j:
            if advent[i]+advent[j]==2020:
                
                print(f'Product {advent[i]*advent[j]} ')
                break
            
