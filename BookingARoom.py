total,booked = map(int,input().split())

log={}
for i in range(total):
    log[i+1]=0
for i in range(booked):
    room_no=int(input())
    log[room_no]=1

if total>booked:
    for k, v in log.items():
        if log[k]==0:
            print(k)
            break
elif total==booked:
    print("too late")
