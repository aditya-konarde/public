import random
import sys
import os

#Creating a List.
aryas_list = ['Cersie', 'Joffrey', 'Illyn Payne', 'The hound']
print('First name: ', aryas_list[0])
print()

#Lists can be modified
aryas_list[0] = 'the mountain'
print('First name: ', aryas_list[0])
print()
#Printing a subset of the List
print(aryas_list[1:3])

#Creating lists of Lists
checked_off = ('Joffrey', 'The Hound')
Total_list = (aryas_list, checked_off)
print(Total_list)
print()
print(Total_list[0][1], ' is a dead king')
print()
#list operations
aryas_list.append('Ser Meryn')
print('\nAdd Ser Meryn',aryas_list)

aryas_list.insert(2,'Ser Amory')
print('\nInsert Ser Amory at position 2',aryas_list)

aryas_list.sort()
print('\nSorted list', aryas_list)

aryas_list.reverse()
print('\n Reversing the list',aryas_list)

del aryas_list[3]
print('\n Deleting element at position 3',aryas_list)

#Combining Lists
print('Number of people in aryas list', len(aryas_list))
