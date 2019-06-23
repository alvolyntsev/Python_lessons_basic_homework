number=int(input('введите число '))
while number>0:
    print(number%10)
    number=number//10
while number<0:
    print(10-number%10)  
    number=number//10+1