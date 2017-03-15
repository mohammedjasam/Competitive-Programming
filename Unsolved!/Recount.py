### Works perfectly for 8/9 cases, Times out on the last case!!! Please help!


l=[] ## List to store the names of candidates
z={} ## Dictionary to store the frequencies

for i in range(949): ## Counter Value
    s=input()
    if s!="***":
        l.append(s)

        # for x in (l):
        z[s]=0 ## Creates a Dictionary with each name as key and assigns it a value 0

        for k, v in z.items():
            z[k]=l.count(k) ## Assigns the frequency
    else:
        break

maxi=max(z.keys(), key=(lambda key: z[key])) ## Finds out the max votes

c=0
for k, v in z.items():   ### Checks if there are more than one max value in the Dictionary
    if z[k]==z[maxi]:    ### If there are, then it returns
        c+=1
        if c==2:           ### Breaks if it finds atleast 2 ouccerences!!!
            break

if c>1:
    print("Runoff!")
else:
    print(maxi)
