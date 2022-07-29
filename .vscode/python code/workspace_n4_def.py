min_sit = 2
max_sit = 10
sit = 100
memo = {}

def question(remain, min_sit):
    key = str([remain, min_sit])

    if key in memo:
        return memo[key]

    if remain == 0:
        return 1

    if remain < 0:
        return 0

    count = 0
    
    for i in range(min_sit, max_sit + 1):
        count += question(remain - i, i)

    memo[key] = count

    return count

print(question(sit, min_sit))

print(memo)








