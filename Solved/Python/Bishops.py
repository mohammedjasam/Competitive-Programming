# n = int(input())
import sys
for n in sys.stdin:
    n=int(n)
    print(n if n<=2 else n+(n-2))
