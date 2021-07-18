# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

a = int(input())
b = int(input())

t = math.degrees(math.atan(a/b))

print(str(round(t))+chr(176))