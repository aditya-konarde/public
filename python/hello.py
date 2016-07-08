import random
import sys
import os

print("Hello world")

#comment

'''
Multiline
comment
'''

#Strings
name = "Aditya"
print(name)

#Arithmetic
print("5 + 2 =", 5+2)
print("5 - 2 =", 5-2)
print("5 / 2 =", 5/2)
print("5 * 2 =", 5*2)
print("5 ** 2 =", 5**2)
print("5 % 2 =", 5%2)
print("5 // 2 =", 5//2)

#Order of operations is BODMAS, so put braces everywhere!

#Ignoring Characters
quote1 = "\"A Lannister always pays"
quote2 = " his debt\""
print(quote1 + quote2)

#Multi line quotes
multi_line_quote = '''A Lion does not concern himself
with the opinion of sheep
'''
print(multi_line_quote)

#Passing strings to print
print("%s %s %s" %('I like the quotes', quote1+quote2, multi_line_quote))
