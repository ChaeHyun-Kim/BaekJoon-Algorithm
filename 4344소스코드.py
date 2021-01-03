case = int(input()) #테스트 케이스 개수
per =[]
for _ in range(case):
    n,*a =list(map(int,input().split()))    #학생 수n, n명의 점수리스트a
    avg=(sum(a)/n)
    plusnum =0
    for avgplus in a:
        if avgplus > avg:
            plusnum+=1       
    per.append(plusnum/n*100)   #전체 중 평균이상의 비율
for per in per:
    a=round(per,3)  #반올림함수 round()
    print("%.3f"%a+"%") #소수점 셋째 자리까지 출력
