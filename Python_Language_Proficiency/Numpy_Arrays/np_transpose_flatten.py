import numpy

m=int(raw_input().split()[0])
arr=[]
while m!=0:
    arr.append(map(int,raw_input().split()))
    m-=1
print numpy.array(arr).transpose()
print numpy.array(arr).flatten()


