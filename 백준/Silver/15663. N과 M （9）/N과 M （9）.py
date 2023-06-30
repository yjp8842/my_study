def solve(idx, N, M):
  if idx == M:
    for i in stack:
      print(i, end=' ')
    print()
    return

  check = 0
  for i in range(N):
    if dat[i] == 1 or check == lists[i]:
      continue
    stack.append(lists[i]) # 1번
    dat[i] = 1
    check = lists[i]
    solve(idx + 1, N, M)  # 2번
    stack.pop()     # 3번
    dat[i] = 0

N, M = map(int, input().split())
lists = list(map(int, input().split()))
lists.sort()
stack = []
dat = [0] * (N + 1)
solve(0, N, M)
