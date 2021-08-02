N=int(input("Enter the number of coins "))
D=input("Enter the denomination of each coin separated by spaces ")

Splt=D.split(" ")
coinList=[]

for i in Splt:
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
        print("The minimum required number of coins are ", min+1)
        break
    else:
        min+=1