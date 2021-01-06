def reverse(word):  #역순출력 함수
    revWord =""
    N = len(word)
    for i in range(1,N+1):
        revWord+=(word[N-i])           
    return revWord
   
A,B = input().split()
revA = reverse(A)
revB = reverse(B)
print(max(revA, revB))

#revA = A[::-1]
#list[<start>:<stop>:<step>] 이용
