def solution(arr, divisor):
    ans = []

    for i in arr:
        if i%divisor == 0:
            ans.append(i)

    return sorted(ans) if len(ans) else [-1]