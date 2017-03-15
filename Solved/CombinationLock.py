while True:
    a, b, c, d=map(int,input().split())
    if (a == 0 and b == 0 and c == 0 and d == 0):
        break
    a *= 9;
    b *= 9;
    c *= 9;
    d *= 9;
    ans = 720; # 2 full turns
    ans += (a-b+360)%360;
    ans += 360;
    ans += (c-b+360)%360;
    ans += (c-d+360)%360;
    print(ans)
