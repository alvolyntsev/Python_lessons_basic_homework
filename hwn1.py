number=int(input('введите число '))
maxnum=0
while number>0:
    if number%10>maxnum : maxnum = number%10
    number=number//10
#while number<0:
#    if 10-number%10>maxnum : maxnum = 10-number%10
#    number=number//10+1

print('maxnum=', maxnum)