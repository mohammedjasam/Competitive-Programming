l=[]
tsum=0 # calculates the total sum
for i in range(9):
    l.append(int(input())) # Takes the input and appends it into the list
tsum=sum(l)
c=l # temporary list to remove the fake dwarfs
x=0   # Temporary variables for i
y=0   # Temporary variables for j
for i in range(9):
    for j  in range(9):
        if i!=j and (tsum-l[i]-l[j]==100): # Check if after the two removed values, the list adds up to the desired value!
            x=i
            y=j
if x<y:
    del c[x]
    del c[j-1]
elif y<x:
    del c[y]
    del c[x-1]
for x in c:
    print(x)
