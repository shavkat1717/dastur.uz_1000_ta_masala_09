a=int(input("Birinchi sonni kiriting a => "))
b=int(input("Ikkinchi sonni kiriting b => "))
c=int(input("Uchinchi sonni kiriting c => "))
import math
def InvertDigit(x):
    while x>0:
        q=x%10
        print(q,end=(""))
        x=math.floor(x/10)
print("\n")
InvertDigit(a)
print("\n")
InvertDigit(b)
print("\n")
InvertDigit(c)