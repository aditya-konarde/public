import random
import sys
import os

pi_tuple = (3,1,4,1,5,9)

#Typecasting the tuple into a new list
new_list = list(pi_tuple)

#Typecasting a list into a tuple
new_tuple = tuple(new_list)

print(new_tuple)
print(new_list)

#legal, as we can append to list
new_list.append(19)

#Illegal operation: tuples are immutable
#new_tuple.append(19)

print(len(new_tuple))
