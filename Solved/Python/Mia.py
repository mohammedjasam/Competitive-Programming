while True:
    a, b, c, d = map(int, input().split())
    if a == 0 and b == 0 and c == 0 and d == 0:
        break
    a, b = sorted([a, b])
    c, d = sorted([c, d])

    i = b*10 + a
    j = d*10 + c

    if i == j:
        print('Tie.')
    elif i == 21:
        print ('Player 1 wins.')
    elif j == 21:
        print('Player 2 wins.')
    elif a == b:
        if c == d:
            if a > c:
                print('Player 1 wins.')
            else:
                print('Player 2 wins.')
        else:
            print('Player 1 wins.')
    elif c == d:
        print('Player 2 wins.')
    else:
        if i > j:
            print('Player 1 wins.')
        else:
            print('Player 2 wins.')



# import sys
#
# for line in sys.stdin:
#     line=line[:-1]
#     if line == '0 0 0 0':
#         break
#     else:
#         doubly=['11','22','33','44','55','66']
#         s0,s1,r0,r1=line.split()
#         listt=['1','2','3','4','5','6']
#         if (s0 in listt) and (s1 in listt) and (r0 in listt) and (r1 in listt):
#             if ((s0=='1' and s1=='2') or (s1=='1' and s0=='2')) and ((r0=='1' and r1=='2') or (r1=='1' and r0=='2')):
#                 print('Tie.')
#             elif (s0=='1' and s1=='2') or (s1=='1' and s0=='2'):
#                 print("Player 1 wins.")
#             elif (r0=='1' and r1=='2') or (r1=='1' and r0=='2'):
#                 print("Player 2 wins.")
#             else:
#                 s=s0+s1
#                 r=r0+r1
#                 srtS=""
#                 srtR=""
#                 for x in sorted(s):
#                     srtS+=x
#                 for x in sorted(r):
#                     srtR+=x
#                 if (not(s in doubly)) and (not(r in doubly)):
#                     if srtS==srtR:
#                         print("Tie.")
#                     elif srtS>srtR:
#                         print("Player 1 wins.")
#                     elif srtS<srtR:
#                         print("Player 2 wins.")
#                 elif (s in doubly) and (r in doubly):
#                     if doubly.index(s)==doubly.index(r):
#                         print('Tie.')
#                     elif doubly.index(s)>doubly.index(r):
#                         print('Player 1 wins.')
#                     elif doubly.index(s)<doubly.index(r):
#                         print('Player 2 wins.')
#                 elif (s in doubly) and (not(r in doubly)):
#                     print('Player 1 wins.')
#                 elif (r in doubly) and (not(s in doubly)):
#                     print('Player 2 wins.')
