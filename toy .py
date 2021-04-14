def prime(n):
    i=2
    while(i**2 <= n):
        if n% i == 0:
            return False
        else:
            i=i+1
    return True
 


      

def check (n):
    answer=[]
    for i in range(2,n+1):
      
        if prime(i) ==True:
            answer.append(i)

    return len(answer)



number=input("enter a number to check the prime numbers smaller  than or equal to it:")

print(check(int(number)))
                       
         






