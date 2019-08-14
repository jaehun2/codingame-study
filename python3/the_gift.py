import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# 1. budgets에 budget 저장
# 2. budgets의 sum이 c 보다 작은가? yes: is_impossible = True
# 3. budgets를 내림차순 정렬
# 4. spents 리스트 만들기(size: n, 값: 0), total = 0
# 5. not is_impossible and while total < c
# 6. for 돌리면서(가장 큰 budget에서부터 1씩 차감. 한바퀴 돌면 도돌이)
#   a. budget[i]가 0보다 클 경우에만, budgets[i]에 -1, spents[i]에 +1
#   b. total에 +1
#   c. total >= c 이면 break
# 7. spents 오름차순 정렬 & spents 한줄씩 출력

# n = 3
# c = 100
n = int(input())
c = int(input())

budgets = []
# budgets.append(3)
# budgets.append(100)
# budgets.append(100)
for i in range(n):
    b = int(input())
    budgets.append(b)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

budget_sum = sum(budgets)
if budget_sum < c:
    is_impossible = True
else:
    is_impossible = False

budgets.sort(reverse=True)

spents = []
for i in range(n):
    spents.append(0)
total = 0

if is_impossible:
    print("IMPOSSIBLE")
else:
    while total < c:
        for i in range(n):
            if budgets[i] > 0:
                budgets[i] -= 1
                spents[i] += 1
                total += 1
                if total >= c:
                    break
    spents.sort()
    for i in range(n):
        print(spents[i])
