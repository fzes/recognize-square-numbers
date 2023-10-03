a = int(input('?'))
n = 0
while n <= a/2 :
    n = n + 1
    if n**2 == a :
        print('this is a squae number.')
        break
    elif n == a//2 :
        print('this is not a square number.')   