def solution(quiz):
    tmp = []
    ans = []

    for i in quiz:
        tmp = i.split(" ")
        if '+' in tmp: #덧셈
            add = int(tmp[0]) + int(tmp[2])
            ans.append("O") if add == int(tmp[4]) else ans.append("X")

        elif '-' in tmp: #뺄셈
            sub = int(tmp[0]) - int(tmp[2])
            ans.append("O") if sub == int(tmp[4]) else ans.append("X")

    return ans