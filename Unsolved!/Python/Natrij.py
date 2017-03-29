from datetime import datetime
from datetime import timedelta
s1 = input()
AH,AM,AS=s1.split(":")
s2 = input()
BH,BM,BS=s2.split(":")

FMT = '%H:%M:%S'
tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
# print(tdelta)
if tdelta.days < 0:
    tdelta = timedelta(days=0,
                seconds=tdelta.seconds, microseconds=tdelta.microseconds)
s=""
s=str(tdelta)
H,M,S=s.split(":")
if len(H)==1:
    H='0'+str(H)
print(str(H)+":"+str(M)+":"+str(S))

# # for i in range(2):
# H,M,S=map(str,input().split(':'))
# DH,DM,DS=map(str,input().split(":"))
# TH,TM,TS=0,0,0
# H=int(H)
# M=int(M)
# S=int(S)
# DH=int(DH)
# DM=int(DM)
# DS=int(DS)
# l=[]
# # print(H,M,S)
# TotalSec=0
# # if DH<H:
# #     TotalSec=86400
# if H>0:
#     if M>0:
#         TotalSec=(H*60+M)*60+S
#     elif M==0:
#         TotalSec=(H*60)*60+S
# elif H==0:
#     if M>0:
#         TotalSec=(M)*60+S
#     elif M==0:
#         TotalSec=S
# # print(TotalSec)
# l.append(TotalSec)
# TotalSec=0
# if DH<H:
#     TotalSec=86400
# if DH>0:
#     if DM>0:
#         TotalSec+=(DH*60+DM)*60+DS
#     elif DM==0:
#         TotalSec+=(DH*60)*60+DS
# elif DH==0:
#     if DM>0:
#         TotalSec+=(DM)*60+DS
#     elif DM==0:
#         TotalSec+=DS
# # print(TotalSec)
# l.append(TotalSec)
#
# # print(l)
# # print((l[1]-l[0])%86400)
#
# finSec=(l[1]-l[0])
#
#
# print(finSec)
#
# # print(finSec%86400)
