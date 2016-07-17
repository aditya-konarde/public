'''
Python 30 days warmup
Day 2
17-07-2016
Input Format
The first line contains an integer, . 
The second line contains a double, . 
The third line contains a string, .

Output Format
Print the sum of both integers on the first line,
the sum of both doubles (scaled to  decimal place) on the second line,
and then the two concatenated strings on the third line.
'''

i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
i2 = 0
d2 = 0
s2 = 0
# Read and save an integer, double, and String to your variables.
i2 = int(input())
d2 = float(input())
s2 = input()
# Print the sum of both integer variables on a new line.
print(i+i2)
# Print the sum of the double variables on a new line.
print(d+d2)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s+s2)
