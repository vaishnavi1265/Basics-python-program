n=int(input("Enter the Number:"))
s=n
b=len(str(n))
sum1=0
while n!=0: #153
    r=n%10   #153%10=3
    sum1=sum1+(r**b)  #3**3=9
    n=n//10 #15
if s==sum1:
    print("armstrong number")
else:
    print("not armstrong number")