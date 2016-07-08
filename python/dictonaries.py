import sys
import random
import os

'''
Creating a dictionary
A dictionary is a key:value pair
You cannot join dictionaries like lists
'''

super_heroes = {
'spidey':'peter parker',
'batman':'bruce wayne',
'superman':'clark kent',
'hanuman': 'lol'
}

#Printing the corresponding value to the key
print('Real name of spiderman is:',super_heroes['spidey'])

#Deleting an entry
del super_heroes['hanuman']
print(super_heroes)
print()

#Getting the length
print('There are ', len(super_heroes), ' super heroes in our database')
print()
#Modifying a value
super_heroes['superman'] = 'clarke kent'
print(super_heroes)
print()
#Getting values
print(super_heroes.values())
print(super_heroes.get('superman'))
print()

#Getting keys
print(super_heroes.keys())
