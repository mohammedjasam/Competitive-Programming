N = int(input())

log={}
for i in range(N):
    b,a=input().split()
    if b=='entry':
        if not(a in log):
            print(a+ " entered")
            log[a]=b
            # print(log)
        else:
            print(a+ " entered (ANOMALY)")
            # log[a]=b
            # print(log)
    elif b=='exit':
        if (a in log):
            try:
                print(a+ " exited")
                del(log[a])
                # print(log)
            except:
                pass
        else:
            try:
                print(a+ " exited (ANOMALY)")
                # del(log[a])
                # print(log)
            except:
                pass
                # print(log)
#
# print(log)
