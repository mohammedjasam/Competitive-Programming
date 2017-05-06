import sys

def tau(n):
    d = 2
    ans = 1

    while d * d <= n:
        if n % d == 0:
            count = 0
            while n % d == 0:
                n //= d
                count += 1

            ans *= (count + 1)

        d += 1

    if n > 1:
        ans *= 2

    return ans


def solve(n):
    return (tau(n * n) + 1) // 2


def main():
    for line in sys.stdin:
        s = line.strip()
        n = int(s[2:])
        # print(s)
        print(solve(n))

main()
# Contact GitHub API Training Shop Blog About © 2017 GitHub, Inc. Terms Priv
