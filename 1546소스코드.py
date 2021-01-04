N = int(input())    #시험 본 과목 개수
original = list(map(int, input().split())) #실제 성적
total =0
maxScor = max(original)
for i in range(N):
    total += original[i]/maxScor*100    #조작점수 합
print("%0.2f"%(total/N))    #조작점수 평
