alphabets=["@","8","(","|)","3","#","6","[-]","|","_|","|<","1","[]\/[]","[]\[]","0","|D","(,)","|Z","$","']['","|_|","\/","\/\/","}{","`/","2"]
import sys
for i in range (10000):
    try:
        c=input()
        if c=="":
            sys.exit()
        c=c.upper()
        str=""
        l=[]
        for x in (c):
            l.append(x)
        for y in range(len(l)):
            if 65<=ord(l[y])<=90 or 97<=ord(l[y])<=122:
                try:
                    str+=alphabets[ord(l[y])-65]
                except:
                    str+=" "
            else:
                str+=l[y]
        print(str)
    except:
        break
