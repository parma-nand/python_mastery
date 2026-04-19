print("Shri Ganeshay Namah")

a,b,c="hey"
print(a)
print(b)

d=1,2,3
print(d)
p,q,r=d
print(p)
print(q)
print(r)

# Swapping
a=2
b=3
a,b=b,a
print(a,b)

# Function Packing,Unpacking
def get_data():
    return 100,200 #Packing
x,y=get_data()
print(x)
print(y)

# Mutability
a=[1,2,3]
print(a)
a.append(4)
print(a)
a.remove(2)
print(a)
a[0]=5
print(a)

b=(1,2,3)   
print(b)

t=([1],3) # inside tuple,list is mutable
print(t)
t[0].append(6)
print(t)

from collections import defaultdict

sentence = "apple banana apple orange banana apple"
words = sentence.split()

freq = defaultdict(int)

for w in words:
    freq[w] += 1

print(freq)