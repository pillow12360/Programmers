def solution(lottos, win_nums):
    answer = []
    zero_count = 0
    mat = 0
    a=0

    for i in lottos:
        for j in win_nums:
            if i==j:
                mat += 1

    for i in lottos:
        if i == 0:
            zero_count+=1

    if mat == 6:
        a = 1
    elif mat ==5:
        a=2
    elif mat ==4:
        a=3
    elif mat ==3:
        a=4
    elif mat ==2:
        a=5
    else:
        a=6


    best = mat + zero_count

    if best == 6:
        b = 1
    elif best ==5:
        b=2
    elif best ==4:
        b=3
    elif best ==3:
        b=4
    elif best ==2:
        b=5
    else:
        b=6

    answer.append(b)
    answer.append(a)

    return answer

lottos = [44, 1, 0, 0, 31, 25]	
win_nums = [31, 10, 45, 1, 6, 19]

print(solution(lottos,win_nums))