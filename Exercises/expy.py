'''
n = int(input('n: '))

#Left justified
for i in range(n+1):
    print(('*'*i).ljust(n))

#Right justified
for i in range(n+1):
    print(('*'*i).rjust(n))

#Centre justified
for i in range(n+1):
    print(('*'*(2*i-1)).center(2*n-1))
'''
n = 26
for i in range(27, 52):
    print(i%26, end=',')