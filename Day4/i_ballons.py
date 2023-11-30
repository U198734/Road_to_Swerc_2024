import sys
n = int(sys.stdin.readline().strip()) # num infladors
balloons = [i+1 for i in range(n)]
cap = list(map(int,sys.stdin.readline().strip().split()))
 
 
cap.sort()
maxx = -0.1
minn = 10000000
for i in range(n):
    divv = cap[i] / balloons[i]
    if(divv < minn):
        minn = divv
    if(divv > maxx):
        maxx = divv
        
if(maxx > 1):
    print("-1")
elif(minn == 0.0):
    print(int(minn))
else:
    print(minn)



