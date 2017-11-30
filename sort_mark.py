input_data = list(map(int, input().split()))
evaluation = [0] * 6
for now in input_data:
    evaluation[now] += 1
for now in range(len(evaluation)):
    print((str(now) + ' ') * evaluation[now], end=' ')
# варант вывода как в других ЯП
'''print()
for now in range(len(evaluation)):
    for i in range(evaluation[now]):
        print(now, end=' ')'''