N =  input()
sum=0
for i in range(int(N)):
    tmp=input()
    l=len(tmp)
    sum+=(int(tmp[-l:-1])**int(tmp[-1:]))
print(sum)
