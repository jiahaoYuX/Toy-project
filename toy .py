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

    return answer





number=1
while(number != 0):
    number=int(input("please insert any number or 0 to exit "))
    answerlist= check(number)
    if number in answerlist and number != 0:
        index=answerlist.index(number)
        print(str(number)+" is a prime number and it is " + str(index+1)+"th number")
    elif number == 0:
        print("exit the program")
        break
    else:
        print(str(number)+" is not a prime number")
    
                       
         




