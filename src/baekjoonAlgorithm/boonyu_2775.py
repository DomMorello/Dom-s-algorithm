# 이 아파트에 거주를 하려면 조건이 있는데, “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다”
# 는 계약 조항을 꼭 지키고 들어와야 한다.

# 아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라. 
# 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

# 입력
# 첫 번째 줄에 Test case의 수 T가 주어진다. 그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 
# 두 번째 줄에 정수 n이 주어진다. (1 <= k <= 14, 1 <= n <= 14)

# 출력
# 각각의 Test case에 대해서 해당 집에 거주민 수를 출력하라.

# 0.1 -> 1  1.1 ->  1  2.1 ->  1  3.1 -> 1
# 0.2 -> 2  1.2 ->  3  2.2 ->  4  3.2 -> 5
# 0.3 -> 3  1.3 ->  6  2.3 -> 10  3.3 -> 15
# 0.4 -> 4  1.4 -> 10  2.4 -> 20  3.4 -> 35
# 0.5 -> 5  1.5 -> 15  2.5 -> 35  3.5 -> 70
# 0.6 -> 6  1.6 -> 21  2.6 -> 56  3.6 -> 126
 
import sys

def sumidx(arr, start, end):
    i = start
    ret = 0
    while i <= end:
        ret += arr[i]
        i += 1
    return ret

def solution(k, n):
    ret = []
    i = 0
    while i < 15:
        ret.append(list(range(1,16)))
        i += 1
    i = 1
    while i <= k:
        j = 1
        while j <= n:
            ret[i][0] = 1
            ret[i][j] = sumidx(ret[i - 1], 0, j)
            j += 1
        i += 1
    print(ret[i - 1][j - 2])
    
t = int(input())

ks = []
ns = []
while t:
    k = int(input())
    n = int(input())
    if not (k >= 1 and k <= 14) or not (n >= 1 and n <= 14):
        print('error')
        sys.exit()
    ks.append(k)
    ns.append(n)
    t -= 1

k_len = len(ks)
i = 0
while i < k_len:
    solution(ks[i], ns[i])
    i += 1