# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 18:34:20 2023

@author: Hannah
"""

from ArrayDeque import ArrayDequeMaxlen

     
        
AQM = ArrayDequeMaxlen(20)


print('Adding last')
for i in range(100):
    AQM.append(i)
    print (i, AQM._data)
    
print('\nDelete 80', AQM.remove(80), AQM._data, AQM._front)
    


    
print ('\nAdding first')
for i in range(20, 10, -1):
    AQM.appendleft(i)
    print (i, AQM._data)
    
    
print(AQM._front)
    

    
print('\nPerforming the removals')
while not AQM.is_empty():
    print ('Remove first', AQM[0], AQM.popleft(), 'Remove last', AQM[-1],  AQM.pop())