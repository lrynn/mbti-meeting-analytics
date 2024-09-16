score_by_group = {
    'ENFJ':89,
    'INTJ':87,
    'ENFP':87,
    'ENTP':84,
    'INTP':81,
    'ESTP':78,
    'INFP':78,
    'ISFJ':72,
    'ISFP':72,
    'ESFP':64,
    'ENTJ':58,
    'ESFJ':55,
    'ESTJ':52,
    'INFJ':52,
    'ISTJ':49,
    'ISTP':47
}

def anno(group, num):
    print(group, '그룹의 점수 평균:', num)
    print('  전체 평균과의 차:', num - avg)

group = [['I', 'E'], ['S', 'N'], ['F', 'T'], ['J', 'P']]

avg = 0
for i in score_by_group.keys():
    avg += score_by_group[i]
avg /= 16
anno('전체', avg)
print('----')

# find 1
for i in group:
    for j in i:
        score = 0
        target_group = j
        for k in score_by_group.keys():
            if j in k:
                score += score_by_group[k]
        score /= 8
        anno(j, score)
    print('----')

# find 2
for i in range(3):
    for j in range(i+1, 4):
        for k in range(4): # 바이너리를 활용해서 두 리스트에 true, false 지정 해버리기
            score = 0
            target_group = ['', '']
            target = bin(k)[2:]
            if len(target) == 1:
                target = '0' + target
            target_group[0] = group[i][int(target[0])]
            target_group[1] = group[j][int(target[1])]
            for l in score_by_group.keys():
                boo = True
                for p in target_group:
                    if not p in l:
                        boo = False
                if boo:
                    score += score_by_group[l]
            score /= 4
            anno(target_group, score)
        print('----')
