N=int(input())
D=input().split(" ")

coinList=[]

for i in D:
    coinList+=[int(i)]

avrg=0
for j in coinList:
    avrg+=j/2

coinList.sort(reverse=True)

min=0
Sum=0

for k in coinList:
    Sum+=k
    if Sum>avrg:
        print(min+1)
        break
    else:
        min+=1