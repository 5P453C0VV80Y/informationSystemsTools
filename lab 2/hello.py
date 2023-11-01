# Task 1
print (37/10)
print (37//10)
print (37%10)
print('--------TASK 1--------')
# Task 2
print ('hello world')
print('--------TASK 2--------')

#Task 3
a = 3
print(type(a))
a = 3.5
print(type(a))
a = 'qwerty'
print(type(a))
a = True
print(type(a))
a = '123'
print(type(a))
print('--------TASK 3--------')
#если попробовать сложить строку с числом -
#будет ошибка типа

#Task 4
asd = int(5.7)
print(asd)
asdf = int(-5.7)
print(asdf)
asdfg = int(float(3**39))
print(asdfg)
print('--------TASK 4--------')
#получилось очень большое число (????)

#Task 5
a = str(input('enter your name:'))
print('howdy,',a)
print('--------TASK 5--------')

#task 6
print('how many hours did the doctor drive to work?')
x = int(input())
print('how many minutes did the doctor walk from lunch to work?')
y = int(input())
print('minutes spent on the road:', ((x*60)+y))
print('--------TASK 6--------')

#task 7
a = False
b = True
c = False

z = (not (a or b) and c)
print(z)
print('--------TASK 7--------')

#TODO: didnt quite understand how to structure the solution
#task 8
print('enter the year')
year = int(input())
if((year > 1900) and (year < 3000)):
    print('norm')
else:
    print('out of range')

if (year % 400 == 0):
        print('happy birthday')        
else:
    print('nah, not that')

print('--------TASK 8--------')

#task 9
counter = 0
while True:
    if counter != 20:
        counter += 2
        print(counter)
    else:
        print('finish')
        break
    

print('--------TASK 9--------')

#task 10
x = int(input())
result = 0
while x:
    result += x
    x = int(input())
print('summ of entered values:',result)

print('--------TASK 10--------')

#task 11
p = int(input())
k = int(input())


